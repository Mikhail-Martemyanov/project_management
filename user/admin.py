from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(User, UserAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('for_user', 'text_task', 'author_task', 'status')


admin.site.register(Task, TaskAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('author_message', 'text_message', 'create_time')


admin.site.register(Message, MessageAdmin)

