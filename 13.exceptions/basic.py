l = list('abcd')
d = dict(name='Lux', champion_type='Magician')

print('program start')
try:
    print('before l[5]')
    # l[3]에 접근했을때 어느부분까지 코드가 실행되는지 확인
    print('check dict key')
    d['Sona']
    print('check list index')
    l[5]
    print('after l[5]')
except IndexError as e:
    print('l[5] exception!')
except KeyError as e:
    import traceback
    print("d['Sona'] exception!")
    print(traceback.format_exc())
    print(e)

"""
while문 내에 try구문에서 input을 이용해 숫자값을 입력받음
입력받은 숫자값에 해당하는 l[index]를 참조하고, IndexError가 날 경우 다시 숫자값을 입력받음
IndexError가 나지 않으면 while문 종료

"""

print('program terminate')

