from django.shortcuts import render,redirect
from .models import *
from .forms import Registerform, Loginform
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.
def home(request):
    data=HomeInteriors.objects.all()
    return render(request,'home.html',{'data':data})
def reg(request):
    form=Registerform()
    if request.method=='POST':
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
            
        else:
            return render(request,'Registration.html',{'form':form})
    form=Registerform()
    return render(request,'Registration.html',{'form':form})
def login(request):
    form = Loginform()
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                print('y')
                auth_login(request, user)
                return redirect('app:home')  # ✅ Redirect to home page
            else:
                print('n')
                return render(request, 'login.html', {'form': form})  # ✅ Render template instead of redirect

    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/login/')
def business(request):
    data=Business.objects.all()
    return render(request,'business.html',{'data':data})
from django.shortcuts import render, redirect
from .forms import ContactForm

def submit_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, "contactus.html", {"form": form})
def get(request):
    data=HomeInteriors.objects.all()
    return render(request,'get.html',{'data':data})
