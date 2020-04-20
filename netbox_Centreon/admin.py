from django.contrib import admin
from .models import CentreonObjectStatus

@admin.register(CentreonObjectStatus)
class CentreonObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'imported', 'state')