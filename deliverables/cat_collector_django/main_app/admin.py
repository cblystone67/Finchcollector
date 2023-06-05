from django.contrib import admin
from .models import Cat, Feeding, Toy

admin.site.register([Cat, Feeding, Toy])