from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EventSerializer, EventRosterSerializer, LangSerializer
from .serializers import ClientProfileSerializer, OrganizationProfileSerializer, MembershipSerializer
from .serializers import OrganizationMembershipSerializer, ClientLanguageMembershipSerializer, OrgListEventSerializer
from .serializers import OrgLanguageMembershipSerializer, EventTypeSerializers, FileUploadSerializer, UserRegistrationSerializer, EventRosterSignupSerializer, EventRosterNameSerializer
from .models import Event, EventRoster, Lang, ClientProfile, OrganizationProfile, OrganizationMembership
from .models import ClientLanguageMembership, OrgLanguageMembership, EventType, FileUpload, User
from safe_connected.permissions import IsManagerOrReadOnly, IsManagerOrReadOnlyEventDetails, IsManagerOrReadOnlyCreateOrganiz, IsManagerOrReadOnlyEditOrganiz, IsManagerOnlyClientList
from django.utils.timezone import now
# Create an event


class EventViewSet(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [IsAuthenticated, IsManagerOrReadOnly]

    def perform_create(self, serializer):
        event_organizer = self.request.user
        event_organization_id = event_organizer.organiz_memberships.first().organization_id
        serializer.save(event_organizer=event_organizer,
                        event_organization_id=event_organization_id)
        serializer.instance.email_event_create()


# lists all of a clients events


class EventHomeClientViewSet(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticated]
    # Filters to not show events that have past dates and orders by closest date

    def get_queryset(self):

        today = now().date()

        queryset = Event.objects.filter(event_date__gte=today) | Event.objects.filter(
            event_date__isnull=True)
        queryset = queryset.order_by('event_date')

        return queryset

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
        "event_date",
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # we need to work on this. it's filtering based on who created event
    def get_queryset(self):
        return self.queryset.filter(event_organizer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(event_organizer=self.request.user)


class OrgEventListViewSet(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = OrgListEventSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        org_id = self.kwargs['event_organization_id']
        user_in_organiz = Event.objects.filter(
            event_organizer=self.request.user, event_organization__id=org_id).exists()
        if not user_in_organiz:
            raise PermissionDenied('You are not allowed to do this')
        else:
            return Event.objects.filter(event_organization__id=org_id)

    # def get_queryset(self):
    #     org_id = self.kwargs['organization_id']

    #     return Event.objects.filter(event_organization__id=org_id)


class EventDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [permissions.IsAuthenticated,
                          IsManagerOrReadOnlyEventDetails]

    def perform_update(self, serializer):
        serializer.save(event_organizer=self.request.user)
        serializer.instance.email_event_edit()


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


class EventRosterCreateViewSet(generics.UpdateAPIView):
    queryset = EventRoster.objects.all()
    serializer_class = EventRosterSignupSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(attendee=self.request.user)
        serializer.instance.email_event_signup()


class EventRosterListViewSet(generics.ListAPIView):
    queryset = EventRoster.objects.all()
    serializer_class = EventRosterSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class EventRosterViewSet(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventRosterNameSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventRosterUpdateViewSet(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventRosterSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        event_instance = serializer.instance
        event_instance.event_attendees.add(
            self.request.user)
        event_instance.email_event_signup(self.request.user)
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

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsManagerOrReadOnlyEditOrganiz]


class OrganizationMembershipViewSet(generics.CreateAPIView):
    queryset = OrganizationMembership.objects.all()
    serializer_class = OrganizationMembershipSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


# class OrganizationClientViewSet(generics.ListAPIView):
#     queryset = OrganizationMembership.objects.all()
#     serializer_class = OrganizationMembershipSerializer

#     permission_classes = [permissions.IsAuthenticated]

#     def organization_clients(self, organization):

#         members = OrganizationMembership.objects.filter(organization)


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
        "member",
    ]

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(member=self.request.user)


class ClientListView(generics.ListAPIView):
    queryset = OrganizationMembership.objects.all()
    serializer_class = MembershipSerializer

    permission_classes = [permissions.IsAuthenticated, IsManagerOnlyClientList]

    def get_queryset(self):
        org_id = self.kwargs['organization_id']
        user_in_organiz = OrganizationMembership.objects.filter(
            member=self.request.user, organization__id=org_id).exists()
        if not user_in_organiz:
            raise PermissionDenied('You are not allowed to do this')
        else:
            return OrganizationMembership.objects.filter(organization__id=org_id)

        # return OrganizationMembership.objects.filter(organization__id=org_id)


class UserRoleView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
