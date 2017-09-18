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
		context = {'vip':'你好'+request.session['mywebuser'],'haha':'退出'}
		
	else:
		context = {'vip':'请登录'}
	return context

#购物车
def shopchart(request):
	context = loadlogin(request)
	return render(request,"myweb/shopchart.html",context)

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


#订单页
def order(request):
	tt = request.GET.get('tt')
	# request.session['total'] = tt
	gids = tt.split(',')
	shoplist = request.session['shoplist']
	orderlist = {}
	total = 0
	# request.session['orderlist'] = {}
	# return HttpResponse(gids[2])
	for i in gids:
		if i == '':
			continue
		orderlist[i] = shoplist[i]
		total += shoplist[i]['price']*shoplist[i]['num']
	request.session['orderlist'] = orderlist
	request.session['total'] = total
	context ={}
	ob = Users.objects.get(id = request.session['webuserid'])
	context['user'] = ob
	# return HttpResponse(tt)
	return render(request,"myweb/order.html",context)

def orderconfirm(request):
	context = {}
	ob = Order()
	ob.linkman = request.POST['name']
	ob.address = request.POST['address']
	ob.code = request.POST['code']
	ob.phone = request.POST['phone']
	context['order'] = ob
	return render(request,"myweb/orderconfirm.html",context)

def insertorder(request):
	ob = Order()
	ob.uid = request.session['webuserid']
	ob.linkman = request.GET.get('linkman')
	ob.address = request.GET.get('address')
	ob.code = request.GET.get('code')
	ob.phone = request.GET.get('phone')
	ob.addtime = time.time()
	ob.total = float(request.session['total'])
	ob.save()
	for shop in request.session['orderlist'].values():
		detail = Detail()
		detail.orderid = ob.id
		detail.goodsid = shop['id']
		detail.picname = Goods.objects.get(id=shop['id']).picname
		detail.goodsname = shop['goods']
		detail.price = shop['price']
		detail.num = shop['num']
		detail.save()
	
	shoplist = request.session['shoplist']

	for lmt in request.session['orderlist']:
		del shoplist[lmt]

	# request.session['shoplist'] = {}
	request.session['orderlist'] = {}
	del request.session['total']
	context ={'info':'下单成功'}
	return render(request,"myweb/info.html",context)










