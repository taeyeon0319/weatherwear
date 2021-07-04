from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import MyClothes
# Register your models here.

admin.site.register(MyClothes)