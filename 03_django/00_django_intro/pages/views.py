# django imports style guide
# 1. standard library (파이썬 내장)
# 2. third-party (requets)
# 3. django  (from django.shortcuts import render)
# 4. local django

import random
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'index.html') # render()에 첫 인자도 반드시 request

# view 함수간에는 2 줄을 띄는게 convention
def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'introduce.html', context)


def dinner(request):
    menu = ['족발', '햄버거', '짬뽕', '덮밥']
    pick = random.choice(menu)
    context = {'temp_pick': pick}
    return render(request, 'dinner.html', context)
    # value pick 은 위의 pick, key의 pick은 template에서 가져올 pick


def image(request):
    return render(request, 'image.html')


# <variable routing>
## 동적 라우팅 -> 주소자체를 변수처럼 사용 request 이외에 다른 변수가 필요
def hello(request, name):
    menu = ['족발', '햄버거', '짬뽕', '덮밥']
    pick = random.choice(menu)
    context = {'name': name, 'temp_pick': pick}  # context에 변수를 자유롭게 추가해서 사용가능
    return render(request, 'hello.html', context)


def times(request, num1, num2):
    num3 = num1 * num2
    context = {'num3': num3, 'num1': num1, 'num2': num2,} 
    return render(request, 'times.html', context)

def area(request, r):
    area = (r**2)*3.14
    context = {'r': r, 'area': area,}
    return render(request, 'area.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피',]
    my_sentence = 'Life is short. You need python'
    messages = ['apple', 'banana', 'cucumber', 'bean']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)


def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result,}
    return render(request, 'isitgwangbok.html', context)