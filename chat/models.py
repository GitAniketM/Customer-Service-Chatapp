from django.db import models
from users.models import Customer
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    value = models.CharField(max_length=255, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(default=datetime.now) 
    

    