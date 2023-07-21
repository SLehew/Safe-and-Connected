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

    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, null=False, blank=False, default="Client")

    def __str__(self):
        return self.username

# Lang model is a table of all the languages used by organizations and clients


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

    def __str__(self):
        return self.client.username


class OrganizationProfile(models.Model):
    org_name = models.CharField(max_length=250)
    street_number = models.CharField(max_length=50, blank=True, null=True)
    street_name = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=25, default='27514')
    phone = PhoneNumberField(blank=True, null=True)
    org_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.org_name

# Identifies which organizations a client is affiliated with.


class OrganizationMembership(models.Model):
    client = models.ForeignKey(to=ClientProfile, on_delete=models.CASCADE)
    organization = models.ForeignKey(
        to=OrganizationProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.organization.org_name} {self.client}"

# Identifies which languages a client speaks.


class ClientLanguageMembership(models.Model):
    client = models.ForeignKey(to=ClientProfile, on_delete=models.CASCADE)
    client_language = models.ForeignKey(to=Lang, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client} {self.client_language}"

# Identifies which languages an organizations services.


class OrgLanguageMembership(models.Model):
    organization = models.ForeignKey(
        to=OrganizationProfile, on_delete=models.CASCADE)
    org_language = models.ForeignKey(to=Lang, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.organization.org_name} {self.org_language}"


class EventType(models.Model):
    event_type = models.CharField(max_length=50)

    def __str__(self):
        return self.event_type


class Event(models.Model):

    event_organizer = models.ForeignKey(
        to=User, on_delete=models.CASCADE, blank=True)
    event_organization = models.ForeignKey(
        to=OrganizationProfile, on_delete=models.CASCADE, blank=True)
    event_language = models.ForeignKey(
        to=Lang, on_delete=models.CASCADE, default=1)
    event_title = models.CharField(max_length=250)
    event_type = models.ForeignKey(
        to=EventType, on_delete=models.CASCADE, default=1)
    general_notes = models.TextField()
    street_number = models.CharField(max_length=50, blank=True, null=True)
    street_name = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=25, default='27514')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    privacy = models.BooleanField(default=False)
    max_attendees = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.event_title


class EventRoster(models.Model):
    event_id = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    attendee = models.ManyToManyField(to=User)

    def __str__(self):
        return f"{self.event_id} {self.attendee}"


class FileUpload(models.Model):
    client_profile = models.ForeignKey(
        to=ClientProfile, on_delete=models.CASCADE, blank=True, null=True)
    organization_profile = models.ForeignKey(
        to=OrganizationProfile, on_delete=models.CASCADE, blank=True, null=True)
    event = models.ForeignKey(
        to=Event, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to="uploads/")
    file_desc = models.CharField(max_length=50)

    def __str__(self):
        return self.file_desc
