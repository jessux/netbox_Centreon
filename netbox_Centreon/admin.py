from django.contrib import admin
from .models import CentreonObjectStatus

@admin.register(CentreonObjectStatus)
class CentreonAdmin(admin.ModelAdmin):
    list_display = ('name', 'imported','state')