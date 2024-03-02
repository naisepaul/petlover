from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def listings(request):
    return render(request,'listings.html')

def signup(request):
    return render(request,'account/signup.html')
    
def login(request):
    return render(request,'account/login.html')