
from django.db import models

class MainModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateField(auto_now_add=True)

