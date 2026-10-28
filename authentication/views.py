from django.http import HttpResponse
from django.shortcuts import render

def signup(request):
    return render(request, "registration/signup.html")

def login_view(request):
    return render(request, "registration/login.html")

def logout_view(request):
    return redirect("login")

def profile(request):
    return HttpResponse("Your profile page - coming soon")

def delete_profile(request):
    return redirect("login")