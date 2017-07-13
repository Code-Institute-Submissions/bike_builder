from django.contrib import admin
from .models import Manufacturer, Layout, Bike


admin.site.register(Manufacturer)
admin.site.register(Layout)
admin.site.register(Bike)
