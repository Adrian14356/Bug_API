from django.contrib import admin

from .models import Users, Project

admin.site.register(Users)
admin.site.register(Project)