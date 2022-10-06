def getdate():
    import datetime
    return datetime.datetime.now()


def time1():
    tida = str(getdate())
    if int(tida[11:13]) >= 12:
        a = tida[11:13]
        if int(a) == 13:
            return f'{tida[:11]}1:{tida[14:19]} PM'
        elif int(a) == 12:
            return f'{tida[:11]}12:{tida[14:19]} PM'
        elif int(a) == 14:
            return f'{tida[:11]}2:{tida[14:19]} PM'
        elif int(a) == 15:
            return f'{tida[:11]}3:{tida[14:19]} PM'
        elif int(a) == 16:
            return f'{tida[:11]}4:{tida[14:19]} PM'
        elif int(a) == 17:
            return f'{tida[:11]}5:{tida[14:19]} PM'
        elif int(a) == 18:
            return f'{tida[:11]}6:{tida[14:19]} PM'
        elif int(a) == 19:
            return f'{tida[:11]}7:{tida[14:19]} PM'
        elif int(a) == 20:
            return f'{tida[:11]}8:{tida[14:19]} PM'
        elif int(a) == 21:
            return f'{tida[:11]}9:{tida[14:19]} PM'
        elif int(a) == 22:
            return f'{tida[:11]}10:{tida[14:19]} PM'
        elif int(a) == 23:
            return f'{tida[:11]}11:{tida[14:19]} PM'
    else:
        return f'{tida[:11]}{tida[11:19]} AM'


def new_attendance_sheet():
    attendance_sheet_number = int(input('Sheet number:'))
    # noinspection PyBroadException
    try:
        attend_file = open('attendance' + str(attendance_sheet_number) + '.txt')
        attend_file.read()
        attend_file.close()
        print('This file already exists ')
    except:
        attend_file = open('attendance' + str(attendance_sheet_number) + '.txt', 'a')
        attend_file.write('DATE')
        attend_file.write('\t\t\t\t\tTime')
        attend_file.write('\t\t\tName')
        attend_file.write('\t\t\tAbsent/Present')
        attend_file.write('\n')
        attend_file.close()
        file_selector = open('Attendance_sheet_ holder', 'a')
        file_selector.write('attendance' + str(attendance_sheet_number) + '.txt')
        file_selector.close()
        print('~~~Sheet creation successful~~~')


def attendance_sheet_selector():
    sheet_name = input('Sheet number:')
    file_changer = open('Attendance_sheet_ holder', 'w')
    file_changer.write('attendance' + str(sheet_name) + '.txt')
    file_changer.close()


def attendance_holder():
    print('Enter your name:')
    employee_name = input()
    file1 = open('Attendance_sheet_ holder')
    reader = file1.readline()
    employee_attendance = open(reader, 'a')
    date_time = str(time1())
    employee_attendance.write(date_time[:11])
    employee_attendance.write('\t\t\t' + date_time[11:22])
    employee_attendance.write('\t\t\t' + employee_name.capitalize())
    while True:
        absent_present = input('A:Absent\tP:Present\n--->')
        if absent_present.lower() == 'a':
            employee_attendance.write('\t\t\tAbsent')
            break
        elif absent_present.lower() == 'p':
            employee_attendance.write('\t\t\tPresent')
            break
        else:
            print('Invalid input')
            continue
    employee_attendance.write('\n')
    employee_attendance.close()


def attendance_sheet_reader():
    file1 = open('Attendance_sheet_ holder')
    reader = file1.readline()
    employee_attendance_reader = open(reader)
    sheet = employee_attendance_reader.read()
    print(sheet)


def absent():
    file2 = open('Attendance_sheet_ holder')
    readfile = file2.readline()
    presence = open(readfile)
    content = presence.readlines()
    name = input('Name:')
    for i in content:
        print(i)




def main_attendance():
    print('~~~Attendance.exe~~~')
    while True:
        print('1:Make a new attendance sheet')
        print('2:Change sheet number')
        print('3:Attendance')
        print('4:Attendance sheet reader')
        print('\tType exit to exit the program')
        option_selector = input(':-->')
        if option_selector.lower() == 'exit':
            break
        elif int(option_selector) == 1:
            new_attendance_sheet()
            continue
        elif int(option_selector) == 2:
            attendance_sheet_selector()
        elif int(option_selector) == 3:
            attendance_holder()
        elif int(option_selector) == 4:
            attendance_sheet_reader()
        elif int(option_selector) == 5:
            absent()
        else:
            print('Invalid input')
            continue
main_attendance()
