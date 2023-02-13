from django.db import models


# Create your models here.

SCHEDULE = (
    ("8 AM to 9 AM", "8 AM to 9 AM"),
    ("9 AM to 10 AM", "9 AM to 10 AM"),
    ("10 AM to 11 AM", "10 AM to 11 AM"),
    ("11 AM to 12 PM", "11 AM to 12 PM"),
    ("2 PM to 3 PM", "2 PM to 3 PM"),
    ("3 PM to 4 PM", "3 PM to 4 PM"),
    ("4 PM to 5 PM", "4 PM to 5 PM"),
    ("5 PM to 6 PM", "5 PM to 6 PM"),
)

class Appointment(models.Model):
    name = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    patient = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=20)
    schedule = models.CharField(max_length=20, choices=SCHEDULE)
    backup_schedule = models.CharField(max_length=20,blank=True, choices=SCHEDULE)
    appointed_time = models.CharField(max_length=20, choices=SCHEDULE, null=True)
    message = models.CharField(max_length=20, blank=True)
    card_no = models.CharField(max_length=12, null=True)
    appointed_date = models.DateField(null=True)
    booked_date = models.DateField(null=True)
    appointed = models.BooleanField(default=False)

    def __str__(self):
        return self.patient
    
class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=20)
    message = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    



    