#cheater game
import pyttsx3
class fg:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
def cheater():
        lost=0
        while lost <= 10:
            player = input(fg.cyan + 'Choose:')
            if player == 999:
                break
            elif player == 's':
                print(fg.orange + 'Gun')
                lost = lost + 1
                continue
            elif player == 'w':
                print(fg.orange + 'Snake')
                lost = lost + 1
                continue
            elif player == 'g':
                print(fg.orange + 'Water')
                lost = lost + 1
                continue
            else:
                print(fg.red + 'Invaid input')
                continue
        print(fg.cyan + 'Please wait', fg.yellow + '⏳')
        time.sleep(5)
        print(fg.green + 'Loading results...')
        time.sleep(5)
        print(fg.pink + 'Computer won the game...')
        time.sleep(2)
        print(fg.red + 'NOOB hahahaha')
        book_text = ['Noob hahahahahahahahahaha']
        engine = pyttsx3.init()
        for i in book_text:
            engine.say(i)
            engine.runAndWait()
def rps():
    won = 0
    lose = 0
    draw = 0
    a = 0
    while a < 10:
        ranswg = random.randint(1, 3)
        try:
            player = input(fg.cyan+'Choose:')
            if player == 's' and ranswg == 2:
                if ranswg == 1:
                    print(fg.orange+'SNAKE')
                elif ranswg == 2:
                    print(fg.orange+'WATER')
                else:
                    print(fg.orange+'GUN')
                won = won + 1
                a = a + 1
                continue
            elif player == 'w' and ranswg == 3:
                if ranswg == 1:
                    print(fg.orange+'SNAKE')
                elif ranswg == 2:
                    print(fg.orange+'WATER')
                else:
                    print(fg.orange+'GUN')
                won = won + 1
                a = a + 1
                continue
            elif player == 'g' and ranswg == 1:
                if ranswg == 1:
                    print(fg.orange+'SNAKE')
                elif ranswg == 2:
                    print(fg.orange+'WATER')
                else:
                    print(fg.orange+'GUN')
                won = won + 1
                a = a + 1
                continue
            elif player == 's' and ranswg == 1:
                if ranswg == 1:
                    print(fg.orange+'SNAKE')
                elif ranswg == 2:
                    print(fg.orange+'WATER')
                else:
                    print(fg.orange+'GUN')
                draw = draw + 1
                a = a + 1
                continue
            elif player == 'w' and ranswg == 2:
                if ranswg == 1:
                    print(fg.orange+'SNAKE')
                elif ranswg == 2:
                    print(fg.orange+'WATER')
                else:
                    print(fg.orange+'GUN')
                draw = draw + 1
                a = a + 1
                continue
            elif player == 'g' and ranswg == 3:
                if ranswg == 1:
                    print(fg.orange+'SNAKE')
                elif ranswg == 2:
                    print(fg.orange+'WATER')
                else:
                    print(fg.orange+'GUN')
                draw = draw + 1
                a = a + 1
                continue
            elif player == 'g' and ranswg == 2:
                if ranswg == 1:
                    print(fg.orange+'SNAKE')
                elif ranswg == 2:
                    print(fg.orange+'WATER')
                else:
                    print(fg.orange+'GUN')
                lose = lose + 1
                a = a + 1
                continue
            elif player == 'w' and ranswg == 1:
                if ranswg == 1:
                    print(fg.orange+'SNAKE')
                elif ranswg == 2:
                    print(fg.orange+'WATER')
                else:
                    print(fg.orange+'GUN')
                lose = lose + 1
                a = a + 1
                continue
            elif player == 's' and ranswg == 3:
                if ranswg == 1:
                    print(fg.orange+'SNAKE')
                elif ranswg == 2:
                    print(fg.orange+'WATER')
                else:
                    print(fg.orange+'GUN')
                lose = lose + 1
                a = a + 1
                continue
            elif player != 'r' or player != 'p' or player != 's':
                print("inavlid input")
                continue
        except:
            print('Invalid input')
            continue
    print(fg.cyan + 'Please wait', fg.yellow + '⏳')
    time.sleep(5)
    print(fg.green + 'Loading results...')
    time.sleep(5)
    if won > lose:
        print('~~WON~~')
    elif won < lose:
        print('~~LOST~~')
    else:
        print('~~DRAW~~')
import random
import time
print(fg.blue+ 'w:Water\ng:Gun\ns:Snake')
randm = random.randint(1, 2)
if randm == 2:
    cheater()
elif randm==1:
    rps()
