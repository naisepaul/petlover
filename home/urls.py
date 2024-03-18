from django.urls import path
from . import views
# from .views import 

urlpatterns =[
    path('', views.index, name = 'home'),    
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login_account, name = 'login_account'),
    path('logout/', views.logoutconfirm, name = 'logoutconfirm'),     
    path('profile-page/', views.profile_page, name = 'profile-page'),   
    path('profile-update/', views.profile_update, name ='profile-update'),
    path('profile-delete/', views.profile_delete, name = 'profile-delete'),
    path('listings/listing-form/',views.listing_form, name = 'listing-form'),
    path('listings/listings/',views.listings, name = 'listings'),
    path('listings/my-listings/',views.my_listings, name = 'my-listings'),
]