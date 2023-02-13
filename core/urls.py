from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('contact_us', views.contact_us, name="contact_us"),
    path('user_approval', views.user_approval, name="user_approval"),
    path('book_appointment /<int:pk>/', views.book_appointment, name="book_appointment"),
    path('appointments', views.appointments, name="appointments"),
    path('schedule_appointment /<int:pk>/', views.schedule_appointment, name="schedule_appointment"),
    path('cards', views.cards, name="cards"),
    path('user_messages', views.user_messages, name="user_messages"),
    path('about_us', views.about_us, name="about_us"),

                            
]