from django.shortcuts import render

# Create your views here.
# 在users.views.py文件中定义视图
from django.views import View
from django.http.response import HttpResponseBadRequest
from libs.captcha.captcha import captcha
from django_redis import get_redis_connection
from django.http import HttpResponse


# 注册视图
class RegisterView(View):
    """用户注册"""

    def get(self, request):
        """
        提供注册界面
        :param request: 请求对象
        :return: 注册界面
        """

        return render(request, 'register.html')


class ImageCodeView(View):
    """验证码"""

    def get(self, request):
        """
        1. 接收前端传递过来的uuid
        2. 判断uuid是否获取到
        3. 通过调用captcha来生成图片验证码（图片二进制和图片内容）
        4. 将图片内容保存到redis中
            uuid作为一个key，图片内容作为一个value，同时我们还需要设置一个实数
        5. 返回图片二进制
        """
        # 1. 接收前端传递过来的uuid
        uuid = request.GET.get('uuid')
        # 2. 判断uuid是否获取到
        if uuid is None:
            return HttpResponseBadRequest('没有传递uuid')
        # 3. 通过调用captcha来生成图片验证码（图片二进制和图片内容）
        text, image = captcha.generate_captcha()
        # 4. 将图片内容保存到redis中
        #     uuid作为一个key，图片内容作为一个value，同时我们还需要设置一个实数
        redis_conn = get_redis_connection('default')
        # key 设置为uuid, seconds 过期秒数 300s, value 生成的图片二进制内容
        redis_conn.setex('img:%s' % uuid, 300, text)
        # 5. 返回图片二进制,注意指定返回的是图片形式
        return HttpResponse(image, content_type='image/jpeg')