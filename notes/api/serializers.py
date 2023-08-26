from rest_framework import serializers
from notes.models import Note

class NoteSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(source="user.id", read_only=True)
    snippet = serializers.CharField(read_only=True)
    class Meta:
        model = Note
        fields = ("id", "title", "text", "snippet", "timestamp", "user", )