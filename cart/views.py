from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cart_detail(request):
    return HttpResponse('Cart Detail Page')
