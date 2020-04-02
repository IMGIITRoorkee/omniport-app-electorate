import swapper

from rest_framework import serializers

from electorate.models.question import Question
from electorate.models.like import Like
from electorate.serializers.candidate_profile_serializer import CandidateProfileSerializer
from electorate.serializers.person import PersonSerializer
from electorate.serializers.candidate_profile_serializer import CandidateProfileSerializer


class QuestionCreateSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Question
        fields = [
            'id',
            'asker',
            'answered',
            'question',
            'answer',
            'candidate',
            'post',
            ]
