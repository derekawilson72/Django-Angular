from django.contrib import admin

# Register your models here.
from .models import  Report, Portfolio
admin.site.register(Report)
admin.site.register(Portfolio)
