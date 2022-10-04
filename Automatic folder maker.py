import random
'''After you have done all steps you will get a .bat file which you have to copy and paste at the place
   where you want to make folders'''
name=random.randint(0,9999999999999)
name2=random.randint(0,1000)
file = open(str(name)+str(name2)+'.bat', 'a')
inputs = []
print("Paste folder names/press empty enter 2 times when done:" )
while True:
    inp = input()
    if inp == "":
        break
    inputs.append(inp)
print('Folder names are added')
file.write('mkdir ')
for i in inputs:
    file.write(i+' ')
file.write('\n')
print('~~~Main folders added successfully~~~')
while True:
    print('Do you want to add sub folders?\na:Same folders\nb:different folders\nc:No subfolders ')
    subfolder=input('-->')
    if subfolder == 'b':
        foldername=input('folder name in which you want to add:')
        inputs2 = []
        print("Paste subfolder names/press empty enter 2 times when done:")
        while True:
            inp2 = input()
            if inp2 == "":
                break
            inputs2.append(inp2)
        print('Sub folder names added')
        file.write('cd '+foldername+'\n')
        file.write('mkdir ')
        for i2 in inputs2:
            file.write(i2 + ' ')
        file.write('\n')
        continue
    elif subfolder == 'c':
        file.close()
        break
    elif subfolder == 'a':
        print('This will make same name folders in every main folder')
        print("Type/paste subfolder name:")
        while True:
            name1 = input()
            for i in inputs:
                file.write('cd ')
                file.write(i + ' ')
                file.write('\n')
                file.write(f'mkdir {name1}')
                file.write('\ncd..\n')
            file.write('\n')
            break
        print('Sub folder names added')
    else:
        print('Invalid input')
        continue
