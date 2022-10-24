# Create your models here.
import uuid
from django.db import models

    
    
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    icon_url = models.CharField(max_length=100)
    url = models.URLField()
    value = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name="categories")
    
    def __str__(self):
        return self.url
    