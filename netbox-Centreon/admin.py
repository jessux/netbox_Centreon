from django.contrib import admin
from .models import netbox-Centreon

@admin.register(netbox-Centreon)
class centreon(admin.ModelAdmin):
    list_display = ('name', 'imported', 'state')