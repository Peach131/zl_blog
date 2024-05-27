from django.contrib import admin
from home.models import ArticleCategory
from home.models import Article
from home.models import Comment
# Register your models here.

# 类别管理
admin.site.register(ArticleCategory)

# 文章管理
admin.site.register(Article)

# 评论管理
admin.site.register(Comment)
