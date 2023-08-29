from django.db import models
from django.contrib.auth.models import User
from techcare.userApp.models import Profile
from django.utils import timezone

class GeneralPurpose:
    dept = [("Emergency Care", "Emergency Care"),
            ("Operation & Surgery", "Operation & Surgery"),
            ("Outdoor Checkup", "Outdoor Checkup"),
            ("Ambulance Service", "Ambulance Service"),
            ("Medicine & Pharmacy", "Medicine & Pharmacy"),
            ("Blood Testing", "Blood Testing"),
            ("General Health", "General Health"),
            ("Cardiology", "Cardiology"),
            ("Dental", "Dental"),
            ("Neurology", "Neurology"),
            ("Orthopaedics", "Orthopaedics"),
            
            ]
    
    
    user_status = [
        ("Unknown", "Unknown"),
        ("Booked for Test", "Booked for Test"),
        ("Transferred", "Transferred"),
        ("Admitted", "Admitted"),
        ("Discharged", "Discharged"),
        ("Dead", "Dead"),
        
    ]


class Service(models.Model):
    genP = GeneralPurpose()
    
    service_id = models.AutoField(primary_key=True)
    service_option = models.CharField(choices=genP.dept, max_length=20, null=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    HoD = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    service_logo = models.ImageField(upload_to="service_logo/", blank=True, null=True, unique=False)
    price = models.BigIntegerField(unique=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    


class BookingService(models.Model):
        genP = GeneralPurpose()
        
        booking_id = models.AutoField(primary_key=True)
        user = models.ForeignKey(User, null=False, blank=False, unique=False, on_delete=models.CASCADE)
        hod = models.ForeignKey(User, related_name="hod", null=False, blank=False, unique=False, on_delete=models.CASCADE, default=1)
        service_id = models.ForeignKey(Service, null=False, unique=False, on_delete=models.CASCADE)
        date_created = models.DateField(auto_now_add=True)
        consultant_doctor = models.ForeignKey(User, related_name="consultant_doctor", null=False, unique=False, on_delete=models.CASCADE, default=1)
        resident_doctor = models.ForeignKey(User, related_name="resident_doctor", null=False, unique=False, on_delete=models.CASCADE, default=1)
        approved_date = models.DateField(null=True, blank=True, unique=False)
        approved_time = models.TimeField(null=True, blank=True, unique=False)
        description = models.CharField(max_length=300, blank=True, null=True)
        service_name = models.CharField(max_length=300, blank=True, null=True, unique=False)
        payment = models.BooleanField(default=False, blank=True, null=True, unique=False)
        served = models.BooleanField(default=False, blank=True, null=True, unique=False)
        patient_status = models.CharField(choices=genP.user_status, max_length=20, unique=False, null=True)
        doctor_remark = models.CharField(max_length=100, blank=True, null=True, unique=False)
        price = models.BigIntegerField(unique=False, default=00)
        
        
        