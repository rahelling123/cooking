from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Restaurant(models.Model):
    restaurant_user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant_name = models.TextField(max_length=50)
    about = models.CharField(max_length=500)


class Customer(models.Model):
    customer_user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=500)