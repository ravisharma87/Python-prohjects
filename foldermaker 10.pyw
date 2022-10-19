from tkinter import *
import tkinter.messagebox as msg
import random
from tkinter import filedialog
import os
from PIL import ImageTk, Image
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

n1 = random.randint(0, 9999999999999)
n2 = random.randint(0, 1000)

fileg = f'{str(n1) + str(n2)}.bat'


def file_clearer():
    main_folder_clear = open('../foldermakerauto/Mainfoldernames.txt', 'w')
    main_folder_clear.write('')
    main_folder_clear.close()
    sub_folder_clear = open('../foldermakerauto/Subfoldernames.txt', 'w')
    sub_folder_clear.write('')
    sub_folder_clear.close()


file_clearer()


def runner():
    path = filedialog.askdirectory()
    a = rf"{path}"
    b = a.replace("/", "/\"")
    my_dir = str(b)
    os.system(f'cmd /c "Move {fileg} {my_dir}""')
    os.system(f'cmd /c "{my_dir[:2]} & cd {my_dir}" & {my_dir}"//{fileg} "')
    os.system(f'cmd /c "{my_dir[:2]} & cd {my_dir}" & del {fileg} "')


def Mainfoldersaver():
    main_file = open("../foldermakerauto/Mainfoldernames.txt", "w")
    main_file.write(main_text_input.get(1.0, END))
    main_file.close()


def Subfoldersaver():
    sub_file = open("../foldermakerauto/Subfoldernames.txt", "w")
    sub_file.write(sub_text_input.get(1.0, END))
    sub_file.close()


def reset():
    main_text_input.delete(1.0, END)
    sub_text_input.delete(1.0, END)
    file_clearer()


def main():
    Mainfoldersaver()
    Subfoldersaver()
    bat_file = open(str(n1) + str(n2) + '.bat', 'a')
    main_folder_out = open('../foldermakerauto/Mainfoldernames.txt')
    input_reader = main_folder_out.readlines()
    for names in input_reader:
        bat_file.write('mkdir \" ')
        bat_file.write(f'{names}')
        bat_file.write('\n')
    sub_folder_out = open('../foldermakerauto/Subfoldernames.txt')
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
    msg.showinfo("Done","Folders are generated")
    reset()

def hlp():
    msg.showinfo('Help', '1:Give main folder names\n2:Give subfolder names\n3:Press Save button\n4:Select Folder\n'
                         '!!! Do not leave extra line after folder name !!!')


root = Tk()
root.geometry("733x360")
root.maxsize(733, 360)
root.minsize(733, 360)
root.title('Folder maker-By Ravi sharma')
root.wm_iconbitmap("folder.ico")
root.config(background="grey")
photo1 = Image.open("../foldermakerauto/folde icon.png")
resized1 = photo1.resize((60, 40), Image.ANTIALIAS)
create = ImageTk.PhotoImage(resized1)
photo2 = Image.open("../foldermakerauto/reset icon.png")
resized2 = photo2.resize((60, 40), Image.ANTIALIAS)
reseter = ImageTk.PhotoImage(resized2)
photo3 = Image.open("../foldermakerauto/noteeeeee.png")
resized3 = photo3.resize((700, 70), Image.ANTIALIAS)
note = ImageTk.PhotoImage(resized3)
frame3 = customtkinter.CTkFrame(root, border_width=3, corner_radius=10)
frame3.grid(columnspan=4,padx=3)
frame1 = customtkinter.CTkFrame(frame3, bg='skyblue', corner_radius=10)
frame1.grid(pady=5, padx=5)
frame2 = customtkinter.CTkFrame(frame3, width=100, height=50, bg='skyblue', corner_radius=10)
frame2.grid(row=0, column=1, pady=3)
scrollbar = customtkinter.CTkScrollbar(frame1)
scrollbar.grid(column=1)
scrollbar2 = customtkinter.CTkScrollbar(frame2)
scrollbar2.grid(row=2, column=1)
customtkinter.CTkLabel(frame1, text='Main Folder Names', bg='skyblue', fg='red', corner_radius=5).grid()
main_text_input = Text(frame1, fg="lightgreen", width=30, height=8, yscrollcommand=scrollbar.set, font=' 20',
                       bg='grey', borderwidth=5, relief=SUNKEN)
main_text_input.grid(row=0)
customtkinter.CTkLabel(frame2, text='Sub Folder Names', bg='skyblue', fg='red', corner_radius=5).grid()
sub_text_input = Text(frame2, fg="lightgreen", width=30, height=8, yscrollcommand=scrollbar2.set, font=' 20',
                      bg='grey', borderwidth=5, relief=SUNKEN)
sub_text_input.grid(row=2)
customtkinter.CTkButton(root, text="Generate", text_font="arial 20", image=create, command=main, borderwidth=0,
                        corner_radius=10) \
    .grid(row=3, column=3, pady=40)
customtkinter.CTkButton(root, text="Reset", text_font="arial 20", image=reseter, width=100, command=reset,
                        borderwidth=0, corner_radius=10) \
    .grid(row=3,column=2)
help = Menu(root)
help.add_command(label='How to use', command=hlp)
root.config(menu=help)
root.mainloop()
