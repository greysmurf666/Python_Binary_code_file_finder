
from tkinter import filedialog
import tkinter as tk


filename = ""
hex_name = ""
directory = ""
count = 0
first_loop = True
key = ""
result = ""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def search(word,source):
    places = []
    for x in range(0,len(source)):
        if source[x] == word[0]:
            if source[x:x+len(word)] == word:
                places.append(x)
    return places






while True:

    if first_loop == True:

        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()
        root.quit()

        hex_name = input("input object in binary code: ")
        print(file_path)

    if first_loop == False:

        key = input("A for back, D for next or put integer number or R for reset: ")

    checkint = is_number(key)

    if key == "r":
        first_loop = True
        key = ""
        continue



    if checkint == True:

        count = int(key)

    else:
        if key!= "a" and key !="d" and key !="r" and first_loop == False:

            print("Input Invalid")

            continue


    if key=="a" and first_loop == False:
        count -= 1

    if key=="d" and first_loop == False:
        count += 1

    if count<0 and first_loop == False:
        count = 0

    if  count>len(result)-1 and first_loop == False:
        count = len(result)-1

    if hex_name == "" and file_path == "":
        first_loop = True
        print("Select file and input string to search")
        continue

    if hex_name !="" and file_path !="":

        f=open(file_path,"rb")
        data = f.read()
        converter = str(data)
        binary = converter[2:-1]

        result = search(hex_name,binary)

        if result != []:
            print("Number of cases finded:",len(result))
            print("Binary Code: \n",binary)

            print("object finded number "+str(count+1),"\n")

            print(result)

            print("..." + binary[result[count]-10:result[count]]+bcolors.OKBLUE+binary[result[count]:result[count]+len(hex_name)]+bcolors.ENDC+binary[result[count]+len(hex_name):result[count]+10+len(hex_name)]+"... \n")
        else:

            first_loop = True
            print(bcolors.FAIL+"no any object in Binary code"+bcolors.ENDC)


    first_loop = False