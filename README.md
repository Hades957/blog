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
