from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def product_list(request):
    return HttpResponse('Product List Page')

def product_detail(request, pk):
    return HttpResponse(f'Product Detail Page for product {pk}')
