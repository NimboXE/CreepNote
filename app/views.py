from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from app.models import *

# Create your views here.
def index(request):

    ## Login request ##
    if request.method == "POST":

        ## Post Get's ##
        username = request.POST.get("username")
        password = request.POST.get("password")

        ## Login ##
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)

            return redirect(home)

    return render(request, 'index.html')

def signupPage(request):

    ## Signup request ##
    if request.method == "POST":

        ## Post Get's ##
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        birthdate = request.POST.get("birthdate")

        ## SignUp ##
        CNUser.createNewUser(username, birthdate, email, password)

        ## Returning to LoginPage(index) ##
        return redirect(index)

    return render(request, 'signupPage.html')

@login_required(login_url=index)
def home(request):
    return render(request, 'home.html')