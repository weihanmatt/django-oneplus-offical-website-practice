# -*- coding: utf-8 -*-
# 
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from myweb.models import Pic

import time,os

# 浏览相册图片信息信息        
def indexpic(request):
    # 执行数据查询，并放置到模板中
    list = Pic.objects.all()
    context = {"stulist":list}
    return render(request,"myweb/pic/index.html",context)

# 加载添加信息表单
def addpic(request):  
    return render(request,"myweb/pic/add.html")

# 执行信息添加操作
def insertpic(request): 
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
        ob.addtime= time.time()
        ob.save()
        #os.rename(os.path.join("./static/pic/",myfile.name),os.path.join("./static/pic/",ob.name+myfile.name))
        context = {'info':'添加成功！'}
        return render(request,"myweb/pic/info.html",context)
    except:
        context = {'info':'添加失败！'}
        return render(request,"myweb/pic/info.html",context)

# 执行信息删除操作    
def delpic(request,uid):  
    try:
        ob = Pic.objects.get(id=uid)
        ob.delete()
        picname = './static/pic/' + ob.picname
        os.remove(picname)
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myweb/pic/info.html",context)

# 加载信息编辑表单    
def editpic(request,uid):  
    try:
        ob = Pic.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"myweb/pic/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
        return render(request,"myweb/pic/info.html",context)

# 执行信息编辑操作
def updatepic(request):
    try:
        ob = Pic.objects.get(id= request.POST['id'])
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myweb/pic/info.html",context)
    