from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.home_page, name='home'),
    path('contact_page/', views.contacts_page, name='contacts')
]
