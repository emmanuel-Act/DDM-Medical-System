from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import User
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    form = SignUpForm(request.POST, request.FILES)
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
                user = form.save()
                msg = 'Registration pending. We will approve your request after reviewing your credentials'
                return redirect('/')
        else:
            msg = 'form is not valid'
            return redirect('register')
    else:
        form = SignUpForm()
    return render(request,'registration.html', {'form': form, 'msg': msg})


def admin_login_page(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin_home')
            elif user is not None and user.is_doctor:
                msg= 'There is no admin with this username and password'
            elif user is not None and user.is_patient:
                msg= 'There is no admin with this username and password'
            else:
                msg= 'Wrong username or password'
    return render(request, 'admin_login.html', {'form': form, 'msg': msg})

def doctor_login_page(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_doctor:
                if user.approved:
                    login(request, user)
                    return redirect('doctor_home')
                else:
                    msg = "Your registration request is still pending"
            elif user is not None and user.is_admin:
                msg= 'There is no doctor with this username and password'
            elif user is not None and user.is_patient:
                msg= 'There is no doctor with this username and password'
            else:
                msg= 'Wrong username or password'
    return render(request, 'doctor_login.html', {'form': form, 'msg': msg})


def patient_login_page(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_patient:
                if user.approved:
                    login(request, user)
                    return redirect('patient_home')
                else:
                    msg = "Your registration request is still pending"
            elif user is not None and user.is_doctor:
                msg= 'There is no patient with this username and password'
            elif user is not None and user.is_admin:
                msg= 'There is no patient with this username and password'
            else:
                msg= 'Wrong username or password'
    return render(request, 'patient_login.html', {'form': form, 'msg': msg})



def admin(request):
    return render(request,'admin_home.html')


def doctor(request):
    return render(request,'doctor_home.html')


def patient(request):
    return render(request,'patient_home.html')

def user_logout(request):
    logout(request)
    return redirect('/')


def update_profile(request):
    if request.method == 'POST':
        
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('patient_home')
    form = EditProfileForm(instance=request.user)
    return render(request,'update_profile.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
      form = PasswordChangeForm(data=request.POST, user=request.user)
      if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        return redirect('patient_home')
      else:
          print(form.errors)
          return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,'change_password.html', {'form': form})
      