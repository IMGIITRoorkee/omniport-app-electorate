import logging

import swapper

from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from electorate.models.question import Question
from electorate.permissions.permissions import has_object_permission, has_candidate_permission, has_question_permission
from electorate.serializers.question_serializer import QuestionSerializer

Student = swapper.load_model('kernel', 'Student')
Residence = swapper.load_model('kernel', 'Residence')

logger = logging.getLogger('electorate')

class QuestionView(viewsets.ModelViewSet):

    serializer_class = QuestionSerializer

    def get_queryset(self):
        """
        Overrides the get queryset method to get Question model 
        objects and the candidate query parameters.
        """
        queryset = Question.objects.all()
        candidate = self.request.query_params.get('candidate', None)
        if candidate is not None:
            queryset = Question.objects.filter(candidate=candidate)
        return queryset

    def update(self, request, pk=None):
        """
        Overrides the update method in serializer to ensure that only the 
        candidate has the permission to answer the question.
        """

        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(obj, data=request.data)
        if serializer.is_valid():
            if has_candidate_permission(request, obj):
                if obj.answer is not None:
                    serializer.save(asker=request.person.student)
            else:
                return Response('Not allowed', status=HTTP_403_FORBIDDEN)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Overrides the destroy method in serializer to ensure that only the 
        asker can delete the question object.
        """

        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(obj)
        if has_question_permission(request, obj):
            if serializer.validated_data.answered is not None:
                obj.delete()
            else:
                return Response('Not allowed', status=HTTP_403_FORBIDDEN)
            return Response('deleted', status=HTTP_200_OK)
        return Response('Not Allowed', status=HTTP_404_NOT_FOUND)
