from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
# from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def listings(request):
    return render(request,'listings.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('fname')   
        uname = request.POST.get('username')      
        email = request.POST.get('email')        
        password = request.POST.get('password1')
        confirmpassword = request.POST.get('password2')
        if password != confirmpassword:
            return HttpResponse("Password Incorrect")
        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        return HttpResponse("Signup Succesfull")
    return render(request,'account/signup.html')
    
def login(request):
    return render(request,'account/login.html')