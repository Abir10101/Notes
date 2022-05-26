from rest_framework import serializers
from .models import Note


class NoteSerializer( serializers.ModelSerializer ):
    body = serializers.CharField( max_length=300 )
    class Meta:
        model = Note
        fields = "__all__"