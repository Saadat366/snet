from django.urls import path
from .views import *


urlpatterns = [
    # path("<int:pk>/", ProfileRetrieveView.as_view(), name="profile"),
    path("<username>/", UserRetrieveView.as_view()),
    path("<username>/following/", SubscribingListView.as_view()),
    path("<username>/followers/", SubscribersListView.as_view()),
    path("user/edit/<int:pk>/", UserEditView.as_view()),
    path("profile/<int:pk>/", ProfileView.as_view()),
    path("profile/edit/<int:pk>/", ProfileEditView.as_view()),
]