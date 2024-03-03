from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages

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
            messages.warning(request,"Password Incorrect")
            return redirect('/signup')
        try: 
            if User.objects.get(username = uname):
                messages.info(request,"Username is taken")
                return redirect('/signup')                
        except:
            pass        
        try: 
            if User.objects.get(email = email):
                messages.info(request,"Email is taken")
                return redirect('/signup')                
        except:
            pass
        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        messages.info(request,"Sign Up Success")
        return redirect('/login') 
    return render(request,'account/signup.html')
    
def login(request):
    return render(request,'account/login.html')