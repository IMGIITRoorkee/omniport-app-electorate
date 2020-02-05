import swapper

from rest_framework import serializers

from electorate.models.question import Question
from electorate.serializers.candidate_profile_serializer import CandidateProfileSerializer
from electorate.serializers.person import PersonSerializer
from electorate.serializers.candidate_profile_serializer import CandidateProfileSerializer


class QuestionSerializer(serializers.ModelSerializer):

    asker_full_name = serializers.CharField(
        source='asker.person.full_name',
        read_only=True
    )
    asker_displayPicture = serializers.FileField(
        source='asker.person.display_picture',
        read_only=True
    )

    candidate_full_name = serializers.CharField(
        source='candidate.student.person.full_name',
        read_only=True
    )
    candidate_displayPicture = serializers.FileField(
        source='candidate.student.person.display_picture',
        read_only=True
    )

    class Meta:
        model = Question
        fields = [
            'asker',
            'answered',
            'question',
            'answer',
            'candidate',
            'asker_full_name',
            'asker_displayPicture',
            'candidate_full_name',
            'candidate_displayPicture']
