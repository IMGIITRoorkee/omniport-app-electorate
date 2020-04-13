import swapper

from rest_framework import serializers

from electorate.models.question import Question
from electorate.models.like import Like
from electorate.serializers.candidate_profile_serializer import CandidateProfileSerializer
from electorate.serializers.person import PersonSerializer
from electorate.serializers.candidate_profile_serializer import CandidateProfileSerializer


class QuestionSerializer(serializers.ModelSerializer):

    asker_full_name = serializers.CharField(
        source='asker.full_name',
        read_only=True
    )
    asker_displayPicture = serializers.FileField(
        source='asker.display_picture',
        read_only=True
    )

    enrolment_number = serializers.IntegerField(
        source='candidate.student.enrolment_number',
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
    
    liked_question_id = serializers.SerializerMethodField()
    
    def get_liked_question_id(self,instance):
        if Like.objects.filter(question = instance,user = self.context['request'].person).exists():
            return Like.objects.get(question = instance, user = self.context['request'].person).id
        else:
            return "None"
        
    did_user_like = serializers.SerializerMethodField()
    
    def get_did_user_like(self,instance):
        return Like.objects.filter(question = instance,user = self.context['request'].person).exists()
    

    class Meta:
        model = Question
        fields = [
            'id',
            'asker',
            'did_user_like',
            'liked_question_id',
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
            'candidate_displayPicture',
            'enrolment_number'
            ]
