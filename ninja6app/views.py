from django.shortcuts import render
from . models import Quotetion

# Create your views here.

def home(request):
    quote = Quotetion.objects.all()
    return render(request, 'ninja6app/home.html', {'quote': quote})


def base(request):
    return render(request, 'base.html')

def navbar(request):
    return render(request, 'ninja6app/navbar.html')