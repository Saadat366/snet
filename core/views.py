from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, \
    ListAPIView, RetrieveUpdateAPIView

from .serializers import *
from .models import Profile


class ProfileRetrieveView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    # lookup_field =


class UserRetrieveView(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = "username"
    queryset = User.objects.filter(is_active=True)


class SubscribingListView(ListAPIView):
    serializer_class = UserListSerializer
    
    def get_queryset(self):
        username = self.kwargs["username"]
        user = User.objects.get(username=username)
        lst = user.profile.subscription.all()
        return lst


class SubscribersListView(ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        user = User.objects.get(username=username)
        lst = User.objects.filter(profile__subscription__in=[user])
        return lst


class UserEditView(RetrieveUpdateAPIView):
    serializer_class = UserEditSerializer
    queryset = User.objects.all()


class ProfileView(RetrieveAPIView):
    serializer_class = ProfileViewSerializer
    queryset = Profile.objects.all()


class ProfileEditView(RetrieveUpdateAPIView):
    serializer_class = ProfileEditSerializer
    queryset = Profile.objects.all()