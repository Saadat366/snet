from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *


class PublicationSerializer(ModelSerializer):
    likes = SerializerMethodField()

    class Meta:
        model = Publication
        fields = ["pk",
            "image",
            "likes",
            "description",
            "publisher",
            "created"]

    def get_likes(self, obj):
        return obj.like.count()


class UserPublicationListSerializer(ModelSerializer):
    likes = SerializerMethodField()

    class Meta:
        model = Publication
        fields = ["pk", "image", "likes"]

    def get_likes(self, obj):
            return obj.like.count()


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "user", "publication"]