from django.db import models

# Create your models here.


class Note(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=255, default='заголовок')
    body = models.TextField(default='тело')
    read = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)