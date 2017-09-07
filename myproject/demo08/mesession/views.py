from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator

from mesession.models import Stu

from mesession.models import District

#stu学生信息分页实例
def stu(request,pIndex):
    #return HttpResponse('ok')
    list = Stu.objects.all()
    #实例化分页对象
    p = Paginator(list,3)
    # 处理当前页号信息
    if pIndex=="":
        pIndex = '1'
    pIndex = int(pIndex)
    # 获取当前页数据
    list2 = p.page(pIndex)
    plist = p.page_range
    return render(request,"mesession/stu.html",{'stulist':list2,'pIndex':pIndex,'plist':plist})





# # 加载城市级联信息操作模板
def showdistrict(request):
    return render(request,"mesession/district.html")

# 加载对应的城市信息，并json格式ajax方式响应
def district(request,upid):
    dlist = District.objects.filter(upid=upid)
    list = []
    for ob in dlist:
        list.append({'id':ob.id,'name':ob.name})
    return JsonResponse({'data':list})
    #return HttpResponse(list)