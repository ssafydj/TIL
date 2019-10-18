from django.urls import reverse
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

def get_absolute_url(self):
    # return f'/articles/{self.pk}/'
    # return reverse('articles:detail', args=[self.pk]) # articles/10/
    return reverse('articles:detail', kwargs={'pk': self.pk}) #articles/10/
    # 주의사항
    # reverse 함수에 args 와 kwargs 를 동시에 인자로 보낼 수 없다.
