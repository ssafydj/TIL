#DOCstring > 주석과 비슷하게 파일 실행에 영향주지 않으면서 설명하는 용도
"""
이 함수는~
누가 만들었고~
어떻게 사용하는~
함수입니다.
"""

"""
Q: 다음과 같은 내용의 파일 quest.txt 가 있다.
0
1
2
3

이 파일의 내용을 다음과 같이 역순으로 reverse_quest.txt 라는 파일로 저장하시오.

"""

# 순서 
#1. 읽기
with open('quest.txt', 'r') as f:
    lines = f.readlines()
   

#2. 뒤집고(how to reverse list in python~~ etc... googling 자주 해보기)

lines.reverse()
print(lines)

#3. 작성하고
with open('reverse_quest.txt', 'w') as f:
    for line in lines:
        f.write(line)
# or

with open('reverse_quest.txt', 'w') as f:
    f.writelines(lines)

