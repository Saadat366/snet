from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from .serializers import *
from .models import *


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentToCommentViewSet(ModelViewSet):
    serializer_class = CommentToCommentSerializer
    queryset = CommentToComment.objects.all()