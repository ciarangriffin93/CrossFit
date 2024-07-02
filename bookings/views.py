from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GymClass, Booking
from django.contrib import messages

# Create your views here.
def gym_classes_list(request):
    gym_classes = GymClass.objects.all()
    return render(request, 'bookings/gym_classes_list.html', {'gym_classes': gym_classes})

@login_required
def book_gym_class(request, class_id):
    gym_class = GymClass.objects.get(id=class_id)
    if Booking.objects.filter(user=request.user, gym_class=gym_class).exists():
        messages.error(request, 'You have already booked this class.')
    elif gym_class.booking_set.count() >= gym_class.capacity:
        messages.error(request, 'This class is fully booked.')
    else:
        Booking.objects.create(user=request.user, gym_class=gym_class)
        messages.success(request, 'You have successfully booked the class.')
    return redirect('gym_classes_list')
