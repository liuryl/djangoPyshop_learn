from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.

# /poducts->index
# uniform Rescource Locator (address)
'''根据html添加内容'''
def index(request):
    products = Product.objects.all()
    return render(request,'index.html',
                  {'products':products})



def new(request):
    return HttpResponse('New products')