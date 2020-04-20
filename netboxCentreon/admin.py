from django.contrib import admin
from .models import netboxCentreon

@admin.register(netboxCentreon)
class centreon(admin.ModelAdmin):
    list_display = ('name', 'imported', 'state')