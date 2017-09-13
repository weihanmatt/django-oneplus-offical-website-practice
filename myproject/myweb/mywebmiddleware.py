# 自定义后台中间件类
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

import re

class MywebMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        #print("AdminMiddleware")

    def __call__(self, request):
        # 获取当前请求路径
        path = request.path
        #print("Hello World!"+path)
        # 判断当前请求是否是访问购物车
        if re.match("/shopchart",path):
            # 判断当前用户是否没有登录
            if "mywebuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('login'))
        

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        
        return response