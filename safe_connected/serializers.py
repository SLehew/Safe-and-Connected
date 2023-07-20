from rest_framework import serializers
from .models import Event, EventRoster, Lang, ClientProfile, OrganizationProfile
from .models import OrganizationMembership, ClientLanguageMembership
from .models import OrgLanguageMembership, EventType, FileUpload


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class EventRosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventRoster
        fields = '__all__'


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

    def validate(self, data):
        if data["client_profile"] and data["organization_profile"]:
            raise serializers.ValidationError(
                "Only one id allowed for client_profile or organization_profile"
            )
        return data
