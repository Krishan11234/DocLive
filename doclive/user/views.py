from django.shortcuts import render

from rest_framework.permissions import AllowAny
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserRegisterSerializer, LoginSerializer
from .models import CustomUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .utils import response_data
from django.contrib.auth import login
from rest_framework.renderers import TemplateHTMLRenderer


class UserDetailAPI(APIView):
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]
  def get(self,request,*args,**kwargs):
    # user = CustomUser.objects.get(id=request.user.id)
    user = CustomUser.objects.all()
    serializer = UserSerializer(user)
    return Response(serializer.data)


class RegisterUserAPIView(generics.CreateAPIView):
  authentication_classes = []
  serializer_class = UserRegisterSerializer

  def create(self, request, *args, **kwargs):
    try:
      response = super().create(request, *args, **kwargs)
    except Exception as e:
      message = 'Missing Fields'
      if 'username' in e.args[0]:
        message = 'Username must be unique'
      elif 'phone_number' in e.args[0]:
        message = 'Incorrect Phone Number Please ' + e.args[0]['phone_number'][0]
      elif 'email' in e.args[0]:
        message = 'Incorrect Email ' + e.args[0]['email'][0]
      elif 'password' in e.args[0]:
        message = e.args[0]['password'][0]
      return response_data(400, message, {})

    return response_data(200, 'Registration has been successfully!', response.data)


class UserLoginAPI(APIView):
  authentication_classes = []
  serializer_class = LoginSerializer

  def post(self, request):
    try:
      serializer = self.serializer_class(data=self.request.data,
                                               context={'request': self.request})
      serializer.is_valid(raise_exception=True)
      user = serializer.validated_data['user']
      login(request, user)
      return response_data(200, 'Login Success', {})
    except Exception as e:
      message = "Failed Please Try After Some Time"
      if 'non_field_errors' in e.args[0]:
        message = e.args[0]['non_field_errors'][0]
      if 'username' in e.args[0]:
        message = 'Please fill Username'
      elif 'password' in e.args[0]:
        message = 'Please fill Password'
      return response_data(400, message, {})

