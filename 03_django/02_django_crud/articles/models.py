from django.db import models

# Create your models here.
# 보여질 데이터를 어떻게 구성할지를 담당
class Article(models.Model):
    title = models.CharField(max_length=20) #blank=True -> 공백도 허용 default = false
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# 객체표현
def __str__(self):
    return self.title

