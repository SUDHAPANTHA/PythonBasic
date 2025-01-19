# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books/', null=True, blank=True)  # Optional image field
    description = models.TextField()
    
def __str__(self):
        return self.title
