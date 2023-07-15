from django.db import models
from django.contrib.auth.models import AbstractUser

class User_Lang(models.Model):
    user_lang = models.CharField(max_length=100)

class User(AbstractUser):
    CLIENT = "C"
    MANAGER = "M"
    ROLE_CHOICES = [
        (CLIENT, "Client"),
        (MANAGER, "Manager"),
    ]

    user_lang = models.ForeignKey(
        to=User_Lang, on_delete=models.CASCADE, default=0, related_name='languages')
    client_zipcode = models.IntegerField(default=27514)
    client_children = models.BooleanField(default=False)
    notes = models.TextField()
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    organization = models.ForeignKey(to=)


class Oranization(models.Model):
    org_name = models.CharField(max_length=250)
    org_lang = models.ForeignKey(to=User_Lang, default=0, related_name='languages', on_delete=models.CASCADE)
    street_number = models.CharField(max_length=50, blank=True, null=True)
    street_name = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=25, default='27514')
    phone = models.IntegerField(max_length=12, blank=True, null=True)
    
