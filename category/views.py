from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def cateogries(request,id):
    data=Cateogries.objects.filter(category_id=id)
    data1=HomeInteriors.objects.all()
    return render(request,'cateogries.html',{'data':data,'data1':data1})
def cateogries_details(request,id):
    data=Cateogries.objects.get(id=id)
    data1=HomeInteriors.objects.all()
    return render(request,'cateogriesdetail.html',{'data':data,'data1':data1})
def contactus(request):
    return render(request,'contactus.html')
def business_cateogries(request,id):
    data=Business_Cateogries.objects.filter(category_id=id)
    data1=Business.objects.all()
    return render(request,'business_cateogries.html',{'data':data,'data1':data1})
def businesscateogries_details(request,id):
    data=Business_Cateogries.objects.get(id=id)
    data1=Business.objects.all()
    return render(request,'businesscateogries_details.html',{'data':data,'data1':data1})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cateogries, Business_Cateogries
from app.models import HomeInteriors

def search_and_redirect(request):
    query = request.GET.get("q", "").strip()

    if query:
        # Check if it's a main category (e.g., "Kitchen")
        main_category = HomeInteriors.objects.filter(category_name__icontains=query).first()
        
        # Check if it's a specific model (e.g., "U-Shape Kitchen")
        specific_category = Cateogries.objects.filter(name__icontains=query).first()

        if main_category:
            return redirect('category:cateogries', id=main_category.id)  # Redirect to cateogries.html
        
        if specific_category:
            return redirect('category:cateogries_details', id=specific_category.id)  # Redirect to cateogriesdetail.html

    return redirect('app:home')  # If nothing found, go back to home
