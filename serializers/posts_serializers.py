import swapper

from rest_framework import serializers

from electorate.models.candidate_profile import CandidateProfile
from electorate.serializers.question_serializer import QuestionSerializer
from electorate.serializers.candidate_profile_serializer import CandidateProfileSerializer

class PostSerializer(serializers.ModelSerializer):
    
    # candidates = serializers.SerializerMethodField()
    
    # def get_candidates(self,instance):
    #     return {"candidates":CandidateProfile.objects.get(post = instance.post).student}

    class Meta:

        model = CandidateProfile
        fields = ['id', 'post']
