from django.contrib import admin
from .models import Manufacturers, Layouts, Bikes


# Register your models here.
admin.site.register(Manufacturers)
admin.site.register(Layouts)
admin.site.register(Bikes)
