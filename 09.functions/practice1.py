def what_fruit(color):
    color = color.lowercase()
    if color == 'red':
        return 'apple'
    elif color == 'yellow':
        return 'banana'
    elif color == 'green':
        return 'melon'
    else:
        return 'I don\'t know'


def what_fruit2(color):    
    fruit_color_dict = {
        'red': 'apple',
        'yellow': 'banana',
        'green': 'melon',
    }
    return fruit_color_dict.get(color, 'I don\'t know')


result = what_fruit2('red')
print(result)

