def return_list(value, result=[]):
    result.append(value)
    return result

l1 = return_list('apple')
print(l1)
l2 = return_list('banana')
print(l2)


def return_list2(value, result=None):
    print(value, result)

return_list2('apple')
return_list2('banana')
return_list2('melon', [])

