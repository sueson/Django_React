from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


# for converting model into JSON API
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} # password field is write-only, no-one can't read password, it will be automatically hashed
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}  # author field is read-only, no-one can't write author name, it will be automatically set to the current user