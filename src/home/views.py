from django.shortcuts import render

# Create your views here.
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