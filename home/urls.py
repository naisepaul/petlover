from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name = 'home'),
    path('listings/', views.listings, name = 'listings'),
    path('signup/', views.signup, name = 'signup'),
    
]