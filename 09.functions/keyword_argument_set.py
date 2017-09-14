def print_kwargs(title='untitled', **kwargs):
    print(kwargs)

print_kwargs(name='hanyeong.lee', age=30)


def print_all_args(*args, **kwargs):
    print(args)
    print(kwargs)

print_all_args('ABCD', list, age=30, name='lhy')
