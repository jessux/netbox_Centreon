from django.contrib import admin
from .models import Centreon

@admin.register(Centreon)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'imported', 'state')