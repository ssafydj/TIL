def calc(equation):
    equation = equation.replace('+', ' +')
    equation = equation.replace('-', ' -')
    return sum(map(int, equation.split()))
    # split으로 str -> list로 변환한 후에 int로 형 변환이 가능하다.
    # ValueError: invalid literal for int() with base 10: > str을 계산할 때 발생하는 오류


print(calc('123 +2 -124'))
print(calc('-12+12-7979+9191'))
print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))