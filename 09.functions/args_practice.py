# 인자가 2개 주어지면 두 인자를 서로 곱하고,
# 1개 주어지면 해당 인자를 제곱하는 함수를 작성 및 실행
# 함수는 위치인자묶음 변수를 사용
#   -> 어려울경우 마음대로 구현
def mul(*args):
    if len(args) == 1:
        return args[0] ** 2
    elif len(args) == 2:
        return args[0] * args[1]

print(mul(3))
print(mul(5, 7))

