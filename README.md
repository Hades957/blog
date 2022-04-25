# blog
python_django博客系统


# databases
```mysql
# 新建Mysql数据库：blog
create database blog charset=utf8;
# 新建Mysql用户：blog
create user blog identified by '123456';
# 授权blog用户访问blog数据库
grant all on blog.* to 'blog'@'%';
# 授权结束后刷新特权
flush privileges;
```

# 开发过程
1. urls中定义视图，定义一个函数
2. urlpatterns中增加访问路径

# 日志使用过程
1. 导入系统的logging
import logging
2. 创建(获取)日志器
logger = logging.getLogger('django')
3. 使用日志器，记录信息
logger.info('info')
---
日志级别
* FATAL/CRITICAL = 重大的，危险的
* ERROR = 错误
* WARNING = 警告
* INFO = 信息
* DEBUG = 调试
* NOTSET = 未设置

# 静态资源文件
1. 准备静态资源文件，放置在项目根目录下static文件夹内
2. 指定静态文件的加载路径STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
3. 配置完成后，运行程序，测试结果  http://127.0.0.1:8000/static/index.html

# 创建用户模块应用
```
1. 创建子应用users
python manage.py startapp users
2. 注册用户模块应用
INSTALLED_APPS = [
    ...
    'users.apps.UsersConfig',
]
3. 准备模板目录并设置模板路径
    创建模板文件夹templates并在settings文件中设置模板路径
4. 定义用户注册视图
    * 将static文件夹下在register.html拖拽到templates文件中
    * 在users.views.py文件中定义视图
5. 定义用户注册路由
    * 在users子应用中创建urls.py文件，并定义子路由
    * 在工程的urls.py总路由中添加子应用路由引导
    * 运行测试程序
6.修改静态文件加载方式
    * 是由于静态资源加载是相对路径，因此我们需要修改静态资源的加载方式
    * 运行测试程序，没有问题   http://127.0.0.1:8000/users/register
```
