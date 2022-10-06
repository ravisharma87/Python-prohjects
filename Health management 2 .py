#sort the data alphabetically
#Remove the time stamp
#delete any entry

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


def getdate():
    import datetime
    return datetime.datetime.now()


def datime():
    tida = str(getdate())
    if int(tida[11:13])>=12:
        a=tida[11:13]
        if int(a)==13:
            return (f'Date:{tida[:11]}1:{tida[14:19]} PM')
        elif int(a)==12:
            return (f'Date:{tida[:11]}12:{tida[14:19]} PM')
        elif int(a)==14:
            return (f'Date:{tida[:11]}2:{tida[14:19]} PM')
        elif int(a)==15:
            return (f'Date:{tida[:11]}3:{tida[14:19]} PM')
        elif int(a)==16:
            return (f'Date:{tida[:11]}4:{tida[14:19]} PM')
        elif int(a)==17:
            return (f'Date:{tida[:11]}5:{tida[14:19]} PM')
        elif int(a)==18:
            return (f'Date:{tida[:11]}6:{tida[14:19]} PM')
        elif int(a)==19:
            return (f'Date:{tida[:11]}7:{tida[14:19]} PM')
        elif int(a)==20:
            return (f'Date:{tida[:11]}8:{tida[14:19]} PM')
        elif int(a)==21:
            return (f'Date:{tida[:11]}9:{tida[14:19]} PM')
        elif int(a)==22:
            return (f'Date:{tida[:11]}10:{tida[14:19]} PM')
        elif int(a)==23:
            return (f'Date:{tida[:11]}11:{tida[14:19]} PM')
    else:
        return(f'Date:{tida[:11]}{tida[11:19]} AM')

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
                        file_logger.write(str(datime()))
                        file_logger.write(':-->')
                        file_logger.write(writer)
                        file_logger.write('\n')
                        file_logger.close()
                        print(fg.lightgreen + 'Added successfully', colors.reset)
                        continue
                    elif diex == 2:
                        file_logger = open(ask_name_login.capitalize() + 'diet', 'a')
                        writer = input(fg.pink + 'Type here -->' + colors.reset)
                        file_logger.write(str(datime()))
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
