from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from .forms import ProfileForm
# from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.

# Home page

def index(request):
    return render(request,'index.html')

# dog listing page

def listings(request):
    return render(request,'listings.html')

# create listings page

def create_listings(request):
    return render(request,'create_listings.html')

# user login page

def login_account(request):
    if request.method == "POST":
        uname = request.POST.get('username')             
        pass1 = request.POST.get('password1')
        myuser= authenticate(username=uname, password=pass1)
        if myuser is not None:               
            login(request, myuser)                      
            messages.success(request,"Login Success")                
            return redirect('/')                        
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect('/login')
    else:    
        return render(request,'account/login.html')

# New user signup page

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
        messages.info(request,"Sign Up Success. Now you can Login")
        return redirect('/login') 
    return render(request,'account/signup.html')   

# user logout page

def logoutconfirm(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request,"Successfully Logout")
        return redirect('/')
    return render(request, 'account/logout.html')

# user profile page

@login_required
def profile_page(request):
    # u_form = UserUpdateForm()
    # p_form = ProfileUpdateForm()

    # context = {
    #     'u_form' : u_form,
    #     'p_form' : p_form
    # }
    return render(request,'profile/profile_page.html')

def profile_update(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Successfully")
            return redirect('/profile-page')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'profile/profile_update.html', {'form': form})
