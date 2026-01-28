from django import forms #importing forms module from django
from .models import  Reservation #ill be using reservation model to create the 2 forms

class Reservationform(forms.ModelForm):
    class Meta:
        model= Reservation
        fields = ['name', 'phonenumber', 'email', 'date', 'time', 'guests'] #all fields required or else form validation will fail
class Reservationpageform(forms.ModelForm):
    class Meta:
        model= Reservation
        fields = ['name', 'phonenumber', 'email', 'date', 'time', 'guests']
       