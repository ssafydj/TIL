from django.contrib import admin
from .models import Article  # 명시적 상대경로 표현 .(현재위치) 

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # 튜플이나 리스트로 작성한다. (대부분 문서는 튜플로 작성되어있다.)
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',) # 무조건 사용해야하는것 나머지는 선택사항
    list_filter = ('created_at',)
    list_display_links = ('content',)
    list_editable = ('title',)
    list_per_page = 2  # default = 100 줄



admin.site.register(Article, ArticleAdmin)
