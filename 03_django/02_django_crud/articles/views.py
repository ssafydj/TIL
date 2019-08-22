from IPython import embed  # embde 라는 일시정지시키는 모듈
from django.core.exceptions import ValidationError # 필요x
from django.shortcuts import render, redirect  # render를 보완하는 redirect
from .models import Article  # ?

# Create your views here.

def index(request):
    # articles = Article.objects.all() # 오름차순
    articles = Article.objects.order_by('-pk') # DB가 변경하여 역순으로 받음  
    # index.html에서, articles 를 for 문 돌려서 하나씩 정보를 불러온다.
    # articles = Article.objects.all()[::-1] # python 이 변경
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)
    

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.full_clean()   #유효성 검증 과정 , 이 과정이 없으면 blank=False 등 조건이 작동안함
    except ValidationError:
        raise ValidationError('Error')
    else:
        article.save()
    return redirect('/articles/')  

def detail(request, pk):
    article = Article.objects.get(pk=pk) # 앞에 pk 는 테이블의 컬럼 뒤에 pk는 위의 변수 pk /articles/pk 값으로 문서에 직접 접근
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/') #삭제 후 메인 페이지인 articles로 복귀


def edit(request, pk): # 수정할 대상 필요
    article = Article.objects.get(pk=pk) # 수정할 대상 1개를 선택
    context = {'article': article,}
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)

    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}/')
    #페이지가 필요없으므로 redirect


