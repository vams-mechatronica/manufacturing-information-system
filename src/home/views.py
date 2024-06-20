from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def master(request):
    return render(request,'master.html')

def maintenance(request):
    return render(request,'maintenance.html')

def reports(request):
    return render(request,'reports.html')

def amc_page(request):
    return render(request,'amc.html')

def loginRequest(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Login failed")
            return redirect('login') 
    return render(request, 'accounts/login.html')

def logoutRequest(request):
    logout(request)
    return redirect("login")