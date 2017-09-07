# -*- coding: utf-8 -*-
# 
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator

from myweb.models import Stu,District

def index(request):
    return render(request,"myweb/index.html")


#使用session实现简单购物车联系
def shop(request):
    if 'shoplist' in request.session:
        pass
    else:
        request.session['shoplist']={}
    return render(request,"myweb/shop/shop.html")

#添加购物车
def addshop(request):
    #获取要放入购物车中的商品信息
    shop = {
        'id':request.POST['id'],
        'name':request.POST['name'],
        'price':request.POST['price'],
        'num':1,
    }
    #从session获取购物车信息
    shoplist = request.session['shoplist']
    #判断此商品是否在购物车中
    if shop['id'] in shoplist:
        #商品数量加一
        shoplist[shop['id']]['num']+=1
    else:
        #新商品添加
        shoplist[shop['id']]=shop

    #将购物车信息放回到session
    request.session['shoplist'] = shoplist
    return render(request,"myweb/shop/showshop.html")

def showshop(request):
    shoplist = request.session['shoplist']
    
    request.session['shoplist'] = shoplist
    return render(request,"myweb/shop/showshop.html")

def delshop(request,shopid):
    shoplist = request.session['shoplist']
    del shoplist[shopid]
    request.session['shoplist'] = shoplist
    return render(request,"myweb/shop/showshop.html")

def clearshop(request):
    request.session['shoplist'] = {}
    return render(request,"myweb/shop/showshop.html")

def changeshop(request):
    shoplist = request.session['shoplist']
    #获取信息
    shopid = request.GET['shopid']
    num = int(request.GET['num'])
    if num<1:
        num = 1
    shoplist[shopid]['num'] = num #更改商品数量
    request.session['shoplist'] = shoplist
    return render(request,"myweb/shop/showshop.html")

def login(request):
    return render(request,"myweb/login.html")

def showcode(request):
    #引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定义变量，用于画面的背景色、宽、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (242,164,247)
    width = 100
    height = 25
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
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
