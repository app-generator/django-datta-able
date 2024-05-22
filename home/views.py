from admin_datta.forms import (
  LoginForm,
  RegistrationForm,
  UserPasswordChangeForm,
  UserPasswordResetForm,
  UserSetPasswordForm,
)
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
  LoginView,
  PasswordChangeView,
  PasswordResetConfirmView,
  PasswordResetView,
)
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .models import *

from django.views.generic import CreateView

from .models import *


def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)
