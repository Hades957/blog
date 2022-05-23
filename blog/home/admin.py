from django.contrib import admin

# Register your models here.
# 注册模型
from home.models import ArticleCategory

admin.site.register(ArticleCategory)
