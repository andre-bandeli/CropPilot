from django.contrib import admin
from .models import Machine, Location

# Registre os modelos
@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity_kg') 
    search_fields = ('name',) 

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')
    list_filter = ('name',)