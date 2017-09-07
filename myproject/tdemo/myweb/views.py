from django.shortcuts import render
import time

# Create your views here.
def index(request):
    return render(request,"myweb/index.html")
    

def tpl01(request):
    context= {
        "uname":"zhangsan",
        "a":[10,20,30],
        "value":time.time()
      }
    return render(request,"myweb/tpl01.html",context)

def opIndex(request):
	return render(request,"oneplus/index.html")