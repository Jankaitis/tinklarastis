from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    body = HTMLField()

    def __str__(self):
        return f'"{self.title}" by {self.author}'

    def get_absolute_url(self):
        return reverse('home')
