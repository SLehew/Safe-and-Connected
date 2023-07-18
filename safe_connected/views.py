from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import EventSerializer
from .models import User, Event


class EventViewSet(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(event_orgranizer=self.request.user)
