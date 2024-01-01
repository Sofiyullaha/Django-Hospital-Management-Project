from django.db import models
from techcare.userApp.models import Profile
from techcare.servicesApp.models import BookingService

# Create your models here.

class Payment_service(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE)
    booking = models.ForeignKey(BookingService, null=False, on_delete=models.CASCADE, unique=False)
    amount = models.BigIntegerField(unique=False, null=False)
    date_of_payment = models.DateTimeField(auto_now_add=True, null=False)
    reference = models.CharField(null=False, max_length=50 )
