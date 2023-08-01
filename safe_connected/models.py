from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import send_mail, EmailMessage
from config import settings
from datetime import date, time

# User model, Language sets preferred translation for user when viewing events.


class User(AbstractUser):

    CLIENT = "Client"
    MANAGER = "Manager"

    ROLE_CHOICES = [
        (CLIENT, "Client"),
        (MANAGER, "Manager"),
    ]

    SPANISH = "es"
    FRENCH = "fr"
    SWAHILI = "sw"
    ENGLISH = "en"

    LANGUAGE_CHOICES = [
        (SPANISH, "es"),
        (FRENCH, "fr"),
        (SWAHILI, "sw"),
        (ENGLISH, "en"),
    ]

    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES)
    language = models.CharField(
        max_length=5, choices=LANGUAGE_CHOICES)
    user_avatar = models.ImageField(
        upload_to="uploads/", null=True, blank=True)

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_user_avatar(self):
        if self.user_avatar:
            return self.user_avatar.url
        return None

# Lang model is a table of all the languages used by organizations and clients


class OrganizationProfile(models.Model):
    org_name = models.CharField(max_length=250)
    street_number = models.CharField(max_length=50, blank=True, null=True)
    street_name = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=25, default='27514')
    phone = PhoneNumberField(blank=True, null=True)
    org_notes = models.TextField(blank=True, null=True)
    org_avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.org_name

# Identifies which organizations a client is affiliated with.


class OrganizationMembership(models.Model):
    member = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='organiz_memberships')
    organization = models.ForeignKey(
        to=OrganizationProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.organization.org_name} {self.member}"


class EventType(models.Model):
    event_type = models.CharField(max_length=50)

    def __str__(self):
        return self.event_type


class Event(models.Model):

    event_organizer = models.ForeignKey(
        to=User, on_delete=models.CASCADE)
    event_organization = models.ForeignKey(
        to=OrganizationProfile, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=250)
    event_type = models.ForeignKey(
        to=EventType, on_delete=models.CASCADE, default=1)
    general_notes = models.TextField()
    street_number = models.CharField(max_length=50, blank=True, null=True)
    street_name = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=25, default='27514')
    event_date = models.DateField(default=date.today)
    start_time = models.TimeField(default=time(12, 0, 0))
    end_time = models.TimeField(default=time(12, 0, 0))
    privacy = models.BooleanField(default=False)
    max_attendees = models.IntegerField(blank=True, null=True)
    event_attendees = models.ManyToManyField(
        User, related_name='attended_events', blank=True)
    event_avatar = models.ImageField(null=True, blank=True)

    def email_event_create(self):

        email_to = [self.event_organizer.email]

        send_mail(
            subject=(f'{self.event_title} on {self.start_time}'),
            message=(
                f'{self.event_organizer}, you have successfully created an event titled {self.event_title}. It is scheduled for {self.event_date} from {self.start_time} to {self.end_time}.'),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=email_to,
            fail_silently=False

        )

    def email_event_signup(self, user):

        email_to = [user.email]

        send_mail(
            subject=(f'{self.event_title} on {self.start_time}'),
            message=(
                f'{user.first_name}, you have signed up to attend {self.event_title}. It is scheduled for {self.event_date} from {self.start_time} to {self.end_time}.'),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=email_to,
            fail_silently=False

        )

    def email_event_remove_signup(self, user):

        email_to = [user.email]

        send_mail(
            subject=(f'{self.event_title} on {self.start_time}'),
            message=(
                f'{user.first_name}, you have cancelled your sign up to attend {self.event_title}, on {self.event_date} from {self.start_time} to {self.end_time}.'),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=email_to,
            fail_silently=False

        )

    def email_event_edit(self):

        email = EmailMessage(
            subject=(f'{self.event_title} on {self.start_time}'),
            body=(
                f'{self.event_organizer}, has made a change to {self.event_title}. It is scheduled for {self.start_time}. Please check to make sure you can still attend.'),
            from_email=settings.EMAIL_HOST_USER,
            to=[self.event_organizer.email],
            bcc=self.event_attendees.all(),

        )
        email.send()

    def __str__(self):
        return self.event_title


class EventRoster(models.Model):
    event_id = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    attendee = models.ManyToManyField(to=User)

    def __str__(self):
        return f"{self.event_id} {self.attendee}"


class FileUpload(models.Model):
    client_profile = models.ForeignKey(
        to=User, on_delete=models.CASCADE, blank=True, null=True)
    organization_profile = models.ForeignKey(
        to=OrganizationProfile, on_delete=models.CASCADE, blank=True, null=True)
    event = models.ForeignKey(
        to=Event, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to="uploads/")
    file_desc = models.CharField(max_length=50)

    def __str__(self):
        return self.file_desc
