# I have tried making a little type of phone which contain 10 programs
import time


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


def swg():
    import random
    won = 0
    lose = 0
    draw = 0
    a = 0
    print(fg.red + 'THE ~~SWG~~ GAME' + colors.reset)
    while a < 10:
        ranswg = random.randint(1, 3)
        try:
            print(fg.green + "Choose your option:\ns=snake\nw=water\ng=gun ")
            player = input('-->')
            if player == '999':
                break
            elif player == 's' and ranswg == 2:
                if ranswg == 1:
                    print(fg.cyan + 'SNAKE')
                elif ranswg == 2:
                    print(fg.cyan + 'WATER')
                else:
                    print(fg.cyan + 'GUN')
                won = won + 1
                a = a + 1
                continue
            elif player == 'w' and ranswg == 3:
                if ranswg == 1:
                    print(fg.cyan + 'SNAKE')
                elif ranswg == 2:
                    print(fg.cyan + 'WATER')
                else:
                    print(fg.cyan + 'GUN')
                won = won + 1
                a = a + 1
                continue
            elif player == 'g' and ranswg == 1:
                if ranswg == 1:
                    print(fg.cyan + 'SNAKE')
                elif ranswg == 2:
                    print(fg.cyan + 'WATER')
                else:
                    print(fg.cyan + 'GUN')
                won = won + 1
                a = a + 1
                continue
            elif player == 's' and ranswg == 1:
                if ranswg == 1:
                    print(fg.cyan + 'SNAKE')
                elif ranswg == 2:
                    print(fg.cyan + 'WATER')
                else:
                    print(fg.cyan + 'GUN')
                draw = draw + 1
                a = a + 1
                continue
            elif player == 'w' and ranswg == 2:
                if ranswg == 1:
                    print(fg.cyan + 'SNAKE')
                elif ranswg == 2:
                    print(fg.cyan + 'WATER')
                else:
                    print(fg.cyan + 'GUN')
                draw = draw + 1
                a = a + 1
                continue
            elif player == 'g' and ranswg == 3:
                if ranswg == 1:
                    print(fg.cyan + 'SNAKE')
                elif ranswg == 2:
                    print(fg.cyan + 'WATER')
                else:
                    print(fg.cyan + 'GUN')
                draw = draw + 1
                a = a + 1
                continue
            elif player == 'g' and ranswg == 2:
                if ranswg == 1:
                    print(fg.cyan + 'SNAKE')
                elif ranswg == 2:
                    print(fg.cyan + 'WATER')
                else:
                    print(fg.cyan + 'GUN')
                lose = lose + 1
                a = a + 1
                continue
            elif player == 'w' and ranswg == 1:
                if ranswg == 1:
                    print(fg.cyan + 'SNAKE')
                elif ranswg == 2:
                    print(fg.cyan + 'WATER')
                else:
                    print(fg.cyan + 'GUN')
                lose = lose + 1
                a = a + 1
                continue
            elif player == 's' and ranswg == 3:
                if ranswg == 1:
                    print(fg.cyan + 'SNAKE')
                elif ranswg == 2:
                    print(fg.cyan + 'WATER')
                else:
                    print(fg.cyan + 'GUN')
                lose = lose + 1
                a = a + 1
                continue
            elif player != 's' or player != 'w' or player != 'g':
                print("inavlid input")
                continue
        except:
            print('Invalid input')
            continue
    print(fg.blue + 'Number of rounds won:', fg.pink + str(won))
    print(fg.blue + 'Number of rounds lost:', fg.pink + str(lose))
    print(fg.blue + 'Number of rounds draw:', fg.pink + str(draw))
    if won > lose:
        print(fg.red + '~~WON~~', colors.reset)
    elif won < lose:
        print(fg.red + '~~LOST~~')
    else:
        print(fg.red + '~~DRAW~~')
    print(colors.reset)


def gatedate():
    import datetime
    return datetime.datetime.now()


