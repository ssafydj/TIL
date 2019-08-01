
def positive_sum(numbers):
    plus = 0
# numbers 는 list 이지만, 그 안에 있는 int 를 계산해야하므로 빈 list가 아니라 0을 더해가는 방법.
    for number in numbers:
        if number > 0:
            plus += number
    return plus    

print(positive_sum([1, -4, 7, 12]))
print(positive_sum([-1, -2, -3, -4]))

