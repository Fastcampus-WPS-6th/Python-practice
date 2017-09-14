import timeit

TIMES = 10000
RANGE = 1000

cmd_list = 'list(range(1000))'
cmd_comprehension = '[x for x in range(1000)]'

t1 = timeit.repeat(cmd_list, number=TIMES)
t2 = timeit.repeat(cmd_comprehension, number=TIMES)

print(t1)
print(t2)

