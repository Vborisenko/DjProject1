from django.db import models
from django.urls import reverse

# Create your models here.
# Remember to make a migration, after changing smth here


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_lenght is required
    description = models.TextField(blank=True, null=True, max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, null=True,
                               max_length=120)  # blank=True means that this field isn't required, null provides for database
    feature = models.BooleanField(default=True)

    def get_detail_url(self):
        # return f"../product/{self.id}/"        # hardcoding!
        return reverse("products: product-details", kwargs={"id": self.id})