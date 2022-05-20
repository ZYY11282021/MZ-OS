import os

print("欢迎来到MZ-OS!")

def iput():
    global iputContent
    iputContent = input("$ ")

def oput():
    if iputContent == "exit":
        exit()
    elif iputContent == "clear":
        os.system("cls")
    else:
        print('Command "%s" not found.' % iputContent)
