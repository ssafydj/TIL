# 딕셔너리 만들기 - 1
lunch = {
    '중국집': '02-123-3456',
    '일식집': '031-478-1113',
    '양식집': '042-741-4879'
}

# 딕셔너리 만들기 - 2
dinner =dict(중국집='02-123-3456', 일식집='02-456-7890')

# 딕셔너리에 내용 추가하기
lunch['분식집'] = '031-123-1234'


# 딕셔너리 내용 가져오기
idol ={
    'bts': {
        '지민': 25,
        'RM' : 24
    }
}

# Rm의 나이는? (중요) (상위 폴더부터 차례대로 찾아야함)
idol['bts']['RM']          
idol.get('bts').get('RM')