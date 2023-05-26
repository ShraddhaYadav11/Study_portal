

from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *
from django.views import generic
from django.contrib.auth import login, logout, authenticate
import requests





# Create your views here.
def home(request):
    return render(request,'superuse/home.html')



def register(request):
    if request.method=='POST':
        form=UserRegistrationform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Account Created For {username} Successfully")
            return redirect("login")
    else:
        form=UserRegistrationform()
    context={
        'form':form
    }

    return render(request,'superuse/register.html',context)

