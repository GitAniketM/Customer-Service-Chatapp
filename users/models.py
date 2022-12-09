from django.contrib.auth.models import AbstractUser
from django.db import models
from config.settings import AUTH_USER_MODEL

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    
class Customer(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name="customer")
    is_occupied = models.BooleanField(default=False)