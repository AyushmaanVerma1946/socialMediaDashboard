from django.urls import path
from .views import *
urlpatterns = [
    path('', userLogin, name='login'),
    path('register', userRegister, name= 'register'),
    path('home', home, name= 'home'),
    path('logout', userLogout, name='logout'),
    path('profile', userProfile, name='profile'),
]

