from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EventSerializer, EventRosterSerializer, LangSerializer
from .serializers import ClientProfileSerializer, OrganizationProfileSerializer
from .serializers import OrganizationMembershipSerializer, ClientLanguageMembershipSerializer
from .serializers import OrgLanguageMembershipSerializer, EventTypeSerializers
from .models import Event, EventRoster, Lang, ClientProfile, OrganizationProfile, OrganizationMembership
from .models import ClientLanguageMembership, OrgLanguageMembership, EventType


class EventViewSet(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(event_organizer=self.request.user)


class EventListViewSet(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "event_organizer",
        "event_organization",
        "event_language",
        "event_type",
        "event_title",
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(event_organizer=self.request.user)

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
        serializer.save(client_attendee=self.request.user)


class LanguageViewSet(generics.CreateAPIView):
    queryset = Lang.objects.all()
    serializer_class = LangSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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


class OrganizationProfileViewSet(generics.CreateAPIView):
    queryset = OrganizationProfile.objects.all()
    serializer_class = OrganizationProfileSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EditOrganizationProfileViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrganizationProfile.objects.all()
    serializer_class = OrganizationProfileSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrganizationMembershipViewSet(generics.CreateAPIView):
    queryset = OrganizationMembership.objects.all()
    serializer_class = OrganizationMembershipSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClientLanguageMembershipViewSet(generics.CreateAPIView):
    queryset = ClientLanguageMembership.objects.all()
    serializer_class = ClientLanguageMembershipSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrgLanguageMembershipViewSet(generics.CreateAPIView):
    queryset = OrgLanguageMembership.objects.all()
    serializer_class = OrgLanguageMembershipSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventTypeViewSet(generics.CreateAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializers

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