def datime():
    tida = str(gatedate())
    if int(tida[11:13]) >= 12:
        a = tida[11:13]
        if int(a) == 13:
            print('Date:', tida[:11])
            print('1:' + tida[14:19] + ' PM')
        elif int(a) == 12:
            print('Date:', tida[:11])
            print('Time:', tida[11:19] + ' AM')
        elif int(a) == 14:
            print('Date:', tida[:11])
            print('2:' + tida[14:19] + ' PM')
        elif int(a) == 15:
            print('Date:', tida[:11])
            print('3:' + tida[14:19] + ' PM')
        elif int(a) == 16:
            print('Date:', tida[:11])
            print('4:' + tida[14:19] + ' PM')
        elif int(a) == 17:
            print('Date:', tida[:11])
            print('5:' + tida[14:19] + ' PM')
        elif int(a) == 18:
            print('Date:', tida[:11])
            print('6:' + tida[14:19] + ' PM')
        elif int(a) == 19:
            print('Date:', tida[:11])
            print('7:' + tida[14:19] + ' PM')
        elif int(a) == 20:
            print('Date:', tida[:11])
            print('8:' + tida[14:19] + ' PM')
        elif int(a) == 21:
            print('Date:', tida[:11])
            print('9:' + tida[14:19] + ' PM')
        elif int(a) == 22:
            print('Date:', tida[:11])
            print('10:' + tida[14:19] + ' PM')
        elif int(a) == 23:
            print('Date:', tida[:11])
            print('11:' + tida[14:19] + ' PM')
    else:
        print('Date:', tida[:11])
        print('Time:', tida[11:19] + ' AM')


def textmanager():
    while True:
        # noinspection PyBroadException
        try:
            starter = int(input(fg.blue + '1:Start\n2:Exit' + colors.reset))
            if starter == 1:
                while True:
                    print(fg.green + '1:New file\n2:Read file\n3:Add something to file',
                          '\n4:Format file\n', fg.red + '5:exit', colors.reset)
                    option = int(input('~~}'))
                    if option == 1:
                        print(fg.cyan + 'Create a new file ')
                        new_file = input('name~')
                        file1 = open(new_file, 'a')
                        file1.write('')
                        file1.close()
                        print(fg.lightred + '~~~FILE CREATED~~~', colors.reset)
                        continue
                    elif option == 2:
                        filereader = input(fg.cyan + 'Input file name:')
                        print(fg.pink)
                        file2 = open(filereader)
                        content = file2.read()
                        print(content, colors.reset)
                        file2.close()
                        continue
                    elif option == 3:
                        filewriter = input(fg.cyan + 'Input file name:' + colors.reset)
                        while True:
                            file3 = open(filewriter, 'a')
                            writer = input(fg.red + 'Write here:')
                            file3.write(writer)
                            file3.write('\n')
                            more = int(input(fg.blue + 'Wanna add more?\n1:yes\n2:no' + colors.reset))
                            if more == 1:
                                continue
                            elif more == 2:
                                file3.close()
                                print(fg.red + bg.black + '~~~FILE SAVED AND CLOSED~~~', colors.reset)
                                break
                            else:
                                print(fg.red + 'invalid input' + colors.reset)
                                break
                    elif option == 4:
                        fileformattor = input(fg.cyan + 'Input file name:')
                        file4 = open(fileformattor, 'w')
                        file4.write('')
                        file4.close()
                        print(fg.red + '~~~FILE FORMATTED~~~', colors.reset)
                        continue
                    else:
                        break
            elif starter == 2:
                break
            else:
                print(fg.red + 'Invalid input', colors.reset)
                continue
        except Exception as error:
            print(fg.red + 'Invalid input', colors.reset)
            continue


