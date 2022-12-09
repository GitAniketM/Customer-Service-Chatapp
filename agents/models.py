from django.db import models
from users.models import Customer
from config import settings

# Create your models here.
class Agents(models.Model):
    customer = models.ForeignKey(Customer, related_name="agent_customer", on_delete=models.CASCADE)
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="agent", on_delete=models.CASCADE)
    
