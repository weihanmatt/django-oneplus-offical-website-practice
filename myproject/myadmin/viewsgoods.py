from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Users
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from myadmin.models import Goods,Types
from PIL import Image
import time
import os

#浏览商品
def browsegoods(request,pIndex):
	list = Goods.objects.all()
	p = Paginator(list,5)
	# 处理当前页号信息
	if pIndex=="":
		pIndex = '1'
	pIndex = int(pIndex)
	# 获取当前页数据
	list2 = p.page(pIndex)
	for i in list2:
		ob = Types.objects.get(id=i.typeid)
		i.typename = ob.name
	plist = p.page_range
	return render(request,"myadmin/browsegoods.html",{'goodslist':list2,'pIndex':pIndex,'plist':plist})


#添加商品路由
def addgoods(request):
	list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	context = {"typelist":list}
	return render(request,"myadmin/addgoods.html",context)

#添加商品
def insertgoods(request): 
	try:
		#判断执行图片上传
		myfile = request.FILES.get('picname',None)
		if not myfile:
			return HttpResponse('没有上传图片信息')
		#时间戳命名图片
		filename = str(time.time())+'.'+myfile.name.split('.').pop()
		destination = open(os.path.join('./static/goods/',filename),'wb+')
		for chunk in myfile.chunks():
			destination.write(chunk)
		destination.close()
		#图片缩放
		im = Image.open('./static/goods/'+filename)

		im.thumbnail((375,375))

		im.save('./static/goods/'+filename,'jpeg')

		im.thumbnail((220,220))

		im.save('./static/goods/m_'+filename,'jpeg')

		im.thumbnail((100,100))

		im.save('./static/goods/s_'+filename,'jpeg')

		ob = Goods()
		ob.typeid = request.POST['typeid']
		ob.goods = request.POST['goods']
		ob.company = request.POST['company']
		ob.price = request.POST['price']
		ob.picname = filename
		ob.num = request.POST['num']
		ob.clicknum = request.POST['clicknum']
		ob.descr = request.POST['descr']
		ob.store = request.POST['store']
		ob.status = request.POST['status']
		ob.addtime = time.time()
		ob.save()
		context = {'info':'添加成功！'}
	except:
	    context = {'info':'添加失败！'}
	return render(request,"myadmin/info.html",context)

#删除商品
def deletegoods(request,uid):
	try:
		# 获取被删除商品信的息量，先删除对应的图片
		ob = Goods.objects.get(id=uid)
		#执行图片删除
		os.remove("./static/goods/"+ob.picname)   
		os.remove("./static/goods/m_"+ob.picname)   
		os.remove("./static/goods/s_"+ob.picname)
		#执行商品信息的删除 
		ob.delete()
		context = {'info':'删除成功！'}
	except:
		context = {'info':'删除失败！'}
	return render(request,"myadmin/info.html",context)

#加载编辑商品信息
def editgoods(request,uid):
	# try:
	# 获取要编辑的信息
	ob = Goods.objects.get(id=uid)
	# 获取商品的类别信息
	list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	# 放置信息加载模板
	context = {"typelist":list,'goods':ob}
	return render(request,"myadmin/editgoods.html",context)
	# except:
	# 	context = {'info':'没有找到要修改的信息！'}
	# return render(request,"myadmin/info.html",context)

# 执行商品编辑操作
def updategoods(request,uid):
	try:
		b = False
		oldpicname = request.POST['oldpicname']
		if None != request.FILES.get("pic"):
			myfile = request.FILES.get("pic", None)
			if not myfile:
				return HttpResponse("没有上传文件信息！")
	        # 以时间戳命名一个新图片名称
			filename = str(time.time())+"."+myfile.name.split('.').pop()
			destination = open(os.path.join("./static/goods/",filename),'wb+')
			for chunk in myfile.chunks():      # 分块写入文件  
				destination.write(chunk)  
			destination.close()
	        # 执行图片缩放
			im = Image.open("./static/goods/"+filename)
	        # 缩放到375*375:
			im.thumbnail((375, 375))
	        # 把缩放后的图像用jpeg格式保存:
			im.save("./static/goods/"+filename, 'jpeg')
	        # 缩放到220*220:
			im.thumbnail((220, 220))
			# 把缩放后的图像用jpeg格式保存:
			im.save("./static/goods/m_"+filename, 'jpeg')
			# 缩放到220*220:
			im.thumbnail((100, 100))
			# 把缩放后的图像用jpeg格式保存:
			im.save("./static/goods/s_"+filename, 'jpeg')
			b = True
			picname = filename
		else:
			picname = oldpicname
		ob = Goods.objects.get(id=uid)
		ob.goods = request.POST['goods']
		ob.typeid = request.POST['typeid']
		ob.company = request.POST['company']
		ob.price = request.POST['price']
		ob.store = request.POST['store']
		ob.descr = request.POST['descr']
		ob.picname = picname
		ob.status = request.POST['status']
		ob.save()
		context = {'info':'修改成功！'}
		if b:
			os.remove("./static/goods/m_"+oldpicname) #执行老图片删除  
			os.remove("./static/goods/s_"+oldpicname) #执行老图片删除  
			os.remove("./static/goods/"+oldpicname) #执行老图片删除  
	except:
		context = {'info':'修改失败！'}
		if b:
			os.remove("./static/goods/m_"+picname) #执行新图片删除  
			os.remove("./static/goods/s_"+picname) #执行新图片删除  
			os.remove("./static/goods/"+picname) #执行新图片删除  
	return render(request,"myadmin/info.html",context)

# ==============后台商品类别信息管理======================
# 浏览商品类别信息
def browsetype(request):
    list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    # 遍历查询结果，为每个结果对象追加一个pname属性，目的用于缩进标题
    for ob in list:
        ob.pname = ". . . " * (ob.path.count(',')-1)
        # print(list[0].__dict__)
    context = {"typeslist":list}
    return render(request,'myadmin/browsetype.html',context)

# 商品类别信息添加表单
def addtype(request,tid):
    # 获取父类别信息，若没有则默认为根类别信息
    if tid == '0':
        context = {'pid':0,'path':'0,','name':'根类别'}
    else:
        ob = Types.objects.get(id=tid)
        context = {'pid':ob.id,'path':ob.path+str(ob.id)+',','name':ob.name}
    return render(request,'myadmin/addtype.html',context)

#执行商品类别信息添加	
def inserttype(request):
    try:
        ob = Types()
        ob.name = request.POST['name']
        ob.pid = request.POST['pid']
        ob.path = request.POST['path']
        ob.save()
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}

    return render(request,"myadmin/info.html",context)

# 执行商品类别信息删除
def deltype(request,tid):
    try:
        # 获取被删除商品的子类别信息量，若有数据，就禁止删除当前类别
        row = Types.objects.filter(pid=tid).count()
        if row > 0:
            context = {'info':'删除失败：此类别下还有子类别！'}
            return render(request,"myadmin/info.html",context)
        ob = Types.objects.get(id=tid)
        ob.delete()
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/info.html",context)

# 打开商品类别信息编辑表单
def edittype(request,tid):
	try:
		ob = Types.objects.get(id=tid)
		context = {'type':ob}
		return render(request,"myadmin/edittype.html",context)
	except:
		context = {'info':'没有找到要修改的信息！'}
	return render(request,"myadmin/info.html",context)

# 执行商品类别信息编辑
def updatetype(request,tid):
    try:
        ob = Types.objects.get(id=tid)
        ob.name = request.POST['name']
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myadmin/info.html",context)