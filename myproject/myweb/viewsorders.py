from django.shortcuts import render
from myadmin.models import Users
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse
from myadmin.models import Goods,Types
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
		context = {'vip':'你好'+request.session['mywebuser'],'haha':'退出'}
		
	else:
		context = {'vip':'请登录'}
	return context

#购物车
def shopchart(request):
	return render(request,"myweb/shopchart.html")

#加入购物车
def shopchartadd(request,gid):
	goods = Goods.objects.get(id=gid)
	shop = goods.toDict()
	# shop['m'] = int(request.post['m'])
	if 'shoplist' in request.session:
		shoplist = request.session['shoplist']
	else:
		shoplist={}
	if gid in shoplist:
		#商品数量加一
		shoplist[gid]['num'] = shoplist[gid]['num'] + 1
	else:
		shoplist[gid] = shop
	request.session['shoplist'] = shoplist
	return render(request,'myweb/shopchart.html')


def shopchartdel(request,gid):
    shoplist = request.session['shoplist']
    del shoplist[gid]
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopchart'))

def shopchartclear(request):
    context = loadContext(request)
    request.session['shoplist'] = {}
    return render(request,"myweb/shopchart.html",context)

def shopchartchange(request):
    context = loadContext(request)
    shoplist = request.session['shoplist']
    #获取信息
    shopid = request.GET['sid']
    num = int(request.GET['num'])
    if num<1:
        num = 1
    shoplist[shopid]['num'] = num #更改商品数量
    request.session['shoplist'] = shoplist
    return render(request,"myweb/shopchart.html",context)











