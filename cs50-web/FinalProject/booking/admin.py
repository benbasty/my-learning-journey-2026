from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Category, ClassType, ScheduledClass, Booking

admin.site.register(User)
admin.site.register(Category)
admin.site.register(ClassType)
admin.site.register(ScheduledClass)
admin.site.register(Booking)