import django.contrib.admin
from django.contrib import admin
from .models import studdetails, studmarks
# Register your models here.


admin.site.register(studdetails)
admin.site.register(studmarks)