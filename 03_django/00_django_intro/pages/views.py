# django imports style guide
# 1. standard library (파이썬 내장)
# 2. third-party (requets)
# 3. django  (from django.shortcuts import render)
# 4. local django

import random
from datetime import datetime
from pprint import pprint
import requests
from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'pages/index.html') # render()에 첫 인자도 반드시 request

# view 함수간에는 2 줄을 띄는게 convention
def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'pages/introduce.html', context)


def dinner(request):
    menu = ['족발', '햄버거', '짬뽕', '덮밥']
    pick = random.choice(menu)
    context = {'temp_pick': pick}
    return render(request, 'pages/dinner.html', context)
    # value pick 은 위의 pick, key의 pick은 template에서 가져올 pick


def image(request):
    return render(request, 'pages/image.html')


# <variable routing>
## 동적 라우팅 -> 주소자체를 변수처럼 사용 request 이외에 다른 변수가 필요
def hello(request, name):
    menu = ['족발', '햄버거', '짬뽕', '덮밥']
    pick = random.choice(menu)
    context = {'name': name, 'temp_pick': pick}  # context에 변수를 자유롭게 추가해서 사용가능
    return render(request, 'pages/hello.html', context)


def times(request, num1, num2):
    num3 = num1 * num2
    context = {'num3': num3, 'num1': num1, 'num2': num2,} 
    return render(request, 'pages/times.html', context)

def area(request, r):
    area = (r**2)*3.14
    context = {'r': r, 'area': area,}
    return render(request, 'pages/area.html', context)


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
    return render(request, 'pages/template_language.html', context)


def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result,}
    return render(request, 'pages/isitgwangbok.html', context)


def throw(request):
    return render(request, 'pages/throw.html')


def catch(request):
    # pprint(request)
    # pprint(request.scheme)
    # pprint(request.path)
    # pprint(request.method)
    # pprint(request.GET)   >get 을 쓰는 이유는 내부적으로 querydict 라는 dictionary 형태로 정보를 제공하므로
    pprint(request.meta)


    message = request.GET.get('message')
    # 딕셔너리에서 키 값 가져올 때 get('key 값')
    context = {'message': message,}
    return render(request, 'pages/catch.html', context)


def art(request):
    return render(request, 'pages/art.html')


def result(request):
    # 1. art에서 form 으로 보낸 데이터를 받는다.
    word = request.GET.get('word')
    # ctrl C 로 서버 끄고 pip install requests 필요 import 도
    # 그냥 쓸 수 없으니 word라는 변수에 담는다.
    # 2. ARTII API 폰트 리스트로 요청을 보내 응답을 text로 받는다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    # 3. str 을 list로 바꾼다
    fonts = fonts.split('\n')

    # 4. fonts list 안에 들어있는 요소 중 하나를 선택해서 변수에 저장
    font = random.choice(fonts)

    # 5. 위에서 만든 word 와 font 를 가지고 다시 요청을 만들어서 보내 응답 결과를 받는다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text # response라는 객체에 .text로 출력
    
    context = {'response': response,}
    return render(request, 'pages/result.html', context)


def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name') 
    pwd = request.POST.get('pwd')
    context = {'name': name, 'pwd': pwd,}
    return render(request, 'pages/user_create.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')

    
