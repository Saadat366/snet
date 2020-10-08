from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    subscription_count = serializers.SerializerMethodField()
    subscriber_count = serializers.SerializerMethodField()
    publication_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "user",
            "publication_count",
            "subscription_count",
            "subscriber_count"
        ]

    def get_subscription_count(self, obj):
        return obj.subscription.all().count()
    
    def get_subscriber_count(self, obj):
        return obj.user.subscriber.all().count()
    
    def get_publication_count(self, obj):
        return obj.user.publication.filter(deleted=False).count()


class UserSerializer(serializers.ModelSerializer):
    subscription_count = serializers.SerializerMethodField()
    subscriber_count = serializers.SerializerMethodField()
    publication_count = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    profile_photo = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "subscription_count",
            "subscriber_count",
            "publication_count",
            "description",
            "profile_photo"
            ]
    
    def get_subscription_count(self, obj):
        return obj.profile.subscription.all().count()
    
    def get_subscriber_count(self, obj):
        return obj.subscriber.all().count()
    
    def get_publication_count(self, obj):
        return obj.publication.filter(deleted=False).count()
    
    def get_description(self, obj):
        return obj.profile.description
    
    def get_profile_photo(self, obj):
        return obj.profile.profile_photo.url


class UserListSerializer(serializers.ModelSerializer):
    profile_photo = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "profile_photo", "first_name", "last_name"]
    
    def get_profile_photo(self, obj):
        return obj.profile.profile_photo.url