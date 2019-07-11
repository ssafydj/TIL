# 딕셔너리 반복문 활용하기

lunch = {
    '중국집': '02-123-3456',
    '일식집': '031-478-1113',
    '양식집': '042-741-4879'
}

# 기본 활용
for key in lunch:
    print(key)
    print(lunch[key])

# .items()   (key, value 동시에 출력)
for key, value in lunch.items():
    print(key, value)

# value 만 가져오기 .values()
for value in lunch.values():
    print(value)

# key 만 가져오기 .keys()
for key in lunch.keys():
    print(key)


