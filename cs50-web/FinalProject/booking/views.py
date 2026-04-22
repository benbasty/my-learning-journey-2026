from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from .models import User, Category, ClassType, ScheduledClass, Booking

def index(request):
    # Homepage - show all upcoming classes
    upcoming_classes = ScheduledClass.objects.filter(
        start_time__gte=timezone.now()
    ).order_by('start_time')

    return render(request, "booking/index.html", {
        "classes": upcoming_classes
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "booking/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "booking/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "booking/register.html", {
                "message": "Passwords must match."
            })

        # Check if user is registering as instructor (checkbox)
        is_instructor = request.POST.get("is_instructor") == "on"

        try:
            user = User.objects.create_user(username, email, password)
            user.is_instructor = is_instructor
            user.save()
        except IntegrityError:
            return render(request, "booking/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "booking/register.html")

def class_detail(request, class_id):
    """Show detailed info about a specific class"""
    scheduled_class = get_object_or_404(ScheduledClass, id=class_id)

    # Check if current user has already booked this class
    user_booking = None
    if request.user.is_authenticated:
        user_booking = Booking.objects.filter(
            student=request.user,
            scheduled_class=scheduled_class,
            status='confirmed'
        ).first()

    return render(request, "booking/class_detail.html", {
        "class": scheduled_class,
        "user_booking": user_booking,
        "remaining_spots": scheduled_class.remaining_spots()
    })

@login_required
def book_class(request, class_id):
    """Book a class (AJAX)"""
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    scheduled_class = get_object_or_404(ScheduledClass, id=class_id)

    # Check if class is in the future
    if scheduled_class.start_time <= timezone.now():
        return JsonResponse({"error": "Cannot book a class that has already started"}, status=400)

    # Check if already booked
    existing_booking = Booking.objects.filter(
        student=request.user, 
        scheduled_class=scheduled_class,
        status='confirmed'
    ).exists()

    if existing_booking:
        return JsonResponse({"error": "You already booked this class"}, status=400)

    # Check if class is full
    if scheduled_class.remaining_spots() <= 0:
        return JsonResponse({"error": "This class is full"}, status=400)

    # Create booking
    booking = Booking.objects.create(
        student=request.user,
        scheduled_class=scheduled_class,
        status='confirmed'
    )

    return JsonResponse({
        "success": True,
        "booking_id": booking.id,
        "remaining_spots": scheduled_class.remaining_spots(),
        "message": "Class booked successfully!"
    })

@login_required
def cancel_booking(request, booking_id):
    #Cancel a booking
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    booking = get_object_or_404(Booking, id=booking_id, student=request.user)

    # Check if class is in the future
    if booking.scheduled_class.start_time <= timezone.now():
        return JsonResponse({"error": "Cannot cancel a class that has already started"}, status=400)

    booking.status = 'cancelled'
    booking.save()

    return JsonResponse({
        "success": True,
        "remaining_spots": booking.scheduled_class.remaining_spots(),
        "message": "Booking cancelled successfully!"
    })

@login_required
def dashboard(request):
    #User dashboard - shows different content for instructors vs students
    if request.user.is_instructor:
        # Instructor view: classes they teach
        my_classes = ScheduledClass.objects.filter(instructor=request.user).order_by('start_time')
        return render(request, "booking/instructor_dashboard.html", {
            "my_classes": my_classes
        })
    else:
        # Student view: their bookings
        upcoming_bookings = Booking.objects.filter(
            student=request.user,
            status='confirmed',
            scheduled_class__start_time__gte=timezone.now()
        ).order_by('scheduled_class__start_time')

        past_bookings = Booking.objects.filter(
            student=request.user,
            scheduled_class__start_time__lt=timezone.now()
        ).order_by('-scheduled_class__start_time')

        return render(request, "booking/student_dashboard.html", {
            "upcoming_bookings": upcoming_bookings,
            "past_bookings": past_bookings
        })

@login_required
def create_class(request):
    """Instructor creates a new class"""
    if not request.user.is_instructor:
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":
        class_type_id = request.POST.get("class_type")
        start_time = request.POST.get("start_time")
        capacity = request.POST.get("capacity")
        location = request.POST.get("location")

        class_type = get_object_or_404(ClassType, id=class_type_id)

        from datetime import datetime
        start_time_dt = datetime.fromisoformat(start_time)

        scheduled_class = ScheduledClass.objects.create(
            class_type=class_type,
            instructor=request.user,
            start_time=start_time_dt,
            capacity=capacity,
            location=location
        )

        return HttpResponseRedirect(reverse("dashboard"))

    class_types = ClassType.objects.all()
    return render(request, "booking/create_class.html", {
        "class_types": class_types
    })

@login_required
def edit_class(request, class_id):
    """Instructor edits their own class"""
    scheduled_class = get_object_or_404(ScheduledClass, id=class_id)

    # Only the instructor who created it can edit
    if scheduled_class.instructor != request.user:
        return HttpResponseRedirect(reverse("dashboard"))

    if request.method == "POST":
        start_time = request.POST.get("start_time")
        capacity = request.POST.get("capacity")
        location = request.POST.get("location")

        from datetime import datetime
        scheduled_class.start_time = datetime.fromisoformat(start_time)
        scheduled_class.capacity = capacity
        scheduled_class.location = location
        scheduled_class.save()

        return HttpResponseRedirect(reverse("dashboard"))

    return render(request, "booking/edit_class.html", {
        "class": scheduled_class
    })

@login_required
def delete_class(request, class_id):
    """Instructor deletes their own class"""
    scheduled_class = get_object_or_404(ScheduledClass, id=class_id)

    if scheduled_class.instructor == request.user:
        scheduled_class.delete()

    return HttpResponseRedirect(reverse("dashboard"))