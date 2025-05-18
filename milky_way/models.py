from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Star(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='stars/', default='stars/default.png')
    views_count = models.PositiveIntegerField(default = 0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
