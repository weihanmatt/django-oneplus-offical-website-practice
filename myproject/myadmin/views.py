from django.shortcuts import render
from myadmin.models import Users
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from myadmin.models import Users
import time
import hashlib

#后台首页
def index(request):
	return render(request,"myadmin/index.html")

#会员登录
def login(request):
	return render(request,"myadmin/login.html")

def dologin(request):
	try:
		#根据账号获取登录者信息
		loginuser = Users.objects.get(username=request.POST['username'])
		print(loginuser.name, request.POST['password'],loginuser.password)
		#判断当前用户是否是后台管理员用户
		if loginuser.status == 0:
			#验证密码
			m = hashlib.md5() 
			m.update(bytes(request.POST['password'],encoding="utf8"))
			if loginuser.password == m.hexdigest():	
				# 此处登录成功，将当前登录信息放入到session中，并跳转页面
				request.session['adminuser'] = loginuser.name
				#print(json.dumps(user))
				return redirect(reverse('myadmin_index'))
			else:
				context = {'info':'登录密码错误！'}
		else:
			context = {'info':'此用户非后台管理用户！'}
	except:
	   	context = {'info':'登录账号错误！'}
	return render(request,"myadmin/login.html",context)

def logout(request):
    # 清除登录的session信息
    del request.session['adminuser']
    # 跳转登录页面
    return redirect(reverse('myadmin_login'))




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
		#获取密码并md5
		m = hashlib.md5() 
		m.update(bytes(request.POST['password'],encoding="utf8"))
		ob.password = m.hexdigest()
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
















