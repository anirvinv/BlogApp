from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
