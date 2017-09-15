#from functions.game import play_game
#from functions.shop import buy_item
#import functions
from functions import play_game, buy_item, abc
from friends.chat import send_message

def turn_on():
    print('= Turn on game =')

    while True:
        choice = input('뭐할래요\n 1: 상점, 2: 게임하기, 3: 친구에게 메시지 전송, 0: 나가기\n   선택 : ')
        if choice == '0':
            break
        elif choice == '1':
            buy_item()
        elif choice == '2':
            play_game()
        elif choice == '3':
            send_message()
        else:
            print('있는번호로 선택하세요')
        print('--------')

    print('= Turn off game =')

if __name__ == '__main__':
    turn_on()

