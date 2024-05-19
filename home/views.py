from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Dog, Listing
from .forms import ProfileForm, DogListingForm, ListingForm
from . import choice

# Create your views here.

# Home page

def index(request):
    return render(request,'index.html')

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

        # Check if password meets length requirement
        if len(password) < 8:  
            messages.warning(request, "Password should be at least 8 characters long")
            return redirect('/signup')

        # Check if username meets length requirement
        if len(uname) < 5: 
            messages.warning(request, "Username should be at least 5 characters long")
            return redirect('/signup')

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

@login_required(login_url='login')
def profile_page(request):
    return render(request,'profile/profile_page.html')

@login_required(login_url='login')
def profile_update(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            
            # Check if username meets length requirement
            if len(username) < 5:
                messages.warning(request, "Username should be at least 5 characters long")
                return redirect('/profile-update')   
            
            form.save()
            messages.success(request,"Updated Successfully")
            return redirect('/profile-page')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'profile/profile_update.html', {'form': form})

def profile_delete(request):
    user = get_object_or_404(User, username=request.user.username)
    
    if request.method == 'POST':
        user.delete()
        return redirect('/')  # Redirect to home

    return render(request, 'profile/profile_delete.html')


# dog listing page

def listings(request):
    listings = Listing.objects.select_related('dog').order_by('-created_at').all()
    return render(request, 'listings/listings.html', {'listings': listings})

# single listing page

def single_listing(request, id):
    """ view single listings """
   
    listings = get_object_or_404(Listing, id=id)
    return render(request, 'listings/single_listing.html', {'listings': listings})


# create listings page

@login_required
def listing_form(request):
    if request.method == 'POST':
        dog_form = DogListingForm(request.POST, request.FILES)
        listing_form = ListingForm(request.POST)        
        if dog_form.is_valid() and listing_form.is_valid():
            dog = dog_form.save(commit=False)
            dog.owner = request.user
            dog.save()
            listing = listing_form.save(commit=False)
            listing.dog = dog
            listing.owner = request.user
            listing.save()
            messages.success(request, 'Your listing has been created!')
            return redirect('/') 
        else:            
            messages.error(request, 'Form validation failed. Please correct the errors.')    
    else:
        dog_form = DogListingForm()
        listing_form = ListingForm()
    return render(request, 'listings/listing_form.html', {'dog_form': dog_form, 'listing_form': listing_form})
    
@login_required
def my_listings(request):    
    user = request.user    
    user_dogs = user.dog_set.all()
    return render(request, 'listings/my_listings.html', {'user': user, 'user_dogs': user_dogs})
    



