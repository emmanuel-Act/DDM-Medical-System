from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('', views.index, name='index'),
   path('admin_login', views.admin_login_page, name='admin_login'),
   path('doctor_login', views.doctor_login_page, name='doctor_login'),
   path('patient_login', views.patient_login_page, name='patient_login'),
   path('user_logout', views.user_logout, name='user_logout'),
   path('register', views.register, name='register'), 
   path('admin_home', views.admin, name='admin_home'),
   path('doctor_home', views.doctor, name='doctor_home'),
   path('patient_home', views.patient, name='patient_home'),
   path('update_profile', views.update_profile, name='update_profile'),
   path('change_password', views.change_password, name='change_password'),

   # path('password_reset', views.password_reset, name="password_reset"),
   # # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_confirm"),
   # path('reset/<uidb64>/<token>/', views.passwordResetConfirm, name="password_reset_confirm"),
   # # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view()),
   
]
