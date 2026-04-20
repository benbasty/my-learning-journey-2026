from django.db import models
from django.contrib.auth.models import AbstractUser

# All models are here.

# everyone who uses the app is a user, but is either an instructor or a student
class User(AbstractUser):
    is_instructor = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.username

#helps students find out the type of class ... cardio or strength...
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# describe the type of class students chose ... zumba or barre...
class ClassType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.IntegerField(default=60)

    def __str__(self):
        return self.name

# about the scheduled class that the student signed up for
class ScheduledClass(models.Model):
    class_type = models.ForeignKey(ClassType, on_delete=models.CASCADE, related_name='scheduled_class')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_instructor': True})
    start_time = models.DateTimeField()
    capacity = models.IntegerField(default=18)
    location = models.CharField(max_length=200)

    def remaining_spots(self):
        booked = self.bookings.filter(status='confirmed').count()
        return self.capacity - booked


    def __str__(self):
        return f"{self.class_type.name} on {self.start_time.strftime('%Y-%m-%d %H:%M')}"

# Tracks which student is in which scheduled class, plus whether they showed up
class Booking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    scheduled_class = models.ForeignKey(ScheduledClass, on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    attended = models.BooleanField(default=False)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    # one booking per student per scheduled session
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'scheduled_class'],
                name='unique_booking'
            )
        ]

    def __str__(self):
        return f"{self.student.username} - {self.scheduled_class}"
