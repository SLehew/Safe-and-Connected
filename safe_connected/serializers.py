from rest_framework import serializers
from .models import User, Event, EventRoster


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class EventRosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventRoster
        fields = '__all__'
