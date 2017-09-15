sample = [9, 1, 6, 8, 4, 3, 2, 0, 5, 7]

# 테스트로 첫 번째 루프만 실행
def selection_sort(seq):
    seq = seq.copy()
    # 정렬할 리스트의 길이
    seq_len = len(seq)

    # 최소값과 최소값의 index변수
    min_value = seq[0]
    min_index = 0

    # 전체 리스트를 순회하며 최소값을 판단
    for i in range(seq_len):
        cur_item = sample[i]
        print('Index[%d], value[%d]' % (i, cur_item))
        # 만약 현재요소가 min_value보다 작다면
        if cur_item < min_value:
            min_value = cur_item
            min_index = i
            print('Index[%d]는 현재 min_value(%s)보다 작음' % (i, min_value))
            print(' 변경된 min_value: %d' % min_value)
            print(' 변경된 min_index: %d' % min_index)

    # 한 번의 순회 후 min_index와 맨 앞의 요소를 치환
    seq[0], seq[min_index] = seq[min_index], seq[0]

    return seq

def selection_sort(seq):
    seq = seq.copy()
    # for문을 전체 아이템수-1번만큼 순회하며, 각 순회마다 index값을 증가시키며 seq[index] 부터 끝까지의 리스트를 출력하도록 작성
    # example:
    #   [9, 1, 6, 8, 4, 3, 2, 0, 5, 7]
    #   [1, 6, 8, 4, 3, 2, 0, 5, 7]
    #   [6, 8, 4, 3, 2, 0, 5, 7]
    #   [8, 4, 3, 2, 0, 5, 7]
    #   [4, 3, 2, 0, 5, 7]
    #   ...
    seq_len = len(seq)
    
    # 0부터 전체갯수-1 만큼 i값을 증가시키며 순회
    for i in range(seq_len - 1):
        print('Loop[%d], Current list: %s' % (i, seq))
        min_index = i
        min_value = seq[i]
        print( 'Loop[%d]의 min_index: %d, min_value: %d' % (i, min_index, min_value))

        for j in range(i, seq_len):
            if seq[j] < min_value:
                print(' Index[%d](%d)는 현재 min_value(%d)보다 작음.' % (j, seq[j], min_value))
                min_index = j
                min_value = seq[min_index]
        
        if i == min_index:
            print('  바꿀내용이 없음')
        else:
            print('  Index[%d]와 Index[%d]를 교체' % (i, min_index))
            seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq


result = selection_sort(sample)
print('Start  :', sample)
print('Result :', result)

