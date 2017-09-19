from django.shortcuts import render
from myadmin.models import Users
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse
from myadmin.models import Goods,Types,Order,Detail
import time
import hashlib


# 自定义公共信息加载函数
def loadContext(request):
	context={}
	context['typelist'] = Types.objects.filter(pid=0)
	return context

# 自定义公共登录信息
def loadlogin(request):
	if "mywebuser" in request.session:
		context = {'vip':request.session['mywebuser'],'haha':'退出','dbc':request.session['webuserid']}
		
	else:
		context = {'vip':'请登录'}
	return context

#主页路由
def index(request):
	context = loadlogin(request)
	return render(request,"myweb/index.html",context)


#商品列表页
def mall(request):
	context = loadlogin(request)
	return render(request,"myweb/oneplus-mall.html",context)

def list(request,tid):
	context = loadlogin(request)
	context['goodslist'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(id=tid)).exclude(status=3)
	return render(request,"myweb/list.html",context)

#商品详情页
def oneplus5(request):
	context = loadlogin(request)
	return render(request,"myweb/oneplus-main.html",context)

#商品详情页2
def details(request,gid):
	context = loadContext(request)
	context['goods'] = Goods.objects.get(id=gid)
	ob = Goods.objects.get(id=gid)
	ob.clicknum += 1
	ob.save()
	return render(request,"myweb/details.html",context)


#会员登录页
def login(request):
	context = loadlogin(request)
	return render(request,"myweb/login.html",context)

#登录提交
def dologin(request):
	try:
		#根据账号获取登录者信息
		loginuser = Users.objects.get(username=request.POST['username'])
		# print(request.session.verifycode,request.POST['code'])
		#判断当前用户是否是后台管理员用户
			#验证密码
		m = hashlib.md5() 
		m.update(bytes(request.POST['password'],encoding="utf8"))
		if loginuser.password == m.hexdigest():	
			if request.POST['code2'] == request.session['myweb_verifycode']:

				# 此处登录成功，将当前登录信息放入到session中，并跳转页面
				request.session['mywebuser'] = loginuser.username
				request.session['webuserid'] = loginuser.id
				request.session['webuseraddress'] = loginuser.address
				request.session['webusername'] = loginuser.name
				request.session['webuserphone'] = loginuser.phone
				request.session['webusercode'] = loginuser.code
				#print(json.dumps(user))
				return redirect(reverse('index'))
			else:
				context = {'info':'验证码错误!'}
		else:
			context = {'info':'登录密码错误！'}
	except:
		context = {'info':'登录账号错误！'}
	return render(request,"myweb/login.html",context)

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
	request.session['myweb_verifycode'] = rand_str
	# print(rand_str)
	# 内存文件操作-->此方法为python3的
	import io
	buf = io.BytesIO()
	#将图片保存在内存中，文件类型为png
	im.save(buf, 'png')
	#将内存中的图片数据返回给客户端，MIME类型为图片png
	return HttpResponse(buf.getvalue(), 'image/png')

#会员退出
def logout(request):
    # 清除登录的session信息
    del request.session['mywebuser']
    del request.session['webuserid']
    del request.session['webuseraddress']
    del request.session['webusername']
    del request.session['webuserphone']
    del request.session['webusercode']
    request.session['shoplist'] = {}
    # 跳转登录页面
    return redirect(reverse('login'))

# 详情页
def detail(request,gid):
    context = loadContext(request)
    # 获取对应商品详情信息并放置到context
    ob = Goods.objects.get(id=gid)
    ob.clicknum += 1
    ob.save()
    context['goods'] = ob
    return render(request,'myweb/detail.html',context)

#会员注册页
def register(request):
	return render(request,"myweb/register.html")

#添加会员
def registuser(request): 
	# return HttpResponse(request.POST['password'])
	userlist = Users.objects.all()
	for u in userlist:
		if request.POST['username'] == u.username:
			context = {'info':'用户名已存在'}
			return render(request,"myweb/register.html",context)

	if request.POST['password'] == request.POST['password2'] and request.POST['password'] != '':
		ob = Users()
		ob.username = request.POST['username']

		# ob.name = request.POST['name']
		#获取密码并md5
		m = hashlib.md5() 
		m.update(bytes(request.POST['password'],encoding="utf8"))
		ob.password = m.hexdigest()
		# ob.sex = request.POST['sex']
		# ob.code = request.POST['code']
		# ob.phone = request.POST['phone']
		# ob.email = request.POST['email']
		# ob.status = request.POST['status']
		# ob.addtime = time.time()
		ob.save()
		context = {'info':'注册成功！'}
		return render(request,"myweb/info.html",context)
	else:
		context = {'info':'两次密码不一致'}
		return render(request,"myweb/register.html",context)


#个人中心页面
def personal(request,uid):
	if uid != '':
		ob = Users.objects.get(id=uid)
		context = {'user':ob}
		return render(request,"myweb/personal1.html",context)
	else:
		return render(request,"myweb/login.html")

def personalupdate(request,uid):
	# try:
	ob = Users.objects.get(id= uid)
	# ob.username = request.POST['username']
	ob.name = request.POST['name']
	ob.address = request.POST['address']
	ob.sex = request.POST['sex']
	ob.code = request.POST['code']
	ob.phone = request.POST['phone']
	ob.email = request.POST['email']
	ob.save()
	context = {'info':'修改成功！'}
	# except:
	#     context = {'info':'修改失败！'}
	return render(request,"myweb/info.html",context)

def myorders(request,uid):
	context = {}
	order = Order.objects.filter(uid=uid)
	context['orderlist']=order
	return render(request,"myweb/myorders.html",context)

#确认收货
def got(request,oid):
	ob = Order.objects.get(id = oid)
	ob.status = 2
	ob.save()
	iidd = request.session['webuserid']

	return redirect(reverse('myorders' ,args=[iidd]))




def orderdetail(request,uid):
	# try:
	# 获取要编辑的信息
	context = {}
	ob = Order.objects.get(id=uid)
	dt = Detail.objects.filter(orderid = uid)
		
	# 获取商品的类别信息
	# list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	# 放置信息加载模板
	# context = {'orders':ob}
	# context = {}
	# context= {'detail':dt}
	return render(request,"myweb/orderdetail.html",{'orders':ob,'detail':dt})

def safe(request):
	
	return render(request,"myweb/safe.html")

def changepassword(request):
	m = hashlib.md5() 
	m.update(bytes(request.POST['oldpassword'],encoding="utf8"))
	ob = Users.objects.get(id=request.session['webuserid'])
	if ob.password == m.hexdigest():
		if request.POST['newpassword1'] == request.POST['newpassword2'] and request.POST['newpassword1'] != '':
			p = hashlib.md5() 
			p.update(bytes(request.POST['newpassword1'],encoding="utf8"))
			ob.password = p.hexdigest()
			ob.save()
			context = {'info':'密码修改成功'}
			return render(request,"myweb/safe.html",context)	
		else:
			context = {'info':'两次密码不一致'}
			return render(request,"myweb/safe.html",context)
	else:
		context = {'info':'原始密码错误'}
		return render(request,"myweb/safe.html",context)	


