import swapper

from rest_framework import serializers

from electorate.models.like import Like
from electorate.serializers.question_serializer import QuestionSerializer


class LikeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Like
        fields = ['question', 'user']
