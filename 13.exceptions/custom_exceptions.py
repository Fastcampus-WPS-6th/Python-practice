"""
1. 정규표현식으로 검사했을때 패턴이 없을 경우 발생할 NotMatchedException을 사용자정의
    1-1. Exception을 상속
    1-2. __init__메서드에서 패턴문자열과 소스문자열을 매개변수로 사용
    1-3. __str__메서드는 __init__에서 받은 "패턴문자열"이 "소스문자열"에 없다는 문자열을 반환(리턴)

2. 패턴문자열과 소스문자열을 매개변수로 갖는 search_from_source함수를 정의
    만약 re.search로 소스문자열에서 패턴을 검색했을때 MatchObject를 찾지 못하면, 
    raise NotMatchedException(패턴문자열, 소스문자열)을 발생시킴

3. try~except 구문에서 위 함수를 실행, 예외를 발생시키고 except구문에서 해당 예외를 받을 수 있도록 구현
"""
import re

# pattern과 source를 생성자 매개변수로 갖는 Exception클래스 정의
class NotMatchedException(Exception):
    def __init__(self, pattern, source):
        self.pattern = pattern
        self.source = source

    def __len__(self):
        return len(self.pattern)
    
    # print(obj)했을 때 출력될 내용
    def __str__(self):
        return f'Pattern "{self.pattern}" is not matched in source "{self.source}"'

# pattern과 source매개변수를 받아 re.search로 소스(s)에서 패턴(p)을 검색. 찾지 못하면 NotMatchedException이 발생
def search_from_source(p, s):
    m = re.search(p, s)
    if not m:
        raise NotMatchedException(p, s)
    return m


source_string = 'Lux, the Lady of Luminosity'
pattern_string = r'L\w{5}\b'

result = None
try:
    result = search_from_source(pattern_string, source_string)
except NotMatchedException as e:
    print(e)

print('Search result:', result)