def health_management():
    def getdate():
        import datetime
        return datetime.datetime.now()

    def signup():
        ask_name_sign = input(fg.cyan + 'Enter your name:')
        file1 = open(ask_name_sign.capitalize() + 'ex', 'a')
        file2 = open(ask_name_sign.capitalize() + 'diet', 'a')
        filepass = open(ask_name_sign.capitalize() + 'pass', 'a')
        file1.write('')
        file2.write('')
        newpassword = input(fg.red + 'Create a password:')
        filepass.write(newpassword)
        file1.close()
        file2.close()
        filepass.close()
        print(fg.red + 'Account created successfully', colors.reset)

    # noinspection PyBroadException
    def login():
        ask_name_login = input(fg.cyan + 'Name:')
        while True:
            try:
                passwordc = input(fg.red + 'Password:')
                passfile = open(ask_name_login.capitalize() + 'pass')
                passwd = passfile.read()
                if passwordc == passwd:
                    print(fg.red + 'Press 999 to go to previous page')
                    print(fg.green + 'what do you want to do?\n1:Log data\n2:Retrieve data', colors.reset)
                    data_do = int(input('-->'))

                    if data_do == 1:
                        print(fg.blue + 'LOG DATA')
                        print(fg.lightgreen + '1:Exercise\n2:Diet')
                        diex = int(input('-->'))
                        if diex == 1:
                            file_logger = open(ask_name_login.capitalize() + 'ex', 'a')
                            writer = input(fg.pink + 'Type here -->' + colors.reset)
                            file_logger.write(str(getdate()))
                            file_logger.write(':-->')
                            file_logger.write(writer)
                            file_logger.write('\n')
                            file_logger.close()
                            print(fg.lightgreen + 'Added successfully', colors.reset)
                            continue
                        elif diex == 2:
                            file_logger = open(ask_name_login.capitalize() + 'diet', 'a')
                            writer = input(fg.pink + 'Type here -->' + colors.reset)
                            file_logger.write(str(getdate()))
                            file_logger.write(':-->')
                            file_logger.write(writer)
                            file_logger.write('\n')
                            file_logger.close()
                            print(fg.lightgreen + 'Added successfully', colors.reset)
                            continue
                        elif diex == 999:
                            break
                        else:
                            print(fg.red + 'Invalid Input', colors.reset)
                            continue
                    elif data_do == 2:
                        print(fg.blue + 'RETRIEVE DATA')
                        print(fg.lightgreen + '1:Exercise\n2:Diet')
                        diex2 = int(input('-->'))
                        if diex2 == 1:
                            file_logger = open(ask_name_login.capitalize() + 'ex')
                            content = file_logger.read()
                            print(fg.pink + content, colors.reset)
                            continue
                        elif diex2 == 2:
                            file_logger = open(ask_name_login.capitalize() + 'diet')
                            content = file_logger.read()
                            print(fg.pink + content, colors.reset)
                            continue
                        elif diex2 == 999:
                            break
                        else:
                            print(fg.red + 'Invalid Input', colors.reset)
                            continue
                    elif data_do == 999:
                        break
                    else:
                        print(fg.red + 'Invalid Input', colors.reset)
                        continue
                else:
                    print(fg.red + 'Invalid Input', colors.reset)
                    break

            except Exception as Error1:
                print(fg.red + 'Invalid Input', colors.reset)
                break

    def main2():
        """If input is given = Owner password is required to access owner
            On giving input = 1 you will be redirected to signup page and
            On giving input = 2 you will be redirected to login page... """
        print(fg.black + bg.red + '~~~WELCOME TO HEALTH MANAGEMENT SERVICES~~~', colors.reset)

        while True:
            print(fg.red + 'To exit program or go to previous page press 999...')
            print(fg.cyan + '1:Sign up\n2:Log in')
            print(fg.red + bg.black + '\t777:Help', colors.reset)
            # noinspection PyBroadException
            silo = input('-->')
            try:
                if silo == 'owner' or silo == 'Owner' or silo == 'OWNER':
                    passwd = int(input(fg.red + 'password' + colors.reset + '-->'))
                    if passwd == 1234:
                        login()
                        continue
                    else:
                        print(fg.red + 'Permission denied', colors.reset)
                        continue
                elif int(silo) == 1:
                    signup()
                    continue
                elif int(silo) == 2:
                    login()
                    continue

                elif int(silo) == 777:
                    print(main2.__doc__)
                    continue
                elif int(silo) == 999:
                    break
                else:
                    print(fg.red + 'Invalid input' + colors.reset)
                    continue
            except Exception as error:
                print(fg.red + 'Invalid input' + colors.reset)
                print(colors.invisible + str(error) + colors.reset)
                continue

    main2()


def licence():
    while True:
        a = 18
        print(colors.bold + fg.green + "Kya aapka license ban chuka :\n",
              colors.reset + fg.yellow + "1:haa ke liye 1 dabaye\n", "2:nhi ke liye 0 dabaye",
              fg.red + '\n\tExit karne ke liye inke alwa kuch dabaye')
        c = int(input())
        if c == 1:
            print(fg.red + "Ye programe aapke liye nhi h", colors.reset)
            break
        elif c > 1:
            print(fg.lightred + 'Exiting program', colors.reset)
            break
        else:
            print(fg.blue + "Enter your  age:\n")
            b = int(input())
            if a == b:
                print(fg.lightblue + "Sir ji aapki age valid h license bnavane ke liye ")
            elif a > b:
                print("Tum chhote ho abhi\n", "Tum ", int(a) - int(b), "saal baad aana")
            else:
                print("bhaishaab aapne abhi tak lisence nhi banvaya. Jaldi karo thodha", colors.reset)
            continue


