from django.contrib import admin
from .models import Delivery, Category, Address, Alarm


admin.site.register(Delivery)
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Alarm)