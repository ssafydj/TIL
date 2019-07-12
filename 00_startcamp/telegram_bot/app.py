from flask import Flask, render_template , request
import requests
from decouple import config


app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')


@app.route('/')
def hello():
    return 'Hi there!'


# webhook telegram 과 flask 를 연결
@app.route(f'/{token}', methods=['post'])
def telegram():
    # step 1. 데이터 구조 print 해보기

    from_telegram = request.get_json()

    if from_telegram.get('message') is not None:
         # step 2. 그대로 돌려보내기 (메아리 기능)
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        
        #한글 키워드 받기
        
        # /번역 으로 입력이 시작되면, 파파고로 번역이 동작한다.
        if text[0:4] == '/번역 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id, 
                'X-Naver-Client-Secret': naver_client_secret
            }
            data = {'source': 'ko', 'target': 'es', 'text': text [4:]}    # text[4:] 4칸~ 무한대 까지 불러온다
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers = headers, data = data)
            text = papago_res.json().get('message').get('result').get('translatedText') # 여기에 한/영 번역 텍스트가 있다.

        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')


    return '', 200