def game():
    c = 10

    print(colors.bold + fg.green + 'Basically you have to guess the number')

    print(colors.reset + fg.cyan + '~~~LEVEL-1~~~', '\n9 CHANCES')
    print(fg.yellow + 'Number is between 1 to 30', colors.reset)
    x = int(input(fg.blue + '1:Start \n2:Exit\n-:}'))
    while c > 0:

        if x == 1:
            if c > 1:

                print(fg.blue + fg.yellow + 'Number of chances left:', c - 1)
                b = int(input('~~~'))
                if b == 17:
                    print(colors.bold + colors.underline + fg.purple + bg.black + "YOU WON", colors.reset)
                    print(colors.reset + fg.cyan + '~~~LEVEL-2~~~', '\n7 CHANCES')
                    d = 8
                    print(fg.yellow + 'Number is between 1 to 50', colors.reset)
                    z = int(input(fg.blue + '1:Start \n2:Exit\n-:}'))
                    if z == 1:
                        while (d > 0):

                            if d > 1:

                                print(fg.blue + fg.yellow + 'Number of chances left:', d - 1)
                                f = int(input('~~~'))
                                if f == 29:
                                    print(colors.bold + colors.underline + fg.purple + bg.black + "YOU WON",
                                          colors.reset)
                                    print(colors.reset + fg.cyan + '~~~LEVEL-3~~~', '\n5 CHANCES')
                                    j = 6
                                    print(fg.yellow + 'Number is between 1 to 100', colors.reset)
                                    y = int(input(fg.blue + '1:Start\n2:Exit\n-:}'))
                                    if y == 1:
                                        while (j > 0):
                                            if j > 1:

                                                print(fg.blue + fg.yellow + 'Number of chances left:', j - 1)
                                                k = int(input('~~~'))
                                                if k == 67:
                                                    print(
                                                        colors.bold + colors.underline + fg.purple + bg.black + "YOU ",
                                                        "WON",
                                                        colors.reset)
                                                    break
                                                elif k <= 60:
                                                    j = j - 1
                                                    print("dur h abhi aap")
                                                elif 67 > k > 60:
                                                    j = j - 1
                                                    print('bhut pass h aap')
                                                elif k >= 76:
                                                    j = j - 1
                                                    print("dur h abhi aap")
                                                elif k < 76:
                                                    j = j - 1
                                                    print("bhut pass h aap")
                                                continue
                                            else:
                                                print(colors.underline + fg.red + colors.reverse + ' YOU LOST ',
                                                      colors.reset)
                                                print(bg.green + '~~~GAME OVER~~~', colors.reset)
                                                break
                                        break
                                    elif y == 2:
                                        break
                                    else:
                                        continue

                                elif f <= 24:
                                    d = d - 1
                                    print("dur h abhi aap")
                                elif 29 > f > 24:
                                    d = d - 1
                                    print('bhut pass h aap')
                                elif f >= 33:
                                    d = d - 1
                                    print("dur h abhi aap")
                                elif f < 33:
                                    d = d - 1
                                    print("bhut pass h aap")
                                continue
                            else:
                                print(colors.underline + fg.red + colors.reverse + ' YOU LOST ', colors.reset)
                                print(bg.green + '~~~GAME OVER~~~', colors.reset)

                                break
                        break



                    elif z == 2:
                        break
                    else:
                        continue

                elif b <= 14:
                    c = c - 1
                    print("dur h abhi aap")
                elif 17 > b > 14:
                    c = c - 1
                    print('bhut pass h aap')
                elif b >= 20:
                    c = c - 1
                    print("dur h abhi aap")
                elif b < 20:
                    c = c - 1
                    print("bhut pass h aap")
                continue

            else:
                print(colors.underline + fg.red + colors.reverse + ' YOU LOST ', colors.reset)
                print(bg.green + '~~~GAME OVER~~~', colors.reset)
                break
        elif x == 2:
            break
        else:
            continue
    print(colors.reset)


