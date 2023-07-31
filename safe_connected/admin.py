from django.contrib import admin
from .models import User
from .models import OrganizationProfile, OrganizationMembership
from .models import EventType, Event, EventRoster, FileUpload


# Register your models here.
admin.site.register(User)
admin.site.register(OrganizationProfile)
admin.site.register(OrganizationMembership)
admin.site.register(EventType)
admin.site.register(Event)
admin.site.register(EventRoster)
admin.site.register(FileUpload)
