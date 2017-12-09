from django.contrib import admin
from .models import Manufacturer, GPU, CPU, Laptop


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'cpu', 'GPU', 'battery')
    search_fields = ['model_name', 'id']


@admin.register(GPU)
class GPUAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'memory')
    search_fields = ['name', 'id']


@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'clock_speed_min', 'clock_speed_max', 'description')
    search_fields = ['name', 'id']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'description')
    search_fields = ['name', 'id']
