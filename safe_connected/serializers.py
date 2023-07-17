from rest_framework import serializers
from .models import User_Lang, Organization, User

class UserLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Lang
        fields = ("user_lang")

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Organization
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ["username", "avatar"]

