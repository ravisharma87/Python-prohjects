import time
import pyttsx3

class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'


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


class bg:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'
def magic():
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
    lightcyan = '\033[96m'
    c = 0
    print(green + '~~~~~~~~~~~~MAGIC~~~~~~~~~~~~~')
    print(blue + 'Hello my friend enter any number:')
    a = int(input())
    print(fg.cyan+'Loading...')
    time.sleep(5)
    print(colors.strikethrough+fg.red+'Loading...',colors.reset)
    book_text = ['Alert..........Someone is trying to breach in system..']
    engine = pyttsx3.init()
    for i in book_text:
        engine.say(i)
        engine.runAndWait()
    time.sleep(3)
    print(red + 'Hacking....')
    book_text = ['System process interrupted....']
    engine = pyttsx3.init()
    for i in book_text:
        engine.say(i)
        engine.runAndWait()
    while True:
            time.sleep(6)
            book_text = ['Admin access is breached...Trying to lock the data........................Data locking permission denied...']
            engine = pyttsx3.init()
            for i in book_text:
                engine.say(i)
                engine.runAndWait()
            print(red + 'HACKED')
            book_text = ['System shutdown process starting.........System will shutdown in ......... Three......two......one.........System shutdown process cancelled']
            engine = pyttsx3.init()
            for i in book_text:
                engine.say(i)
                engine.runAndWait()
            print(red+'Error occurred while shutting down system')
            time.sleep(3)
            book_text = ['Try shutting down system manually...']
            engine = pyttsx3.init()
            for i in book_text:
                engine.say(i)
                engine.runAndWait()
            print(red+'Voice control is locked')
            book_text = ['System lost control over Steve...']
            engine = pyttsx3.init()
            for i in book_text:
                engine.say(i)
                engine.runAndWait()
            time.sleep(2)
            book_text = ['Hey there....I am Rain Mutt.....Your system is under my control.....I am installing some good thing in you system.....']
            engine = pyttsx3.init()
            for i in book_text:
                engine.say(i)
                engine.runAndWait()
            time.sleep(2)
            book_text = ['Keyboard n mouse are locked.......Installing process starting.....']
            engine = pyttsx3.init()
            for i in book_text:
                engine.say(i)
                engine.runAndWait()
            print(red+'Installing trojan...')
            time.sleep(3)
            print(red+'Trojan installed')
            print(red+'Transferring data....')
            book_text = ['Transferring data....']
            engine = pyttsx3.init()
            for i in book_text:
                engine.say(i)
                engine.runAndWait()
            time.sleep(5)
            print(red+'Data transferred successfully...')
            book_text = ['Data transferred successfully....']
            engine = pyttsx3.init()
            for i in book_text:
                engine.say(i)
                engine.runAndWait()
            time.sleep(3)
            print(red+'System locked...')
            book_text = ['System locked....']
            engine = pyttsx3.init()
            for i in book_text:
                engine.say(i)
                engine.runAndWait()
            break
magic()