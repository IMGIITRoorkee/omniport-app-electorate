import swapper

from rest_framework import serializers

from electorate.models.question import Question
from electorate.models.like import Like
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
    question_answered_or_not = serializers.SerializerMethodField()
    
    def get_question_answered_or_not(self,instance):
        if(instance.answer == ""):
            return "False"
        else:
            return "True"

    number_of_likes = serializers.SerializerMethodField()
    
    def get_number_of_likes(self,instance):
        return Like.objects.filter(question = instance).count()
    
    did_user_like = serializers.SerializerMethodField()
    
    def get_did_user_like(self,instance):
        return Like.objects.filter(question = instance,user = self.context['request'].person.student).exists()
    

    class Meta:
        model = Question
        fields = [
            'id',
            'asker',
            'did_user_like',
            'number_of_likes',
            'answered',
            'question',
            'answer',
            'candidate',
            'post',
            'question_answered_or_not',
            'asker_full_name',
            'asker_displayPicture',
            'candidate_full_name',
            'candidate_displayPicture']
