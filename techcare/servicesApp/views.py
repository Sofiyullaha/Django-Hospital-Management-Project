from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from .forms import Services_form, BooksService_form
from django.contrib import messages
from .models import Service, BookingService
from django.urls import reverse
from django.db import transaction
from django.core.mail import send_mail


# Create your views here.


def indexService(request):
    services = Service.objects.all()
    services = services[0:3]
    return render(request=request, template_name='index.html', context={"services": services})


@login_required
def displayServices(request, display):
    services = Service.objects.all()
    if display == "service_nologin":
        return render(request=request, template_name='servicesApp/services.html', context={"services": services})
    
    else:
        return render(request=request, template_name='servicesApp/display_service.html', context={"services": services})
    
    
@login_required
def createService(request):
    if request.method == 'POST':
        service_form = Services_form(request.POST, request.FILES)
        if service_form.is_valid():
            service_form.save()
            
        return displayServices(request, "service_admin")
    
    
    else:
        service_form = Services_form
        return render(request=request, template_name='servicesApp/create_service.html', context= {"serviceForm": service_form})
    
    

@login_required
def editServices(request, serv_id):
    form = get_object_or_404(Service, service_id= serv_id)
    if request.method == "POST":
        service_form = Services_form(request.POST or None, request.FILES or None, instance=form)
        if service_form.is_valid():
            service_form.save()
           
            messages.success(request, ("Your profile has been updated successfully!"))
            return HttpResponsePermanentRedirect(reverse('display_service', args=("service_admin",)))
        
        else:
            messages.error(request, ("Please correct the error below."))
            return HttpResponsePermanentRedirect(reverse('edit_service', args=(serv_id)))
    
    else:
        
        service_form = Services_form(instance=form)
        return render(request, 'services/edit_services_form.html', {
            'service_form' : service_form,
            
        })


@transaction.atomic
@login_required
def serviceDetail(request, serv_id):
    if request.method == 'POST':
        service_form = BooksService_form(request.POST)
        service = Service.objects.get(service_id = serv_id)
        if service_form.is_valid():
            form = service_form.save(commit=False)
            form.hod_id = service.HoD_id
            form.user_id = request.user.id
            form.service_id = service
            form.price = service.price
            form.service_name = service.service_option
            form.save()
            
            # send mail notification to the doctor
            send_mail(
                'Booking has been made by a patient', #subject of the mail
                f'Deaer Dr. {service.HoD.first_name}, a patient has booked for a service. Please accept and fix an appointment with the patient. Thanks', #Body of the mail
                'ogunleyekolade@yahoo.com', #From email(Sender)
                [service.HoD.email], #To email (receiver)
                fail_silently=False, #Handle any error
            )
            messages.success(request, ('Booking created successfully!'))
            return HttpResponsePermanentRedirect(reverse('service_detail', args=(serv_id,)))
        else:
            messages.error(request, ('Please correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('service_detail', args=(serv_id,)))
    else:
        service_detail = Service.objects.filter(service_id=serv_id)
        service_form = BooksService_form()
        return render(request=request, template_name='servicesApp/service_details.html', context={"service_detail":service_detail,"serviceForm": service_form})
    
    

@login_required
def myBooking(request, user):
    booking = BookingService.objects.filter(user_id=user).order_by("approved_date")
    return render(request=request, template_name='servicesApp/my_booking.html', context={"booking_service":booking})

@login_required
def patientBooking(request, user):
    if request.user.profile.position == "CMD":
        my_booking = BookingService.objects.all().order_by('date_created').reverse()
    
    elif request.user.profile.position == "HOD":
        my_booking = BookingService.objects.filter(service_name=request.user.profile.department).order_by('date_created').reverse()
        
    elif request.user.profile.position == "Consultant":
        my_booking = BookingService.objects.filter(consultant_doctor_id = request.user.id, service_name = request.user.profile.department).order_by('date_created').reverse()
    
    elif request.user.profile.position == "Resident doctor":
        my_booking = BookingService.objects.filter(resident_doctor_id = request.user.id, service_name = request.user.profile.department).order_by('date_created').reverse()
    
    
    return render(request=request, template_name='servicesApp/patient_booking.html', context={"patient_booking": my_booking})


    
@login_required
def viewBookingDetail(request):
   my_booking = BookingService.objects.filter(booking_id = book_id)
   return render (request, "servicesApp/view_booking_details.html", {"booking": my_booking})


@login_required
def bookingPayment(request, book_id):
   pass


@login_required
def acceptBooking(request, book_id):
   pass


@login_required
def declineBooking(request, book_id):
   pass


@login_required
def editBooking(request, book_id):
   pass