from django.shortcuts import render
from myadmin.models import Users
from django.core.paginator import Paginator
import time

#index路由
def index(request):
	return render(request,"myadmin/index.html")

#添加用户路由
def adduser(request):
	return render(request,"myadmin/adduser.html")

#浏览用户路由
def browseuser(request,pIndex):
	list = Users.objects.all()
	p = Paginator(list,5)
	# 处理当前页号信息
	if pIndex=="":
		pIndex = '1'
	pIndex = int(pIndex)
	# 获取当前页数据
	list2 = p.page(pIndex)
	plist = p.page_range
	return render(request,"myadmin/browseuser.html",{'userlist':list2,'pIndex':pIndex,'plist':plist})

#添加用户
def insertuser(request): 
	try:
		ob = Users()
		ob.username = request.POST['username']
		ob.name = request.POST['name']
		ob.password = request.POST['password']
		ob.sex = request.POST['sex']
		ob.code = request.POST['code']
		ob.phone = request.POST['phone']
		ob.email = request.POST['email']
		ob.status = request.POST['status']
		ob.addtime = time.time()
		ob.save()
		context = {'info':'添加成功！'}
	except:
	    context = {'info':'添加失败！'}
	return render(request,"myadmin/info.html",context)

#删除用户
def deleteuser(request,uid):
	try:
		ob = Users.objects.get(id=uid)
		ob.delete()
		context = {'info':'删除成功！'}
	except:
	    context = {'info':'删除失败！'}
	return render(request,"myadmin/info.html",context)

# 执行信息编辑操作
def updateuser(request,uid):
	try:
		ob = Users.objects.get(id= uid)
		ob.username = request.POST['username']
		ob.name = request.POST['name']
		ob.password = request.POST['password']
		ob.sex = request.POST['sex']
		ob.code = request.POST['code']
		ob.phone = request.POST['phone']
		ob.email = request.POST['email']
		ob.status = request.POST['status']
		ob.addtime = request.POST['addtime']
		ob.save()
		context = {'info':'修改成功！'}
	except:
	    context = {'info':'修改失败！'}
	return render(request,"myadmin/info.html",context)


#加载编辑用户信息
def edituser(request,uid):
	ob = Users.objects.get(id=uid)
	context = {'user':ob}
	return render(request,"myadmin/edituser.html",context)
















