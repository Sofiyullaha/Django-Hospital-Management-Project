from django.shortcuts import render
from django.db import transaction
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect
from techcare.servicesApp.models import BookingService
from .models import Payment_service
from django.urls import reverse





# Create your views here.


@login_required
def bookingPayment(request):
   return render(request, 'paymentApp/payment.html')




@login_required
@transaction.atomic
def successPayment(request, book_id):
   reference = request.GET.get('reference')
   booking = BookingService.objects.get(booking_id = book_id)
   payment = Payment_service(user_id=request.user.id, booking_id=book_id, amount=booking.price, reference=reference)
   payment.save()
   
   payment = BookingService.objects.filter(booking_id=book_id).update(payment=True)
   
      #Send mail notification to the patient
           
   send_mail(
       'Booking payment has been made by a patient', #Subject of the mail
       f'Dear {booking.hod.first_name}, your booking appointment has been approved. See your booking details for more information or click on the <a href="http://127.0.0.1:8000/servicesApp/view_booking_detail/{booking.user_id}">booking</a>. Thanks \n http://127.0.0.1:8000/servicesApp/view_booking_detail/{booking.user_id}',  #Body of the mail
               
       'ibsoat@gmail.com', #From email (Sender)
       [booking.hod.email], #To email (Receiver)
        fail_silently=False, #Handle any error
           )
   
   messages.success(request, ('Your payment was successful'))
   return HttpResponsePermanentRedirect(reverse('patient_booking', args=(request.user.id,)))

@login_required
def failPayment(request, book_id):
   messages.error(request, ('Your payment fails!'))
   return HttpResponsePermanentRedirect(reverse('patient_booking', args=(request.user.id,)))
