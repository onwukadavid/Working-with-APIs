from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

