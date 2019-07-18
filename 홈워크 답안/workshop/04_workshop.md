04_workshop

1. 양의 정수 x를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요. 

def response(n):

> import math
> math.sqrt(2)



    def my_sqrt(n):     
        x, y = 1, n 
        result = 1
    
    
    while not math.isclose(result**2, n): 
        result = (x+y)/2    
        if result**2 < n:
            x = result
        else:
            y = result
    return result
    print(my_sqrt(2))
