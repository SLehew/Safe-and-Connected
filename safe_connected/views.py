from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EventSerializer
from .models import User, Event


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
