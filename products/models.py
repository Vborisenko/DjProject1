from django.db import models


# Create your models here.
# Remember to make a migration, after changing smth here
class Product(models.Model):
    title          = models.CharField(max_length=100)  #max_lenght is required
    description    = models.TextField(blank=True, null=True)
    price          = models.DecimalField(decimal_places=2, max_digits=10000)
    summary        = models.TextField()
