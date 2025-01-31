import logging

import swapper

from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from electorate.models.question import Question
from electorate.permissions.permissions import has_object_permission, has_candidate_permission, has_question_permission
from electorate.serializers.question_serializer import QuestionSerializer
from electorate.serializers.question_serializer_create import QuestionCreateSerializer
from electorate.utils.create_question_notifications import create_question_notifications
from electorate.utils.answer_question_notifications import answer_question_notifications

Student = swapper.load_model('kernel', 'Student')
Residence = swapper.load_model('kernel', 'Residence')

logger = logging.getLogger('electorate')

class QuestionView(viewsets.ModelViewSet):

    queryset = Question.objects.all().order_by('answered').reverse()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['candidate', 'post', 'candidate__student__enrolment_number']

    def partial_update(self, request, pk=None):
        """
        Overrides the update method in serializer to ensure that only the 
        candidate has the permission to answer the question.
        """

        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = QuestionCreateSerializer(obj, data=request.data, partial = True)
        if serializer.is_valid():
            candidate = serializer.validated_data.get('candidate')
            if has_candidate_permission(request, obj):
                serializer.save()
                answer_question_notifications(self.request.person,obj)
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
            if (obj.answer==""):
                obj.delete()
            else:
                return Response('Not allowed', status=HTTP_403_FORBIDDEN)
            return Response('deleted', status=HTTP_200_OK)
        return Response('Not Allowed', status=HTTP_404_NOT_FOUND)

    def create(self, request, pk=None):
        """
        Create a question object 
        """
        queryset = self.get_queryset()
        serializer = QuestionCreateSerializer(data=request.data)
        if serializer.is_valid():
            candidate = serializer.validated_data.get('candidate')
            question = serializer.save(post = candidate.post,asker = request.person)
            create_question_notifications(self.request.person,question)
            logger.info(
                f'Successfully created question {question.question} '
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
