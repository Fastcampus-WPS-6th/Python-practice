def print_args(*args):
    print(args)

print_args('a')

print_args('a', 'b', 'c', 'd')
print_args(print_args, list)

