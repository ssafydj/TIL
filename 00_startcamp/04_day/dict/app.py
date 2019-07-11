import requests
from flask import Flask, render_template, request

app = Flask(__name__)

 #로또회사 / 내 번호입력 페이지
 
@app.route('/lotto_check')
def lotto_check():
     return render_template('lotto_check.html')  


@app.route('/lotto_result')
def lotto_result():
    # 회차 번호를 받아온다.
    num = request.args.get('num')
    # 동행복권에 요청을 보내 응답을 받는다.
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    # json 형태로 정제 (크롬에서 보는 결과와 같은 모양)
    lotto = res.json()

    # 당첨번호 6개 가져오기
    winner = []
    for i in range(1, 7): 
        winner.append(lotto[f'drwtNo{i}'])

    # 내 번호 리스트 만들기
    numbers = []
    for num in request.args.get('numbers').split():   # split: 공백을 기준으로 문자/숫자를 따로 구분하는 함수
        numbers.append(int(num))                     # append: 목록 마지막에 새로운 문자/숫자를 추가하는 함수
    # 등수 찾기 (몇 개 맞았는지 교집합이 필요)
    matched = 0
    # match: 목록과 목록을 비교하여 같은 항목을 찾는 함수
    #내 번호를 뽑아서 당첨번호 리스트(winner)에 있는지 확인
    for num in  numbers: 
        if num in winner:
            matched += 1
    if matched == 6:
        result = '1등입니다!'
    elif matched == 5:
        if lotto['bnusNo'] in numbers:
            result = '2등입니다!'
        else:
            result = '3등입니다!'
    elif matched == 4:
            result = '4등입니다!'

    elif matched == 3:
            result = '5등입니다!'

    else:
        result = '꽝입니다!'

    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)