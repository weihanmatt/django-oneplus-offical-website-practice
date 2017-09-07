from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator
from images.models import Pic
import os


def index(request):
	list = Pic.objects.all()
	context = {"piclist":list}
	return render(request,"images/index.html",context)
# Create your views here.

def addPic(request):
	return render(request,"images/addPic.html")

def insertPic(request):
    try:
    #执行图片的上传
        myfile = request.FILES.get("mypic", None)
        if not myfile:
            return HttpResponse("没有上传文件信息！")
        destination = open(os.path.join("./static/pic/",myfile.name),'wb+')
        for chunk in myfile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()

        #执行信息的添加
        ob = Pic()
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.picname = myfile.name
        ob.save()
        #os.rename(os.path.join("./static/pic/",myfile.name),os.path.join("./static/pic/",ob.name+myfile.name))
        context = {'info':'添加成功！'}
        return render(request,"images/info.html",context)
    except:
        context = {'info':'添加失败！'}
        return render(request,"images/info.html",context)

def delpic(request,uid):
	try:
		ob = Pic.objects.get(id=uid)
		ob.delete()
		picname = "./static/pic/" + ob.picname
		os.remove(picname)
		context = {'info':'DELETED SUCCESS'}
	except:
		context = {'info':'DELETED FAILED'}
	return render(request,"images/info.html",context)