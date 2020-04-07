import swapper

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from electorate.models.like import Like
from electorate.serializers.like_serializer import LikeSerializer


class LikeView(viewsets.ModelViewSet):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    paginator = None
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user','question']

    def create(self, request, pk=None):
        """
        Create a Like object 
        """
        queryset = self.get_queryset()
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data.get('question')
            if not(Like.objects.filter(question = question, user = request.person).exists()):
                like = serializer.save(user = request.person)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Cant create an object", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

