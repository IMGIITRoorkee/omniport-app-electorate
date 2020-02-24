import swapper

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from electorate.models.candidate_profile import CandidateProfile
from electorate.serializers.posts_serializers import PostSerializer


class PostView(viewsets.ModelViewSet):

    queryset = CandidateProfile.objects.all()
    serializer_class = PostSerializer
