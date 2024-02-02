from django.urls import path
from .views import *
urlpatterns = [
    path('facebook/login', facebookLogin , name='fbLogin'),
    path('facebook/home', facebookHome, name= 'fbHome')
]
