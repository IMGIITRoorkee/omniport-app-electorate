import swapper

from rest_framework import serializers

from electorate.models.like import Like
from electorate.serializers.question_serializer import QuestionSerializer


class LikeSerializer(serializers.ModelSerializer):

    question_text = serializers.CharField(
        source='question.question',
        read_only=True
    )
    asker_name = serializers.CharField(
        source='user.person.full_name',
        read_only=True
    )

    class Meta:

        model = Like
        fields = ['question', 'user', 'liked', 'asker_name', 'question_text']
