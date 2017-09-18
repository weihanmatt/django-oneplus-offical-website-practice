from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Users
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from myadmin.models import Goods,Types,Order,Detail
from PIL import Image
import time
import os


def browseorders(request,pIndex):
	list = Order.objects.all()
	p = Paginator(list,5)
	# 处理当前页号信息
	if pIndex=="":
		pIndex = '1'
	pIndex = int(pIndex)
	# 获取当前页数据
	list2 = p.page(pIndex)
	# for i in list2:
	# 	ob = Users.objects.get(id=i.uid)
	# 	i.typename = ob.name
	plist = p.page_range
	return render(request,"myadmin/browseorders.html",{'orderslist':list2,'pIndex':pIndex,'plist':plist})



def deleteorders(request,uid):
	try:
		# 获取被删除商品信的息量，先删除对应的图片
		ob = Order.objects.get(id=uid)
		#执行商品信息的删除 
		ob.delete()
		dt = Detail.objects.filter(orderid = uid)
		for i in dt:
			i.delete()
		context = {'info':'删除成功！'}
	except:
		context = {'info':'删除失败！'}
	return render(request,"myadmin/info.html",context)

#加载编辑商品信息
def editorders(request,uid):
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
	return render(request,"myadmin/editorders.html",{'orders':ob,'detail':dt})
	# except:
	# 	context = {'info':'没有找到要修改的信息！'}
	# return render(request,"myadmin/info.html",context)

def updateorders(request,uid):
	try:
		ob = Order.objects.get(id= uid)
		ob.linkman = request.POST['linkman']
		ob.address= request.POST['address']
		ob.code = request.POST['code']
		ob.phone = request.POST['phone']
		ob.total = request.POST['total']	
		ob.status = request.POST['status']
		# return HttpResponse(request.POST['status'])
		ob.save()
		context = {'info':'修改成功！'}

	except:
	    context = {'info':'修改失败！'}
	return render(request,"myadmin/info.html",context)

	