from tkinter import *
import tkinter.messagebox as msg
import random
from tkinter import filedialog
import os

n1 = random.randint(0, 9999999999999)
n2 = random.randint(0, 1000)

fileg = f'{str(n1) + str(n2)}.bat'


def file_clearer():
    main_folder_clear = open('Mainfoldernames.txt', 'w')
    main_folder_clear.write('')
    main_folder_clear.close()
    sub_folder_clear = open('Subfoldernames.txt', 'w')
    sub_folder_clear.write('')
    sub_folder_clear.close()


file_clearer()


def runner():
    path=filedialog.askdirectory()
    print(path)
    a = rf"{path}"
    b= a.replace("/","/\"")
    my_dir = str(b)
    os.system(f'cmd /c "Move {fileg} {my_dir}""')
    os.system(f'cmd /c "{my_dir[:2]} & cd {my_dir}" & {my_dir}"//{fileg} "')
    os.system(f'cmd /c "{my_dir[:2]} & cd {my_dir}" & del {fileg} "')

def Mainfoldersaver():
    main_file = open("Mainfoldernames.txt", "w")
    main_file.write(main_text_input.get(1.0, END))
    main_file.close()


def Subfoldersaver():
    sub_file = open("Subfoldernames.txt", "w")
    sub_file.write(sub_text_input.get(1.0, END))
    sub_file.close()


def reset():
    main_text_input.delete(1.0,END)
    sub_text_input.delete(1.0,END)
    file_clearer()

def main():
    Mainfoldersaver()
    Subfoldersaver()
    bat_file = open(str(n1) + str(n2) + '.bat', 'a')
    main_folder_out = open('Mainfoldernames.txt')
    input_reader = main_folder_out.readlines()
    for names in input_reader:
        bat_file.write('mkdir \" ')
        bat_file.write(f'{names}')
        bat_file.write('\n')
    sub_folder_out = open('Subfoldernames.txt')
    input_reader2 = sub_folder_out.readlines()
    for names in input_reader:
        bat_file.write(f'\ncd \" {names}')
        bat_file.write('\n')
        for naam in input_reader2:
            bat_file.write('mkdir \"')
            bat_file.write(str(naam))
            bat_file.write('\n')
        bat_file.write('cd..\n')
    bat_file.close()
    main_folder_out.close()
    sub_folder_out.close()
    runner()


def hlp():
    msg.showinfo('Help', '1:Give main folder names\n2:Give subfolder names\n3:Press Save button\n4:Select Folder')


root = Tk()
root.geometry('800x400')
root.maxsize(800,400)
root.minsize(800,400)
root.title('Folder maker-By Ravi sharma')
root.wm_iconbitmap("folder.ico")
frame1 = Frame(root, borderwidth=10, relief=SUNKEN, bg='skyblue')
frame1.grid(pady=20, padx=17)
frame2 = Frame(root, width=100, height=50, borderwidth=10, relief=SUNKEN, bg='skyblue')
frame2.grid(row=0, column=1, pady=5, padx=5)
scrollbar = Scrollbar(frame1)
scrollbar.grid(column=1)
scrollbar2 = Scrollbar(frame2)
scrollbar2.grid(row=2, column=1)
Label(frame1, text='Main Folder Names', bg='skyblue', fg='red').grid()
main_text_input = Text(frame1, width=30, height=5, yscrollcommand=scrollbar.set, font=' 20', bg='skyblue')
main_text_input.grid(row=0)
Label(frame2, text='Sub Folder Names', bg='skyblue', fg='red').grid()
sub_text_input = Text(frame2, width=30, height=5, yscrollcommand=scrollbar2.set, font=' 20', bg='skyblue')
sub_text_input.grid(row=2)
Button(root, text='Make folder', command=main, font='arial 30', fg='White', bg='navy').grid(row=3,column=1, pady=26)
Button(root, text='RESET', command=reset, font='arial 30', fg='White', bg='RED').grid(row=3, pady=26)
help = Menu(root)
help.add_command(label='How to use', command=hlp)
root.config(menu=help)
Label(root, text='NOTE:Do not give extra empty line after names of folder', fg='red',
      font='arial 17 bold') \
    .grid(row=5, padx=10,pady=25,columnspan=2)
root.mainloop()
