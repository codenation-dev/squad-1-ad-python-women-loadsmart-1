from rest_framework import serializers
from events.models import Event, Agent


class AgentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ["name", "status", "env", "version", "address"]


class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "level", "data", "archived", "date", "agent"]
