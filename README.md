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
