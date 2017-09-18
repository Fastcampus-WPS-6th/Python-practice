l = list('abcde')

loop = 0
while True:
    msg = '숫자입력: ' if not loop else '다시 입력하세요: '
    loop += 1
    try:
        value = int(input(msg))
        l[value]
        print(l[value])
    except IndexError:
        print('인덱스가 너무큽니다')
    except ValueError:
        print('숫자만 입력하세요 ㅡㅡ')
    else:
        print('제대로 출력되었습니다')
        break
    finally:
        print('지금은 %s번째 loop입니다' % loop)

