from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'app1/dashboard.html')
def products(request):
    return render(request, 'app1/products.html')
def customer(request):
    return render(request, 'app1/customer.html') 
