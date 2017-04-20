from django.contrib import admin
from .models import Manufacturer, GPU, CPU, Laptop

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(GPU)
admin.site.register(CPU)
admin.site.register(Laptop)
