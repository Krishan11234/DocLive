from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView

# app_name = 'user'
urlpatterns = [
  path('get-user-details/', UserDetailAPI.as_view()),
  path('user-register/', RegisterUserAPIView.as_view()),
]