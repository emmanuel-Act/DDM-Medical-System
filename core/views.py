from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from accounts.models import User
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')



def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Message sent Successfully"
            send_mail('A DDM user', 'You have a message from a user.', settings.EMAIL_HOST_USER, ['emmanueltessema@gmail.com'], fail_silently=False)
            return redirect('patient_home')
        else:
            print(form.errors)
            return redirect('contact_us')
    else:
        form = ContactUsForm() 
    return render(request, 'contact_us.html', {'form':form})
    
def user_messages(request):
    messages = ContactUs.objects.all()
    return render(request, "user_messages.html", {'messages': messages})


def user_approval(request):
    app = User.objects.all()
    if request.user.is_admin:
        if request.method == 'POST':
            
            id_list = request.POST.getlist('box')
            
            #uncheck every box before updating
            app.update(approved = False)
            
            #update datebase
            for x in id_list:
                User.objects.filter(pk=int(x)).update(approved=True)
            send_mail('A DDM user', 'You have registered successfully', settings.EMAIL_HOST_USER, ['emmanueltessema@gmail.com'], fail_silently=False)
            messages.success(request, ("You have successfully updated the user approval state."))
            return redirect('admin_home')
            
        else:
            return render(request, 'registration_approval.html',{'app':app} )
    else:
        messages.success(request, ("You aren't authorized to access this page."))
        return redirect('/')
    return render(request, 'registration_approval.html')

def book_appointment(request, pk):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print(form)
            post =  form.save(commit=False)
            post.name = request.user
            post.save()
            msg = "Appointment sent Successfully"
            return redirect('patient_home')
        else:
            print(form.errors)
            return redirect('book_appointment', pk=pk)
    else:
        form = AppointmentForm() 
    return render(request, 'book_appointment.html', {'form':form})

def appointments(request):
    appointment = Appointment.objects.all()
    return render(request, "appointments.html", {'appointment': appointment})

def schedule_appointment(request, pk):
    appt = Appointment.objects.get(pk=pk)
    if request.method == 'POST':
        form = ScheduleAppointmentForm(request.POST, instance=appt)
        if form.is_valid():
            #print(form)
            # post = form.save(commit=False)
            # post.appointed = True
            # post.save()
            form.save()
            msg = "Appointment scheduled Successfully"
            return redirect('admin_home')
        else:
            print(form.errors)
            return redirect('schedule_appointment')
  
    form = ScheduleAppointmentForm(instance=appt) 
    return render(request, 'schedule_appointment.html', {'form':form})


def cards(request):
    card = Appointment.objects.filter(name=request.user)
    return render(request, "card.html", {'card': card})
