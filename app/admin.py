from django.contrib import admin
from .models import *
# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#     fields =['name','category']

admin.site.register(Category)
admin.site.register(Blog)

