from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import SignUpForm, Profile_form, User_form
from .models import Profile
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
    
    
@login_required
def my_account(request, _id):
    profile = Profile.objects.all().filter(profile_id=_id)
    return render(request=request, template_name='userApp/my_account.html', context={'my_profile' : profile})


@login_required
def edit_account(request, _id):
    user = get_object_or_404(User, id=_id)
    if request.method == "POST":
        user_form = User_form(request.POST, instance=user)
        profile_form = Profile_form(request.POST or None, request.FILES or None, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ("Your profile has been updated successfully!"))
            return my_account(request, _id)
        
        else:
            messages.error(request, ("Please correct the error below."))
            return HttpResponsePermanentRedirect(reverse('edit_profile', args=(_id,)))
    
    else:
        
        user_form = User_form(instance=user)
        profile_form = Profile_form(instance=user.profile)
        return render(request, 'userapp/edit_profile_form.html', {
            'user_form' : user_form,
            'profile_form' : profile_form
        })

@login_required
def deactivate_account(request, _id):
    user = User.objects.get(id=_id)
    if user.is_active:
        User.objects.filter(id=_id).update(is_active=False)
        messages.success(request, ("Your profile has been deactivated successfully!"))
    else:
        User.objects.filter(id=_id).update(is_active=True)
        messages.success(request, ("Your profile has been activated successfully!"))
    return my_account(request, _id)

@login_required
def allUsers(request, user):
    if user == "staff":
        all_user = Profile.objects.filter(staff=True)
    else:
        all_user = Profile.objects.filter(staff=False)

    return render(request, 'userApp/display_users.html', {'all_user': all_user, 'user': user})