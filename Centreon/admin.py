from django.contrib import admin
from .models import Centreon

@admin.register(Centreon)
class centreon(admin.ModelAdmin):
    list_display = ('name', 'imported', 'state')