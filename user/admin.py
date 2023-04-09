from django.contrib import admin

# Register your models here.
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee')


admin.site.register(User, UserAdmin)
