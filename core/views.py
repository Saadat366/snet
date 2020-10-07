from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

from .serializers import ProfileSerializer
from .models import Profile


class ProfileRetrieveView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    # lookup_field =