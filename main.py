import os

print("欢迎来到MZ-OS!")
print("如果你需要一些帮助，请输入“帮助”")

def iput():
    global iputContent
    iputContent = input("$ ")

def oput():
    if iputContent == "退出":
        exit()
    elif iputContent == "清屏r":
        os.system("cls")
    else:
        print("找不到命令“%s”" % iputContent)
        
while True:
    iput()
    oput()
