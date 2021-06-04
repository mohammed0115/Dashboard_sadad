from django.shortcuts import render

from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from request import SendRequest
def my_login_required(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if not (user.id and request.session.get('code_success')):
            return HttpResponseRedirect('/login/')
        
        return HttpResponseRedirect('')
    return wrapper

# @login_required(login_url='/login/')
# @my_login_required
def index(request):
    return render(request, "index.html")


@login_required
def special(request):
    return HttpResponse("You are logged in !")

def NotFound(request):
    return render(request,"error-404.html",{})
def ServerDown(request):
    return render(request,"error-500.html",{})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



def user_login(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        Body={
            "mobile_number": phone,
            "password": password
        }
        Header={"content-type":"application/json","API-KEY":"b46dc969-f675-4800-9579-631066bc9eed"}
        requ=SendRequest("http://45.77.252.45/accounts/login/", Header,Body)
        response=requ.POST_Send()
        # user = authenticate(username=username, password=password)
        if response.status_code==200:
            print("success access server")
            data=response.json()
            request.session=data['user']
            if data["responseCode"]==0:
                print("welcome")
                return HttpResponseRedirect(reverse("index"))
            else:
                print("sorry   ",data)
                return render(request, "error-login.html", {})

        elif response.status_code==500:
            return HttpResponseRedirect(reverse("error-500"))
        elif response.status_code==404:
            return HttpResponseRedirect(reverse("error-404"))  
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, "login.html", {})