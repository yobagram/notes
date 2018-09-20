from rest_framework import serializers

from .models import Note


#сериализатор модели Note, содержит все ее поля
class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Note
        fields = ('id', 'text', 'read', 'created_at')