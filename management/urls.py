from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('contacts/', contacts, name='contacts'),
    path('about/',about,name='about')
]