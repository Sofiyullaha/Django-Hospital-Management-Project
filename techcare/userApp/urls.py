from django.urls import re_path
from techcare.userApp import views as vw



urlpatterns = [
    
    re_path(r'^my_account/(?P<_id>\d+)/',  vw.my_account, name="my_account"),
    re_path(r'^edit_account/(?P<_id>\d+)/',  vw.edit_account, name="edit_account"),
    re_path(r'^deactivate_account/(?P<_id>\d+)/',  vw.deactivate_account, name="deactivate_account"),
    re_path(r'^all_staff/(?P<user>\w+)/', vw.allUsers, name="all_staff"),
    re_path(r'^all_patients/(?P<user>\w+)/', vw.allUsers, name="all_patients"), 
    

    ]