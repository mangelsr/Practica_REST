from django.contrib import admin
from . import models


admin.site.register(models.Airport)
admin.site.register(models.Airline)
admin.site.register(models.Route)
admin.site.register(models.Country)