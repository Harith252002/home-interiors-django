from django.contrib import admin
from django.urls import path
from .views import *
app_name='category'
urlpatterns = [
    path('cateogries/<int:id>/',cateogries,name='cateogries'),
    path('cateogries_details/<int:id>/',cateogries_details,name='cateogries_details'),
    path('contactus/',contactus,name='contactus'),
    path('business_cateogries/<int:id>/',business_cateogries,name='business_cateogries'),
    path('business_cateogriesdetails/<int:id>/',businesscateogries_details,name='businesscateogries_details'),
    path('search/', search_and_redirect, name='search_redirect'),  
]
