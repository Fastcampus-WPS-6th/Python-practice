def args_count(*args):
    c = len(args)
    print(c)
    return c


result = args_count(3, 5, 2, 10, 'ABC')
print(result)

