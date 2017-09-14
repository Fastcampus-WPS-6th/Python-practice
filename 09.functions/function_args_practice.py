# 1. call function! 이라는 문자열을 출력하는 함수 정의# 2. 함수를 인자로 받아 실행하는 execute_arg_function함수 정의
# 3. execute_arg_function함수에서 위의 'call function!'을 출력하는 함수를 인자로 받아 해당 함수를 실행
def call_func():
    ret = 'call function!'
    print(id(ret))
    return ret

def execute_arg_function(f):
    return f()


print(id(call_func()))
print(execute_arg_function(call_func))

