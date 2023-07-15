from django.db import models
from django.contrib.auth.models import AbstractUser


class User_Lang(models.Model):
    user_lang = models.CharField(max_length=100)

    def __str__(self):
        return self.user_lang


class Organization(models.Model):
    org_name = models.CharField(max_length=250)
    street_number = models.CharField(max_length=50, blank=True, null=True)
    street_name = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=25, default='27514')
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.org_name 



class User(AbstractUser):

    CLIENT = "Client"
    MANAGER = "Manager"
    ROLE_CHOICES = [
        (CLIENT, "Client"),
        (MANAGER, "Manager"),
    ]

    user_lang = models.ForeignKey(
        to=User_Lang, on_delete=models.CASCADE, blank=True, null=True)
    client_zipcode = models.IntegerField(default=27514)
    client_children = models.BooleanField(default=False)
    notes = models.TextField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    organization = models.ForeignKey(
        to=Organization, on_delete=models.CASCADE, blank=True, null=True)

    def __str(self):
        return self.username
