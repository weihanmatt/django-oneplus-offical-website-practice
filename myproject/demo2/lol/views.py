from django.shortcuts import render
from django.http import HttpResponse
from lol.models import leesin

def index(request):

	a = leesin.objects.get(id=1)
	return HttpResponse(a.name)

def indexUsers(request):
	list = leesin.objects.all()
	context = {'leelist':list}
	return render(request,'lol/leesin/index.html',context)

def addUsers(request):
	return render(request,"lol/leesin/add.html")

def insertUsers(request):
	try:
		ob = leesin()
		ob.name = request.POST['name']
		ob.age = request.POST['age']
		ob.phone = request.POST['phone']
		ob.save()
		context={'info':'added success'}
	except:
		context={'info':'added failed'}
	return render(request,'lol/leesin/info.html',context)

def delUsers(request):
	pass

def editUsers(request):
	pass

def updateUsers(request):
	pass
