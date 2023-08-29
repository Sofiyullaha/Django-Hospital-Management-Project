from django import forms
from django.contrib.auth.models import User
from techcare.userApp.models import Profile
from .models import Service, BookingService


class Services_form(forms.ModelForm):
    
    
    list_HOD = []
    for hod in Profile.objects.all().filter(position="HOD"):
        list_HOD.append((hod.user_id, hod.user.first_name + " " + hod.user.last_name + " (" + hod.department + ")" ))
        print(list_HOD)
        service_logo = forms.FileField(required=False)
    HoD = forms.ChoiceField(choices=list_HOD, required=True)
    description = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = Service
        fields = [
            'service_option',
            'HoD',
            'service_logo',
            'price',
            'description',
        ]
        
        
            
class BooksService_form(forms.ModelForm):

    class Meta:
        model = BookingService
        fields = [
         
            'description',
        ]
        
        widgets = {
           
            "description": forms.Textarea(attrs={'cols':60, 'row': 3}),
        }
        
        
class AcceptBooksService_form(forms.ModelForm):

    class Meta:
        model = BookingService
        fields = [
            'description',
            'approved_date',
            'approved_time',
            'doctor_remark',
        ]
        
        widgets = {
           
           "approved_date": forms.NumberInput(attrs={'type': 'date'}),
           "approved_time": forms.NumberInput(attrs={'type': 'time'}),
            "description": forms.Textarea(attrs={'cols':60, 'row': 3}),
            "doctor_remark": forms.Textarea(attrs={'cols':60, 'row': 3}),
        }
        