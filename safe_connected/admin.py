from django.contrib import admin
from .models import User, Lang, ClientProfile, ClientLanguageMembership
from .models import OrganizationProfile, OrganizationMembership, OrgLanguageMembership


# Register your models here.
admin.site.register(User)
admin.site.register(Lang)
admin.site.register(ClientProfile)
admin.site.register(ClientLanguageMembership)
admin.site.register(OrganizationProfile)
admin.site.register(OrganizationMembership)
admin.site.register(OrgLanguageMembership)
