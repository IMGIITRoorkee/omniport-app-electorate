import logging

import swapper

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from electorate.models.question import Question
from electorate.serializers.question_serializer import QuestionSerializer

logger = logging.getLogger('electorate')

class AnswerView(viewsets.ModelViewSet):

    queryset = Question.objects.all().order_by('answered').filter(answer="").reverse()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['candidate','post']
