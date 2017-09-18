from django.shortcuts import render
from myadmin.models import Users
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from myadmin.models import Users
from django.http import HttpResponse,JsonResponse
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
		# print(request.session.verifycode,request.POST['code'])
		#判断当前用户是否是后台管理员用户
		if loginuser.status == 0:
			#验证密码
			m = hashlib.md5() 
			m.update(bytes(request.POST['password'],encoding="utf8"))
			if loginuser.password == m.hexdigest():	
				if request.POST['code'] == request.session['verifycode']:

					# 此处登录成功，将当前登录信息放入到session中，并跳转页面
					request.session['adminuser'] = loginuser.name
					#print(json.dumps(user))
					return redirect(reverse('myadmin_index'))
				else:
					context = {'info':'验证码错误!'}
			else:
				context = {'info':'登录密码错误！'}
		else:
			context = {'info':'此用户非后台管理用户！'}
	except:
	   	context = {'info':'登录账号错误！'}
	return render(request,"myadmin/login.html",context)

#退出登录
def logout(request):
    # 清除登录的session信息
    del request.session['adminuser']
    # 跳转登录页面
    return redirect(reverse('myadmin_login'))

#验证码
def verifycode(request):
	#引入随机函数模块
	import random
	from PIL import Image, ImageDraw, ImageFont
	#定义变量，用于画面的背景色、宽、高
	#bgcolor = (random.randrange(20, 100), random.randrange(
	#    20, 100),100)
	bgcolor = (255,218,191)
	width = 90
	height = 28
	#创建画面对象
	im = Image.new('RGB', (width, height), bgcolor)
	#创建画笔对象
	draw = ImageDraw.Draw(im)
	#调用画笔的point()函数绘制噪点
	for i in range(0, 100):
		xy = (random.randrange(0, width), random.randrange(0, height))
		fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
		draw.point(xy, fill=fill)
	#定义验证码的备选值
	str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
	#随机选取4个值作为验证码
	rand_str = ''
	for i in range(0, 4):
		rand_str += str1[random.randrange(0, len(str1))]
	#构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
	font = ImageFont.truetype('STXIHEI.TTF', 21)
	#font = ImageFont.load_default().font
	#构造字体颜色
	fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
	#绘制4个字
	draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
	draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
	draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
	draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
	#释放画笔
	del draw
	#存入session，用于做进一步验证
	request.session['verifycode'] = rand_str
	# print(rand_str)
	# 内存文件操作-->此方法为python3的
	import io
	buf = io.BytesIO()
	#将图片保存在内存中，文件类型为png
	im.save(buf, 'png')
	#将内存中的图片数据返回给客户端，MIME类型为图片png
	return HttpResponse(buf.getvalue(), 'image/png')




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
	# try:
	ob = Users.objects.get(id= uid)
	ob.username = request.POST['username']
	ob.name = request.POST['name']
	ob.password = request.POST['password']
	ob.sex = request.POST['sex']
	ob.code = request.POST['code']
	ob.phone = request.POST['phone']
	ob.email = request.POST['email']
	ob.status = request.POST['status']
	ob.save()
	context = {'info':'修改成功！'}
	# except:
	#     context = {'info':'修改失败！'}
	return render(request,"myadmin/info.html",context)


#加载编辑用户信息
def edituser(request,uid):
	ob = Users.objects.get(id=uid)
	context = {'user':ob}
	return render(request,"myadmin/edituser.html",context)


#浏览商品
def browsegoods(request,pIndex):
	list = Users.objects.all()
	p = Paginator(list,5)
	# 处理当前页号信息
	if pIndex=="":
		pIndex = '1'
	pIndex = int(pIndex)
	# 获取当前页数据
	list2 = p.page(pIndex)
	plist = p.page_range
	return render(request,"myadmin/browsegoods.html",{'userlist':list2,'pIndex':pIndex,'plist':plist})

















