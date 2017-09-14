level = 0

def global():
    global level
    level += 3
    print(level)
    

def outer():
    # outer함수의 지역변수 level
    level = 50

    # outer함수의 지역함수 inner
    def inner():
        # inner에서 nonlocal로 outer의 level을 사용
        nonlocal level
        level += 3
        # outer함수의 level을 출력
        print(level)

    # outer함수는 자신의 내부에서 정의된 inner함수를 리턴
    return inner

f1 = outer()
f2 = outer()

print(f1)
print(f2)

f1()
f1()

f2()


