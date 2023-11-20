from django.contrib import admin
# modelsからBlogPostクラスをインポート
from .models import BlogPost

# Django管理サイトニBlogPostを登録する
admin.site.register(BlogPost)

