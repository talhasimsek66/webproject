from django.contrib import admin
from .models import Continent, Country, Passport_type

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Passport_type)
