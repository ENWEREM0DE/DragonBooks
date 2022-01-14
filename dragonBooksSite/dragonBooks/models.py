from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
    phoneNumber = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)