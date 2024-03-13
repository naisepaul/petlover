from django.urls import path
from . import views
# from .views import 

urlpatterns =[
    path('', views.index, name = 'home'),
    path('listings/', views.listings, name = 'listings'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login_account, name = 'login_account'),
    path('logout/', views.logoutconfirm, name = 'logoutconfirm'),     
    path('create-listings/', views.create_listings, name = 'create-listings'), 
    path('profile-page/', views.profile_page, name = 'profile-page'),   
    path('profile-update/', views.profile_update, name ='profile-update'),
   
]