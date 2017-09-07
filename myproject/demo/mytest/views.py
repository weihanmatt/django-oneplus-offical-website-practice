from django.shortcuts import render
from django.http import HttpResponse

from mytest.models import Users
import os

def index(request):
    try:
        list = Users.objects.filter(id__in=[1,3,5])
        s = ','.join([vo.name for vo in list])
        
        #修改(将id值为5的age值改为30)
        #ob = Users.objects.get(id=5)
        #ob.age = 30
        #ob.save()

        #删除(删除id为3的信息)	
        #ob = Users.objects.get(id=3)
        #ob.delete()
        
        return HttpResponse(s)
    except:
        return HttpResponse("没有找到对应的信息！")

# 浏览用户信息        
def indexUsers(request):
    # 执行数据查询，并放置到模板中
    list = Users.objects.all()
    context = {"stulist":list}
    return render(request,"mytest/users/index.html",context)

# 加载添加信息表单
def addUsers(request):  
    return render(request,"mytest/users/add.html")

# 执行信息添加操作
def insertUsers(request): 
    try:
        ob = Users()
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}
    return render(request,"mytest/users/info.html",context)

# 执行信息删除操作    
def delUsers(request,uid):  
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"mytest/users/info.html",context)

# 加载信息编辑表单    
def editUsers(request,uid):
    ob = Users.objects.get(id=uid)
    context = {"ob":ob}
    return render(request,"mytest/users/edit.html",context)

# 执行信息编辑操作
def updateUsers(request,uid):  
    try:
        ob = Users.objects.get(id=uid)
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()
        context={'info':'success'}
    except:
        context={'info':'failed'}
    return render(request,"mytest/users/info.html",context)

def upload(request):
    return render(request,"mytest/users/file.html")

def addfile(request):
    if request.method=="POST":
        myfile = request.FILES.get("file", None)
        if not myfile:
            return HttpResponse("没有上传文件信息！")
        destination = open(os.path.join("./uploads/",myfile.name),'wb+')
        for chunk in myfile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()
    return HttpResponse('文件上传成功')

    
    
    
    