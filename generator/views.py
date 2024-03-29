from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    returnedpassword=''

    characters=list('abcdefghijklmnopqrstuvwwxyz')

    length=int(request.GET.get('length', 10))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+')

    for x in range(length):
        returnedpassword+=random.choice(characters)
    return render(request, 'generator/password.html', {'password':returnedpassword})