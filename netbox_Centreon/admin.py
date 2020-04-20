from django.contrib import admin
from .models import CentreonObject

@admin.register(CentreonObject)
class centreon(admin.ModelAdmin):
    list_display = ('name', 'imported', 'state')