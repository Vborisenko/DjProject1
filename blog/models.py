from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title   = models.CharField(max_length=50)
    content = models.TextField(blank=True, max_length=100000)
    active  = models.BooleanField(default=True)

    def get_absolute_url(self):        # critical important to override this method!
        return reverse("articles:article-detail", kwargs={"id": self.id})