import swapper

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from electorate.models.like import Like
from electorate.serializers.like_serializer import LikeSerializer


class LikeView(viewsets.ModelViewSet):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
