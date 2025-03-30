from django.shortcuts import render
from apps.pages.models import Product
from django.core import serializers

from .models import *

def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)


def charts(request):
  products = serializers.serialize('json', Product.objects.all())
  context = {
    'segment': 'charts',
    'products': products
  }
  return render(request, 'pages/charts.html', context)