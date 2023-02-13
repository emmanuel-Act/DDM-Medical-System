from .models import *
from django import forms

class AppointmentForm(forms.ModelForm):
    booked_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "date"
            }
        )
    )
    
    class Meta:
        model = Appointment 
        fields = ('patient', 'phone', 'email', 'booked_date', 'schedule', 'backup_schedule', 'message') 

class ScheduleAppointmentForm(forms.ModelForm):

    appointed_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "date"
            }
        )
    )
    
    class Meta:
        model = Appointment
        fields = ('name', 'card_no', 'patient', 'appointed_date', 'appointed_time')

class ContactUsForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = '__all__'