from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import *

router = routers.DefaultRouter()
router.register(r"publication", PublicationViewSet)

urlpatterns = [
    path("detail/<int:pk>/", publication),
    path("<username>/", UserPublicationListView.as_view()),
    path("<username>/feed/", FeedListView.as_view()),
    path("like/<user_id>/<publication_id>/", LikeView.as_view()),
]

urlpatterns += router.urls