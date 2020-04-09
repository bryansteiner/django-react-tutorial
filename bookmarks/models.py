from django.db import models

# Create your models here.
class Bookmark(models.Model):
    url = models.URLField(max_length=2048)
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=2048)
    codeblock = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
