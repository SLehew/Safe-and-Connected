from rest_framework import serializers
from .models import Event, EventRoster, Lang, ClientProfile, OrganizationProfile
from .models import OrganizationMembership, ClientLanguageMembership, ManagerOrgMembership
from .models import OrgLanguageMembership, EventType, FileUpload, User
from djoser.serializers import UserSerializer, UserCreateSerializer
from PIL import Image
from io import BytesIO
import boto3
from django.core.files.uploadedfile import InMemoryUploadedFile
from config import settings


class UserRegistrationSerializer(UserCreateSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'username', 'role', 'password',
                  'id', 'first_name', 'last_name', 'full_name', 'language', 'user_avatar')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def create(self, validated_data):

        uploaded_image = validated_data.get('file')

        if uploaded_image:
            # Process the image using Pillow (optional)
            image = Image.open(uploaded_image)
            # Prepare the image to be saved to AWS S3
            buffer = BytesIO()
            # Set Format
            image.save(buffer, format='JPEG')

            # Create a new InMemoryUploadedFile to save to AWS S3
            file_name = uploaded_image.name
            file_size = buffer.tell()
            content_type = f"image/{image.format.lower()}"
            buffer.seek(0)
            uploaded_image = InMemoryUploadedFile(
                buffer, None, file_name, content_type, file_size, None
            )

            # Save the modified image to AWS S3
            s3 = boto3.client('s3')
            s3.upload_fileobj(
                uploaded_image, settings.AWS_STORAGE_BUCKET_NAME, file_name)

        return super().create(validated_data)


class UserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        model = User
        fields = ('email', 'username', 'role', 'id',
                  'first_name', 'last_name', 'language', 'user_avatar')


class EventSerializer(serializers.ModelSerializer):
    number_attending = serializers.SerializerMethodField(read_only=True)
    full_address = serializers.SerializerMethodField(read_only=True)

    def get_number_attending(self, obj):
        return obj.event_attendees.count()

    class Meta:
        model = Event
        fields = ('id', 'event_title', 'general_notes', 'event_date',
                  'start_time', 'end_time', 'event_type', 'number_attending', 'street_number', 'street_name', 'city', 'state', 'zipcode', 'privacy', 'max_attendees', 'full_address')

    def get_full_address(self, obj):
        return f"{obj.street_number} {obj.street_name} {obj.city}, {obj.state} {obj.zipcode}"


class OrgListEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('event_organization', 'event_title', 'event_date',
                  'start_time', 'end_time', 'event_type')


class EventRosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['event_attendees']


class EventRosterNameSerializer(serializers.ModelSerializer):

    event_attendees = serializers.SlugRelatedField(
        many=True, slug_field='username', queryset=User.objects.all())

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


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = [
            "id",
            "client_profile",
            "organization_profile",
            "event",
            "file",
        ]

    def create(self, validated_data):

        uploaded_image = validated_data.get('file')

        if uploaded_image:
            # Process the image using Pillow (optional)
            image = Image.open(uploaded_image)
            # Prepare the image to be saved to AWS S3
            buffer = BytesIO()
            # Set Format
            image.save(buffer, format='JPEG')

            # Create a new InMemoryUploadedFile to save to AWS S3
            file_name = uploaded_image.name
            file_size = buffer.tell()
            content_type = f"image/{image.format.lower()}"
            buffer.seek(0)
            uploaded_image = InMemoryUploadedFile(
                buffer, None, file_name, content_type, file_size, None
            )

            # Save the modified image to AWS S3
            s3 = boto3.client('s3')
            s3.upload_fileobj(
                uploaded_image, settings.AWS_STORAGE_BUCKET_NAME, file_name)

        return super().create(validated_data)
