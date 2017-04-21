from django.contrib import admin
from .models import Manufacturer, GPU, CPU, Laptop


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cpu', 'GPU', 'battery')
    search_fields = ['model_name']


@admin.register(GPU)
class GPUAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'memory', 'benchmark')
    search_fields = ['name']


@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'clock_speed_min', 'clock_speed_max', 'description')
    search_fields = ['name']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description')
    search_fields = ['name']
