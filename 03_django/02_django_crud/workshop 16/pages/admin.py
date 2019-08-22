from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'birthday', 'age',)
# list_display 요소는 models.py 에 변수와 동일
admin.site.register(Student, StudentAdmin)
        # student: models.py 의 클래스변수
        # studentAdmin: admin.py의 클래스 변수