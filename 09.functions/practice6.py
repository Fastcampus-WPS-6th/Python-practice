result_list = []
for x in range(2, 10):
    for y in range(1, 10):
        result_list.append('%d x %d = %d' % (x, y, x * y))


result_list2 = [(lambda a, b: '%d x %d = %d' % (a, b, a * b))(x, y) for x in range(2, 10) for y in range(1, 10)]
print(result_list2)

