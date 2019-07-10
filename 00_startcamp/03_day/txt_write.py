 # 변수에 만들고 싶은 파일을 open() 해야 한다.
 # open() 할 때, r: 읽기 / w: 쓰기(덮어 씌워짐) / a: 추가(일반적인 추가)
 # f = open('만들 파일 명', '행동')

f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'This is line {i+1}.\n')
f.close()


# with 구문(context manager) > 매번 반복되는 f.close()의 중복을 해결하기 위해 고안됨

with open('with_ssafy.txt', 'w') as f:
    for i in range(10):
        f.write(f'This is line {i+1}.\n')

# writelines() : list를 넣어주면, 요소 하나당 한 줄씩 작성한다.
with open('ssafy.txt', 'w') as f:
    f. writelines(['0\n', '1\n', '2\n', '3\n'])



## 이스케이프 문자열(기존 문자의 기능 이외에 자기만의 능력이 있는 문자)
# \n : 개행문자(다음 줄 이동)
# \t : tap 기능
# \\ : \ 기능
# \' : '
# \" : "
