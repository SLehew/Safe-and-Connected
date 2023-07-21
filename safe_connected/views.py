from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EventSerializer, EventRosterSerializer, LangSerializer
from .serializers import ClientProfileSerializer, OrganizationProfileSerializer, MembershipSerializer
from .serializers import OrganizationMembershipSerializer, ClientLanguageMembershipSerializer
from .serializers import OrgLanguageMembershipSerializer, EventTypeSerializers, FileUploadSerializer
from .models import Event, EventRoster, Lang, ClientProfile, OrganizationProfile, OrganizationMembership
from .models import ClientLanguageMembership, OrgLanguageMembership, EventType, FileUpload
from safe_connected.permissions import IsManagerOrReadOnly, IsManagerOrReadOnlyEventDetails, IsManagerOrReadOnlyCreateOrganiz

# Create an event


class EventViewSet(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [IsAuthenticated, IsManagerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(event_organizer=self.request.user)

# lists all of a clients events


class EventHomeClientViewSet(generics.ListAPIView):
    queryset = Event.objects.all(), OrganizationMembership.objects.all()
    serializer_class = EventSerializer

    permission_classes = [
        permissions.IsAuthenticated]

# List events by organizer, organization, language, or event type.


class EventListViewSet(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "event_organizer",
        "event_organization",
        "event_language",
        "event_type",
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(event_organizer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(event_organizer=self.request.user)


class EventDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [permissions.IsAuthenticated,
                          IsManagerOrReadOnlyEventDetails]

    def perform_create(self, serializer):
        serializer.save(event_organizer=self.request.user)


class EventSearchViewSet(APIView):
    def get(self, request, format=None):
        event_title = request.query_params.get("event_title")
        general_notes = request.query_params.get("general_notes")

        results = Event.objects.all()

        if event_title:
            results = results.filter(
                event_title__icontains=request.query_params.get("event_title")
            )
        if general_notes:
            results = results.filter(
                general_notes__icontains=request.query_params.get(
                    "general_notes")
            )

        serializer = EventSerializer(results, many=True)
        return Response(serializer.data)


class EventRosterCreateViewSet(generics.CreateAPIView):
    queryset = EventRoster.objects.all()
    serializer_class = EventRosterSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(client_attendee=self.request.user)


class EventRosterViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventRoster.objects.all()
    serializer_class = EventRosterSerializer
    search_fields = [
        "event_id",
        "client_attendee",
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(client_attendee=self.request.user)

    def perform_create(self, serializer):
        serializer.save()


class LanguageViewSet(generics.CreateAPIView):
    queryset = Lang.objects.all()
    serializer_class = LangSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class ClientProfileViewSet(generics.CreateAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class ClientProfileDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class OrganizationProfileViewSet(generics.ListCreateAPIView):
    queryset = OrganizationProfile.objects.all()
    serializer_class = OrganizationProfileSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsManagerOrReadOnlyCreateOrganiz]


class EditOrganizationProfileViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrganizationProfile.objects.all()
    serializer_class = OrganizationProfileSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrganizationMembershipViewSet(generics.ListCreateAPIView):
    queryset = OrganizationMembership.objects.all()
    serializer_class = OrganizationMembershipSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class ClientLanguageMembershipViewSet(generics.CreateAPIView):
    queryset = ClientLanguageMembership.objects.all()
    serializer_class = ClientLanguageMembershipSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class OrgLanguageMembershipViewSet(generics.CreateAPIView):
    queryset = OrgLanguageMembership.objects.all()
    serializer_class = OrgLanguageMembershipSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventTypeViewSet(generics.CreateAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializers

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UploadCreateView(generics.CreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    permission_classes = [permissions.IsAuthenticated]


class MembershipView(generics.ListAPIView):
    queryset = OrganizationMembership.objects.all()
    serializer_class = MembershipSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "member"
    ]

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(member=self.request.user)
