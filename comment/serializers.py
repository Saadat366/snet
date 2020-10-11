from rest_framework.serializers import ModelSerializer
from .models import *


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "user",
            "publication",
            "text",
            "created",
            "updated"
        ]


class CommentToCommentSerializer(ModelSerializer):
    class Meta:
        model = CommentToComment
        fields = [
            "user",
            "comment",
            "answer_text",
            "created",
            "updated"
        ]