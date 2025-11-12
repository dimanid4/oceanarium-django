from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BookingForm

@login_required
def book_tour(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return render(request, 'bookings/booking_success.html', {'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})
