from django.contrib import admin
from .models import CentreonObjects

@admin.register(CentreonObjects)
class centreon(admin.ModelAdmin):
    list_display = ('name', 'imported', 'state')