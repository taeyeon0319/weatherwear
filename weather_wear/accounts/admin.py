from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'gender', 'email', 'age', 'bodyForm',)
    list_filter= ['bodyForm', 'gender']
admin.site.register(UserProfile, UserProfileAdmin)