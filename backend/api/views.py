from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
# Handles API requests and responses

# To connect our Auth routes
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()  # Get all users from the database.
    serializer_class = UserSerializer  # Tells this view, what kind of data we need to accept to make a new user, in this case it's User data
    permission_classes = [AllowAny] # Allows public access (no authentication required)
    

# To create Notes and list all notes of the current user
class NoteListCreate(generics.ListCreateAPIView): # ListCreateAPIView is a pre-built view that allows us to list and also create notes
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can access this view
    
    def get_queryset(self): # This function is called when we want to get all the notes of the current user who is logged in
        user = self.request.user # Get the current user who is logged in and then get all the notes of that user from the database 
        return Note.objects.filter(author = user) # Get all notes of the current user
    
    def perform_create(self, serializer): # This function is called when a new note is created by the user and it will automatically set the author of the note to the current user who is logged in
        if serializer.is_valid(): # If the data is valid then save the author of the note as the current user who is logged in and then save the note to the database
            serializer.save(author = self.request.user) # self.request.user is the current user who is logged in
        else :
            print(serializer.errors)
            
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self): # This function only deletes the notes the current user has created
        user = self.request.user
        return Note.objects.filter(author = user)