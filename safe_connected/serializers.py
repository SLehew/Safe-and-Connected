from rest_framework import serializers
from .models import Event, EventRoster, Lang, ClientProfile, OrganizationProfile
from .models import OrganizationMembership, ClientLanguageMembership, ManagerOrgMembership
from .models import OrgLanguageMembership, EventType, FileUpload, User
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'username', 'role', 'password',
                  'id', 'first_name', 'last_name', 'full_name')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class UserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        model = User
        fields = ('email', 'username', 'role', 'id', 'first_name', 'last_name')


class EventSerializer(serializers.ModelSerializer):
    number_attending = serializers.SerializerMethodField(read_only=True)
    full_address = serializers.SerializerMethodField(read_only=True)

    def get_number_attending(self, obj):
        return obj.event_attendees.count()

    class Meta:
        model = Event
        fields = ('id', 'event_title', 'general_notes',
                  'start_time', 'end_time', 'event_type', 'number_attending', 'event_language', 'street_number', 'street_name', 'city', 'state', 'zipcode', 'privacy', 'max_attendees', 'full_address')

    def get_full_address(self, obj):
        return f"{obj.street_number} {obj.street_name} {obj.city}, {obj.state} {obj.zipcode}"


class OrgListEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('event_organization', 'event_title',
                  'start_time', 'end_time', 'event_type')


class EventRosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['event_attendees']


class EventRosterSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventRoster
        fields = ['event_id']


class LangSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lang
        fields = '__all__'


class ClientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientProfile
        fields = '__all__'


class OrganizationProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationProfile
        fields = '__all__'


class OrganizationMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationMembership
        fields = '__all__'

# class ManagerMembershipSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ManagerOrgMembership
#         fields = '__all__'


class ClientLanguageMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientLanguageMembership
        fields = '__all__'


class OrgLanguageMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrgLanguageMembership
        fields = '__all__'


class EventTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = EventType
        fields = '__all__'


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = [
            "id",
            "client_profile",
            "organization_profile",
            "event",
            "file",
        ]


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationMembership
        fields = '__all__'
