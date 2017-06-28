from django.contrib import admin
from .models import Manufacturer, Layout, Bike


# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Layout)
admin.site.register(Bike)

# from django.contrib import admin
# from .models import Manufacturers, Layouts, Bikes
#
#
# # Register your models here.
# admin.site.register(Manufacturers)
# admin.site.register(Layouts)
# admin.site.register(Bikes)