# noinspection PyBroadException
def office():
    Employee_info = {"raman": ["~designer~", "~DOB:12/3/1997~", "~JOINED ON 26MARCH2020~"],
                     'ram': ['~editor~', "~DOB:1/2/1995~", '~JOINED ON 3JAN2020~ '],
                     'shyaam': ['~editor~', '~DOB:4/5/2000~', '~JOINED ON 12FEB2020~'],
                     'raju': ['~VFX professional~', '~DOB:24/6/1998~', '~JOINED ON 19MAY2020~'],
                     'harry': ['~Python professional~', '~DOB:15/8/1999~', '~JOINED ON 16JAN2020~'],
                     'larry': ['~manager~', '~DOB:7/12/1996~', '~JOINED ON 1JAN2019~'],
                     'sherry': ['~~OWNER~~', '~DOB:18/11/1994~', '~STARTED THE COMPANY~ ']}
    list_of_employee = [['raman', 'yes'], ['ram', 'no'], ['shyaam', 'no'], ['raju', 'yes'], ['harry', 'yes'],
                        ['larry', 'no'], ['sherry', 'yes']]

    while True:
        print(colors.bold + fg.green + 'What do you need to know:\n', '1:Employee\'s information\n'
              , '2:Other things\n', '3:press any other key to cancel\n~~~:', colors.reset)
        try:
            d = int(input())
            if d == 1:
                e = input(fg.cyan + "Enter name of employee:")
                print(colors.reset)
                try:
                    for c in Employee_info[e]:
                        print(fg.lightred + c, colors.reset)
                except:
                    print(fg.red + '\t~~Name is not available in list~~', colors.reset)
                    continue
            elif d == 2:
                while True:
                    print(fg.blue)

                    a = int(input(
                        'what do you want know:\n1:Number of employees\n2:List of employees\n3:Work done list\n4:Work '
                        'not done list\nChoose your option:\nPRESS 5 TO RETURN TO PREVIOUS PAGE:'))
                    print(colors.reset)
                    if a > 4:
                        break
                    elif a == 1:
                        print(bg.blue + fg.black + str(len(list_of_employee)), colors.reset)

                    else:
                        for b, c in list_of_employee:
                            if a == 2:
                                print(colors.underline + fg.pink + b, colors.reset)
                            elif a == 3 and c == 'yes':
                                print(fg.cyan + 'User:', colors.underline + fg.pink + b, colors.reset)
                            elif a == 4 and c == 'no':

                                print(fg.cyan + 'User:', colors.underline + fg.pink + b, colors.reset)
                            else:
                                continue
                continue
            else:
                break
        except Exception as error1:
            print(error1)

            print(fg.red + '!!!Given input isn\'t numerical!!!', colors.reset)


def calculator():
    print(fg.blue + 'To exit type ', colors.bold + fg.red + '(exit)', fg.blue + ' in operator segment ')
    print(colors.reset)
    while (True):
        a = input(fg.cyan + '1st Number:\t')
        b = input(fg.lightgreen + '2nd Number:\t')
        c = input(fg.black + 'operator:\t')
        print(colors.reset)
        if a.isnumeric() == False or b.isnumeric() == False:
            print(fg.red + 'Invalid input try again', colors.reset)
        elif c == '+':
            print('sum:', colors.bold + fg.pink + str(int(a) + int(b)), colors.reset)
        elif c == '-':
            print('Subtract:', colors.bold + fg.pink + str(int(a) - int(b)), colors.reset)
        elif c == '*':
            print('Multiplication:', colors.bold + fg.pink + str(int(a) * int(b)), colors.reset)
        elif c == '/':
            print('Division:', colors.bold + fg.pink + str(int(a) / int(b)), colors.reset)
        elif c == '**':
            print('Raised to the power', fg.lightblue + str(b), colors.reset + ':',
                  colors.bold + fg.pink + str(int(a) ** int(b)), colors.reset)
        elif c == 'exit':
            break

        else:
            print(fg.red + 'Invalid input', colors.reset)
            continue


def astrologer():
    while (True):
        x = int(input(fg.blue + '1:Start\n2:Exit\n:~~'))
        print(colors.reset)
        try:
            if x == 1:
                c = 1
                a = input(fg.cyan + 'yes/no:')
                print(colors.reset)
                b = int(input(fg.orange + 'Enter number:'))
                print(colors.reset)

                while (b > 0):
                    try:
                        if c <= b and a == 'yes':
                            print(c * (fg.red + '*'), colors.reset)
                            c = c + 1
                        elif c <= b and a == 'no':
                            print((b) * (fg.green + '*'), colors.reset)
                            b = b - 1
                        else:
                            break
                    except:
                        print(fg.red + 'Inavlid Input', colors.reset)
                        break


            elif x == 2:
                break
            else:
                print(fg.red + 'Invalid input', colors.reset)
        except:
            print(fg.red + 'Inavlid input', colors.reset)
            continue


