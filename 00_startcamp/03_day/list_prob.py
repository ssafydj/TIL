str = input( '문자를 입력하세요: ')

#아래에 코드를 작성해 주세요.
print(f'첫글자는'{str[0]}, 마지막 글자 {strp[-1]}'')


#문제 2. 

numbers = int(input('숫자를 입력하세요:'))

for i in range(numbers):
    print(i+1)

#문제 3. 

numbers = int(input('숫자를 입력하세요:'))

#if 2로 나눈 나머지가 있으면:
if number % 2:
    print('홀수입니다.')
else:
    print('짝수입니다.')

True(1,2...) / False(0) 

#or

if number % 2==0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

#문제 4.

a = int(input('국어: '))
b = int(input('영어: ')) 
c = int(input('수학: ')) 
d = int(input('과학: ')) 

if a >= 90 and  b > 80 and c > 85 and d >= 80:
    print(true)
else:
    print(false)


#문제 5.

prices = input('물품 가격을 입력하세요: ')

# 문자열을 리스트로 형태 변환하는게 포인트

makes = prices.split(';')

boxes = []

for make in makes:
    boxes.
#리스트에 요소를 추가하는 메서드 .append()
#list.append(1) : 리스트에 1을 추가한다 라는 의미
