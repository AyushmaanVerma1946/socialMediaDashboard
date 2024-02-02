from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .forms import *


def userRegister(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = registerForm()
        return render(request, "userRegister.html", {"form": form})


def userLogin(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user=user)
                return redirect("profile")
            else:
                return HttpResponse(404)
        else:
            print("check for errors")
            return forms.ValidationError(form.errors)
    else:
        form = loginForm()
        return render(request, "userLogin.html", {"form": form})


def userLogout(request):
    logout(request)
    return redirect("login")


def home(request):
    return render(request, "home.html")


def userProfile(request):
    pk = request.user.id
    if pk:
        obj = User.objects.get(id=pk)
        return render(request, "userProfile.html", {"form": obj})
    else:
        print("nope")


