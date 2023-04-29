from rest_framework import generics
from .models import Location, Item
from .serializers import LocationSerializer, ItemSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django.contrib.auth import logout
from rest_framework.views import APIView


# Create your views here.
class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class SignUp(generics.GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signup.html'

    def get(self, request):
        content = {}
        return Response({'content': content})


class Login(generics.GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        content = {}
        return Response({'content': content})


class Dashboard(generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'

    def get(self, request):
      content = {}
      content['user'] = request.user
      return Response({'content': content})


class Logout(APIView):
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        logout(request)
        return redirect('/login')
