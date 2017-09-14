champion = 'Sona'

def show_global_champion():
    print('show_global_champion: {}'.format(champion))

def change_global_champion():
    champion = 'Ahri'
    print('c_locals() :', locals())
    print(globals())
    print('after change_global_champion: {}'.format(champion))


print(locals())

show_global_champion()
change_global_champion()
show_global_champion()

