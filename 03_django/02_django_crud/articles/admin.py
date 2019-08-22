from django.contrib import admin
from .models import Article
    #?? 현재 있는 디렉토리??
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):  # admin에 있는 ModelAdmin에 상속을 받음
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)


    
admin.site.register(Article, ArticleAdmin)  
#/admin 에 articles 폴더에, 위의 ArticleAdmin 클래스에 
# 나열한 list_display 항목들을 보여준다