from django.contrib import admin
from .models import CentreonObjectStatus

@admin.register(Centreon)
class CentreonAdmin(admin.ModelAdmin):
    list_display = ('name', 'imported','state')