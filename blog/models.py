from django.db import models


# Create your models here.
class Article(models.Model):
    title   = models.CharField(max_length=50)
    content = models.TextField(blank=True, max_length=100000)
    active  = models.BooleanField(default=True)