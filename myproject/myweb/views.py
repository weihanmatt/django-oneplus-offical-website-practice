from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"myweb/index.html")

def mall(request):
	return render(request,"myweb/oneplus-mall.html")

def oneplus5(request):
	return render(request,"myweb/oneplus-main.html")

def login(request):
	return render(request,"myweb/login.html")

def register(request):
	return render(request,"myweb/register.html")