from django.shortcuts import render
from myadmin.models import Users
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from myadmin.models import Goods,Types
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
	plist = p.page_range
	return render(request,"myadmin/browsegoods.html",{'goodslist':list2,'pIndex':pIndex,'plist':plist})

#添加商品路由
def addgoods(request):
	return render(request,"myadmin/addgoods.html")

#添加商品
def insertgoods(request): 
	try:
		ob = Goods()
		ob.typeid = request.POST['typeid']
		ob.goods = request.POST['goods']
		ob.company = request.POST['company']
		ob.price = request.POST['price']
		ob.picname = request.POST['picname']
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

#删除用户
def deletegoods(request,uid):
	try:
		ob = Goods.objects.get(id=uid)
		ob.delete()
		context = {'info':'删除成功！'}
	except:
	    context = {'info':'删除失败！'}
	return render(request,"myadmin/info.html",context)

#加载编辑商品信息
def editgoods(request,uid):
	ob = Goods.objects.get(id=uid)
	context = {'goods':ob}
	return render(request,"myadmin/editgoods.html",context)

# 执行商品编辑操作
def updategoods(request,uid):
	try:
		ob.typeid = request.POST['typeid']
		ob.goods = request.POST['goods']
		ob.company = request.POST['company']
		ob.price = request.POST['price']
		ob.picname = request.POST['picname']
		ob.num = request.POST['num']
		ob.clicknum = request.POST['clicknum']
		ob.descr = request.POST['descr']
		ob.store = request.POST['store']
		ob.status = request.POST['status']
		ob.addtime = time.time()
		ob.save()
		context = {'info':'添加成功！'}
	except:
	    context = {'info':'修改失败！'}
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