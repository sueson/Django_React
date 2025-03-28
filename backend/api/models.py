from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Django models are used to create database tables with the help of ORM (Object Relational Mapping)
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # If the user is deleted, all their notes will also be deleted (CASCADE).
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    
    def __str__(self):
        return self.title
