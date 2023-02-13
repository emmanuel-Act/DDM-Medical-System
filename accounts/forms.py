from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    age = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "number"
            }
        )
    )

    

    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'id', 'password1', 'password2', 'profile_pic', 'credentials_img', 'approved', 'is_admin', 'is_doctor', 'is_patient')

class EditProfileForm(UserChangeForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'profile_pic')

