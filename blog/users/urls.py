# 1.在users子应用中创建urls.py文件，并定义子路由
# * 进行users子应用的视图路由
from django.urls import path

from users.views import RegisterView

urlpatterns = [
    # 参数1： 路由
    # 参数2： 视图函数
    # 参数3： 路由名，方便通过reverse来获取路由
    path('register/', RegisterView.as_view(), name='register')
]
# 2.在工程的urls.py总路由中添加子应用路由引导
