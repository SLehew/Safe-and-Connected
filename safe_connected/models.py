from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField


class User(AbstractUser):

    CLIENT = "Client"
    MANAGER = "Manager"

    ROLE_CHOICES = [
        (CLIENT, "Client"),
        (MANAGER, "Manager"),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class Lang(models.Model):
    lang = models.CharField(max_length=100)

    def __str__(self):
        return self.lang


class ClientProfile(models.Model):

    client_zipcode = models.IntegerField(default=27514)
    client_children = models.BooleanField(default=False)
    client_notes = models.TextField(blank=True)
    client_phone = PhoneNumberField(blank=True)
    client = models.ForeignKey(
        to=User, on_delete=models.CASCADE, default=1)


class OrganizationProfile(models.Model):
    org_name = models.CharField(max_length=250)
    street_number = models.CharField(max_length=50, blank=True, null=True)
    street_name = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=25, default='27514')
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.org_name


class OrganizationMembership(models.Model):
    client = models.ForeignKey(to=ClientProfile, on_delete=models.CASCADE)
    organization = models.ForeignKey(
        to=OrganizationProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.client


class ClientLanguageMembership(models.Model):
    client = models.ForeignKey(to=ClientProfile, on_delete=models.CASCADE)
    client_language = models.ForeignKey(to=Lang, on_delete=models.CASCADE)


class OrgLanguageMembership(models.Model):
    organization = models.ForeignKey(
        to=OrganizationProfile, on_delete=models.CASCADE)
    org_language = models.ForeignKey(to=Lang, on_delete=models.CASCADE)


class EventType(models.Model):
    event_type = models.CharField(max_length=50)


class Event(models.Model):

    event_organizer = models.ForeignKey(
        to=User, on_delete=models.CASCADE)
    event_organization = models.ForeignKey(
        to=OrganizationProfile, on_delete=models.CASCADE)
    event_language = models.ForeignKey(
        to=Lang, on_delete=models.CASCADE, default=0)
    event_title = models.CharField(max_length=250)
    event_type = models.ForeignKey(
        to=EventType, on_delete=models.CASCADE, default=0)
    general_notes = models.TextField()
    location = AddressField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    privacy = models.BooleanField(default=False)
    max_attendees = models.IntegerField(blank=True, null=True)

    def __str__():
        return self.event_title
