def sequential_search(s, key):
    index = 0
    while index < len(s):
        cur_char = s[index]
        if cur_char == key:
            return index
        index += 1
    return -1

def sequential_search_for(s, key):
    for index, char in enumerate(s):
        if char == key:
            return index
    return -1


search_char = 'z'
result = sequential_search('League of legends', search_char)
print('Char(%s) search result: %s' % (search_char, result))

