from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login_view(request):
    return HttpResponse('Login Page')

def signup_view(request):
    return HttpResponse('Signup Page')

def profile_view(request):
    return HttpResponse('User Profile Page')
