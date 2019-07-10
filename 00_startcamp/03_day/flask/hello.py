from flask import Flask
app = Flask(__name__)


# 아래의 3줄이 실행+출력을 위한 코드의 전부
@app.route('/')
def hello():
    return 'Damn!'

@app.route('/ssafy') # http://127.0.0.1:5000 + 기본주소에 추가 하고 싶은 주소를 / 뒤에 작성
def ssafy():
    return 'This is SSAFY!' # http://127.0.0.1:5000/ssafy 에 접속했을 때 나오는 값