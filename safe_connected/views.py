from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User_Lang, Organization, User
from .serializers import UserLanguageSerializer, OrganizationSerializer, UserSerializer

# Create your views here.

class UserViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrganisationViewSet(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer