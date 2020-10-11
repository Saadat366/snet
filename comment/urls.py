from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import *

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)
router.register(r'comment-to-comment', CommentToCommentViewSet)

urlpatterns = router.urls