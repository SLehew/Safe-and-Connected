from rest_framework import serializers
from .models import User, Event, Lang, OrganizationProfile, ClientProfile
from .models import OrganizationMembership


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lang
        fields = '__all__'


class OrganizationProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationProfile
        fields = '__all__'


class ClientProfileSeralizer(serializers.ModelSerializer):

    class Meta:
        model = ClientProfile
        fields = '__all__'


class OrganizationMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationMembership
        fields = '__all__'
