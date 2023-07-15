from django.contrib import admin
from .models import User_Lang, Organization, User

# Register your models here.
admin.site.register(User_Lang)
admin.site.register(Organization)
admin.site.register(User)
