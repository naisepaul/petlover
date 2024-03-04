from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name = 'home'),
    path('listings/', views.listings, name = 'listings'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login_account, name = 'login_account'),
    path('logout/', views.logoutconfirm, name = 'logoutconfirm'),
    
]