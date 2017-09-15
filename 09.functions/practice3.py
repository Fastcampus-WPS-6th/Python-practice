def multi1(arg1, arg2=None):
    if arg2:
        return arg1 * arg2
    return arg1 ** 2


def multi2(*args):
    if len(args) > 1:
        return args[0] * args[1]
    elif len(args) == 1:
        return args[0] ** 2
    else:
        raise Exception('require arguments')

result1 = multi1(3)
result2 = multi1(3, 10)
result3 = multi2(3)
result4 = multi2(10, 50)
result5 = multi2()

print(result1)
print(result2)
print(result3)
print(result4)

