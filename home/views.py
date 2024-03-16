from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from .models import *

def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'scan'
  }
  return render(request, "pages/dynamic-tables.html", context)
@login_required(login_url='login')
def scan(request):
    if request.method == "POST":
        url = request.POST.get('url')  # Corrected the method to request.POST
        print(url)  # Print the URL to console (optional)
        # Do something with the URL, such as scanning it
    return render(request, "pages/sample-page.html")

import json
from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required

@login_required
def sub_scan(request):

    return render(request, "pages/sub_scan.html")
