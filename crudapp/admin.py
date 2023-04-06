from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *


class EmployeeRegistration(admin.ModelAdmin):
    list_display=('id','name','address','phone','profileimage')
admin.site.register(registration, EmployeeRegistration)