from tkinter import *
import tkinter.messagebox as msg
import random
import os

n1 = random.randint(0, 9999999999999)
n2 = random.randint(0, 1000)


def file_clearer():
    main_folder_clear = open('Mainfoldernames.txt', 'w')
    main_folder_clear.write('')
    main_folder_clear.close()
    sub_folder_clear = open('Subfoldernames.txt', 'w')
    sub_folder_clear.write('')
    sub_folder_clear.close()


file_clearer()


def Maker():
    root.destroy()
    fileg = f'{str(n1) + str(n2)}.bat'

    def cmdworker():
        a = addressbar_input.get()
        b = a.replace("\\", "//")
        c = path_input.get()
        d = c.replace("\\", "//")
        os.system(f'cmd /c "Move {fileg} {d}"')
        os.system(f'cmd /k "{b}: & cd {d} & {d}//{fileg} & exit"')
        root2.destroy()

    root2 = Tk()
    root2.geometry('900x600')
    root2.maxsize(900, 200)
    root2.minsize(900, 200)
    root2.configure(background='light grey')
    root2.title('Define Path')
    Label(root2, text='Disk name:', bg='light grey', font='arial 20').grid(pady=5)
    Label(root2, text='Path:', bg='light grey', font='arial 20').grid(row=1, column=0)
    Button(root2, text='Create', bg='navy', command=cmdworker, font='arial 20').grid(row=3, column=1)
    address_disk = StringVar()
    addressbar_input = Entry(root2, textvariable=address_disk, font='arial 20')
    addressbar_input.grid(row=0, column=1)
    address_path = StringVar()
    path_input = Entry(root2, textvariable=address_path, font='arial 20')
    path_input.grid(row=1, column=1)
    Label(root2, text="If a folder name contains space in between its name\n"
                      "like (new folder) so please enclose it in (\" \") like\n"
                      "if path = (D:\\New folder) so change path = (D:\\\"New folder\") ",
          borderwidth=5, relief=SUNKEN, fg='red', bg='grey', font='arial 15') \
        .grid(row=3, padx=3, pady=5)
    root2.mainloop()


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
    Maker()


def hlp():
    msg.showinfo('how to use', '1:Paste main folder names\n2:Paste sub folder names\n3:Press SAVE\n4:Give disk name(It '
                               'is '
                               'always a alphabet)\n5:Copy and paste path\n6:Press create\n~~~for more info read ('
                               'readme.txt)..')


root = Tk()
root.geometry('450x550')
root.maxsize(450, 550)
root.minsize(450, 550)
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
Label(root, text=f'File name:{str(n1) + str(n2)}.bat', font='Fantasy 15 bold', borderwidth=10, relief=RAISED, fg='Blue',
      bg='lightgrey') \
    .grid(row=4, pady=10)
Button(root, text='SAVE', command=main, font='arial 40', fg='White', bg='navy').grid(row=3, )
help1 = Menu(root)
help1.add_command(label='How to use', command=hlp)
root.config(menu=help1)
Label(root, text='NOTE:Do not give extra empty line after names of folder', fg='red', borderwidth=5, relief=SUNKEN,
      font='arial 12 bold') \
    .grid(row=5, padx=5)
root.mainloop()
