from flask import Flask, render_template, request
from datetime import datetime     #필요한 정보만 추출
import random

app = Flask(__name__)

@app.route('/')
def hello():
    #return 'Hello World!'
    return render_template('index.html')


@app.route('/ssafy')
def ssafy():
    return 'This is ssafy!'

@app.route('/dday')
def dday():

    #오늘 날짜
    today_time = datetime.now() #의미있는 변수명 설정의 어려움
    #수료 날짜
    endgame = datetime(2019, 11, 29)
    #수료 날짜 - 오늘 날짜
    dday = endgame - today_time   #datetime은 연산가능
    return f'{dday.days} 일 남았습니다.'


@app.route('/html')
def html():
        return '<h1>This is HTML Tag</h1>'


@app.route('/html_line')
def html_line():
    return """
    <h1> 여러 줄을 보내 봅시다</h1>
    <ul>
        <li>안녕하세요</li>
        <li>반갑습니다</li>

    </ul>
    """

# flask 중에서 variable routing(변수 라우팅) > 라우팅 하나로 여러가지 일을 처리
@app.route('/greeting/<string:name>')     #string은 기본값이므로 생략가능, 
def greeting(name):
    # return f'반갑습니다! {name}'
    return render_template('greeting.html', html_name=name)



@app.route('/cube/<int:number>')  #기본값은 string은 문자를 곱할 수 없으므로 int로 형변환이 필요
def cube(number):
        #연산을 모두 끝내고 변수만 cube.html로 넘긴다. 계산은 서버가, 템플릿은 결과를 보여주기만.
        result = number**3
        #return f'{number}의 세제곱은 {number**3}입니다.'  #number**: 제곱 #number**4: 4제곱
        return render_template('cube.html', result = result,  number =number)
                                              #앞의 result는 html의 변수, 뒤에 result는 위에 정의한 변수

#여러 메뉴 중에서 인원수 만큼 무작위로 메뉴로 응답
@app.route('/lunch/<int:people>')   #사람수가 입력되어야하므로 int
def lunch(people):
    menu = ['짬뽕', '짜장', '탕수육', '김밥', '양장피', '삼계탕']
    order = random.sample(menu, people)
    return f'{order} 입니다.'


@app.route('/movie')
def movie():
    movies = ['기생충', '토이스토리', '알라딘', '범죄', '스파이더맨', '전쟁', '재개봉']
    return render_template('movie.html', movies=movies)
                                                #오른쪽이 왼쪽으로 할당됨

#Flask request & response

@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    #print(dir(request))
    name = request.args.get('data') #안녕하세요
    return render_template('pong.html', name=name)

#flask              template
#1 ping 요청              2 ping html 응답
#3 pong 요청              4 pong html 응답 (request.args.get)

# fake naver/google
#https://search.naver.com/search.naver?query=
@app.route('/naver')
def naver():
	return render_template('naver.html')

@app.route('/google')
def google():
	return render_template('google.html')


@app.route('/von')
def von():
	return render_template('von.html')


@app.route('/vonvon/<string:people')
def vonvon():
	personality = ['money', 'kindness', 'appearance']
	result = random.choices(personality, people)

	return render_template('vonvon.html')
	name = request.args.get('data') 
	return render_template('vonvon.html', name=name)

@app.route('/godmademe')
def godmademe():
	name = request.args.get('name')

	first_list = ['잘생김', '못생김', '어중간한']
	second_list = ['자신감', '쑥스러움', '애교', '잘난척']
	third_list = ['허세', '돈복', '식욕', '물욕', '성욕']

	first = random.choice(first_list)
	second = random.choice(second_list)
	third = random.choice(third_list)
	return render_template('vonvon.html', name=name, first=first, second=second, third=third)


