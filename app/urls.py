from django.urls import path
from .views import *

app_name = 'app' 

urlpatterns = [
    path('', home, name='home'),
    path('register/', reg, name='register'),
    path('login/', login, name='login'), 
    path('logout/', logout, name='logout'),
    path('business/',business,name='business'),
    path('contact/', submit_contact, name='submit_contact'),
    path('get/',get,name='get'),
]

