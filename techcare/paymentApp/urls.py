from django.urls import re_path
from techcare.paymentApp import views as pv




urlpatterns = [
        re_path(r'^book_payment/(?P<book_id>\d+)/', pv.bookingPayment, name="book_payment"),
        re_path(r'^payment_fails/(?P<book_id>\d+)/', pv.failPayment, name="payment_fails"),
        re_path(r'^payment_success/(?P<book_id>\d+)/', pv.successPayment, name="payment_success")
    
]