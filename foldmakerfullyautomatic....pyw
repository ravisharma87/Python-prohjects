from tkinter import *
import tkinter.messagebox as msg
import random
from tkinter.filedialog import asksaveasfilename
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


def Mainfoldersaver():
    main_file = open("Mainfoldernames.txt", "w")
    main_file.write(main_text_input.get(1.0, END))
    main_file.close()


def Subfoldersaver():
    sub_file = open("Subfoldernames.txt", "w")
    sub_file.write(sub_text_input.get(1.0, END))
    sub_file.close()

def main():

    Mainfoldersaver()
    Subfoldersaver()
    bat_file = open(str(n1) + str(n2) + '.bat', 'a')
    main_folder_out = open('Mainfoldernames.txt')
    input_reader = main_folder_out.readlines()
    for names in input_reader:
        bat_file.write('mkdir ')
        bat_file.write(names)
        bat_file.write('\n')
    sub_folder_out = open('Subfoldernames.txt')
    input_reader2 = sub_folder_out.readlines()
    for names in input_reader:
        bat_file.write(f'\ncd {names}\n')
        for naam in input_reader2:
            bat_file.write('mkdir ')
            bat_file.write(str(naam))
            bat_file.write('\n')
        bat_file.write('cd..\n')
    bat_file.close()
    main_folder_out.close()
    sub_folder_out.close()
    def runner():
        my_dir = filedialog.askdirectory()
        print(my_dir)
        b=my_dir.replace("\\", "//")
        os.system(f'cmd /c "Move {fileg} {b}"')
        os.system(f'cmd /k "{my_dir[:2]} & cd {b} & {b}//{fileg} & exit"')
        root.destroy()
    runner()
def hlp():
    msg.showinfo('Help','1:Give main folder names\n2:Give subfolder names\n3:Press Save button\n4:Select Folder')

root = Tk()
root.geometry('450x480')
root.maxsize(450, 480)
root.minsize(450, 480)
root.title('Folder maker-By Ravi sharma')
frame1 = Frame(root, width=100, height=50, borderwidth=10, relief=SUNKEN, bg='grey')
frame1.grid(pady=5, padx=5)
frame2 = Frame(root, width=100, height=50, borderwidth=10, relief=SUNKEN, bg='grey')
frame2.grid(row=2, column=0, pady=5, padx=5)
scrollbar = Scrollbar(frame1)
scrollbar.grid(column=1)
scrollbar2 = Scrollbar(frame2)
scrollbar2.grid(row=2, column=1)
Label(frame1, text='Main Folder Names', bg='grey', fg='red').grid()
main_text_input = Text(frame1, width=30, height=5, yscrollcommand=scrollbar.set, font=' 20', bg='grey')
main_text_input.grid(row=0)
Label(frame2, text='Sub Folder Names', bg='grey', fg='red').grid()
sub_text_input = Text(frame2, width=30, height=5, yscrollcommand=scrollbar2.set, font=' 20', bg='grey')
sub_text_input.grid(row=2)
Button(root, text='SAVE', command=main, font='arial 40', fg='White', bg='navy').grid(row=3,pady=26 )
help = Menu(root)
help.add_command(label='How to use', command=hlp)
root.config(menu=help)
Label(root, text='NOTE:Do not give extra empty line after names of folder', fg='red', borderwidth=5, relief=SUNKEN,
      font='arial 12 bold') \
    .grid(row=5, padx=5)
root.mainloop()
