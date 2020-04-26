#-*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.from
from django.contrib import admin


from .models import Company, Order, Contact

admin.register(Company, Order, Contact)(admin.ModelAdmin)