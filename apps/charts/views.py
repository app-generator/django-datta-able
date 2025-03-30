from django.shortcuts import render
from django.core import serializers
from apps.pages.models import *

# Create your views here.

def index(request):
  products = serializers.serialize('json', Product.objects.all())
  context = {
    'segment': 'charts',
    'products': products
  }
  return render(request, 'charts/index.html', context)
