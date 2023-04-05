from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView
urlpatterns = [
  path("get-user-details/",UserDetailAPI.as_view()),
  path('user-register/',RegisterUserAPIView.as_view()),
]