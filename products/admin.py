from django.contrib import admin
from .models import Item,Item_variation
# Register your models here.
admin.register(Item,Item_variation)(admin.ModelAdmin)