def hackedpic():
    print(
        bg.black + fg.red + '⣀⣀⣀⣀⣀⣀⣀⡀⠀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣤⣄⣀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⣤⣀⣀⣀⣀⣀⣀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀')
    print('⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣸⣿⣿⣿⣿⣿⣿⡏⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀')
    print('⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⢀⣿⣿⣿⣿⣿⣿⡿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆')
    print('⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡏⠀⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣿⠇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠇⠀⣿⣿⣿⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⢡⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣧⣀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣾⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢨⣿⣿⣿⣿⣿⣿⡇⠘⣿⣿⣿⣿⣿⣿⣇⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣸⣿⣿⣿⣿⣿⣿⣧⣤⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢀⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣧⠀⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠘⣿⣿⣿⣿⣿⣿⣿⡇⠀⣸⣿⣿⣿⣿⣿⣿⣏⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣿⣿⣿⣿⣿⣧⠀⠀⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣀⣀⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⡏⠉⢻⣿⣿⣿⣿⣿⣿⣷⠀⢻⣿⣿⣿⣿⣿⣿⣷⣴⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⡄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟')
    print('⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⠁⠀⢺⣿⣿⣿⣿⣿⣿⣿⡀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣷⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃')
    print('⠿⠿⠿⠿⠿⠿⠿⠇⠀⠿⠿⠿⠿⠿⠿⠿⠇⠾⠿⠿⠿⠿⠿⠿⠿⠀⠀⠸⠿⠿⠿⠿⠿⠿⠿⠇⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠿⠿⠿⠿⠿⠿⠿⠇⠀⠸⠿⠿⠿⠿⠿⠿⠿⠇⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠋⠁⠀')
    print(colors.reset)


def magic():
    '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    '\033[36m'
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
    time.sleep(2)
    print(red + 'Hacking....')
    while True:
        time.sleep(10)
        print(red + 'HACKED')
        time.sleep(3)
        b = 0
        while b < 10000000000000:

            if 1000 < b < 100000:
                print(red + '-----------------Error-----------------')
                print(
                    red + 'Traceback (most recent call last):\n\tFile\"',
                    fg.blue + 'C:\\Users\\PycharmProjects\\pythonProject\",',
                    fg.red + 'line infinity, in <module>\n\t\tHACKED\nValueError: invalid literal for working')

            elif b >= 100000:
                time.sleep(5)
                hackedpic()
                break
            b = b + 1 / 2
        break


def main():
    while (True):
        print(colors.bold + colors.underline + fg.purple + '-:}PHONE{:-', colors.reset)
        print(fg.cyan + '1:Game\n2:Office\n3:Calculator\n4:Astrologer\n5:Magic\n6:Licence\n7:Health Management',
              '\n8:Text file manager\n9:Date N Time\n10:Snake Water Gun Game', colors.reset)
        print(fg.black + bg.lightgrey + '\tType 999 to exit', colors.reset)

        try:
            m = int(input())
            if m == 1:
                print(colors.bold + fg.red + bg.green + '~~~GAME~~~', colors.reset)
                game()
                print(colors.reset + '')
            elif m == 2:
                print(colors.bold + fg.red + bg.green + '~~~OFFICE~~~', colors.reset)
                office()
            elif m == 3:
                print(colors.bold + fg.red + bg.green + '~~~CALCULATOR~~~', colors.reset)
                calculator()
            elif m == 4:
                print(colors.bold + fg.red + bg.green + '~~~ASTROLOGER~~~', colors.reset)
                astrologer()
            elif m == 5:
                print(colors.bold + fg.red + bg.green + '~~~MAGIC~~~', colors.reset)
                magic()
            elif m == 6:
                print(colors.bold + fg.red + bg.green + '~~~LICENCE~~~', colors.reset)
                licence()
            elif m == 7:
                print(colors.bold + fg.red + bg.green + '~~~HEALTH MANAGEMENT~~~', colors.reset)
                health_management()
            elif m == 8:
                print(colors.bold + fg.red + bg.green + '~~~}TEXT FILE MANAGER{~~~', colors.reset)
                textmanager()
            elif m == 9:
                print(colors.bold + fg.red + bg.green + '~~~}DATE N TIME{~~~', colors.reset)
                datime()
            elif m == 10:
                print(colors.bold + fg.red + bg.green + '~~~}SNAKE WATER GUN GAME{~~~', colors.reset)
                swg()

            elif m == 999:
                break
            else:
                print(fg.red + 'invalid input', colors.reset)
                continue
        except Exception as error:
            print(fg.red + '\t!!!Given input isn\'t numerical!!!')
            print(colors.reset)
            continue


main()
