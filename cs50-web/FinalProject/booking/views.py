from django.shortcuts import render
from django.utils import timezone
from .models import User, Category, ClassType, ScheduledClass, Booking

# Create your views here.

def index(request):
    upcoming_classes = ScheduledClass.objects.filter(start_time = timezone.now()).order_by('start_time')
    return render(request, 'booking/index.html', {
        'classes' : upcoming_classes
    })
