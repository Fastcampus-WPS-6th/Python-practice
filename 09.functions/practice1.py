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
    """
    color매개변수로 색상의 문자열값을 받아 해당하는 과일명의 문자열을 리턴
    찾을 수 없을 경우 'I don't know'문자열을 리턴한다
    """
    fruit_color_dict = {
        'red': 'apple',
        'yellow': 'banana',
        'green': 'melon',
    }
    return fruit_color_dict.get(color, 'I don\'t know')


result = what_fruit2('red')
print(result)

