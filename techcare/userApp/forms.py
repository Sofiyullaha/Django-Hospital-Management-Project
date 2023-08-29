from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUpForm(UserCreationForm):
    pass
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=100, help_text='Enter a valid email address')
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class Profile_form(forms.ModelForm):
    gend = [
        ("Male", "Male"),
        ("Female", "Female")
    ]
    
    user_status = [
        ("Active", "Active"),
        ("Resigned", "Resigned"),
        ("Retired", "Retired"),
        ("Transferred", "Transferred"),
        ("Admitted", "Admitted"),
        ("Discharged", "Discharged"),
        ("Dead", "Dead"),
    ]
    
    
    profile_passport = forms.ImageField(required=False, label="Your Passport")
    means_of_identity = forms.ImageField(required=False, label="Means of Identity")
    status = forms.ChoiceField(choices=user_status, required=True)
    gender = forms.ChoiceField(choices=gend, required=True, widget=forms.RadioSelect)
    particulars = forms.FileField(required=False, label="Particulars")
    class Meta:
        model = Profile
        fields = [
        'address',
        'phone',
        'date_of_birth',
        'gender',
        'nationality',
        'state',
        'means_of_identity',
        'particulars',
        'profile_passport',
        'position',
        'department',
        'marital_status',
        'blood_group',
        'next_of_kin',
        'status',
        'staff',
        ]
        
        widgets = {
            'date_of_birth': forms.NumberInput(attrs = {'type': 'date'}),
        }