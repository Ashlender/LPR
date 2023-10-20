numb = int(input("Number from 0 to 10 "))
if numb>10 or numb<0:
    exit(print("conditions not met"))
if (numb>=0 and numb<4):
    print("[0-3]")
if (numb>=4 and numb<6):
    print("[3-6]")
elif (numb>=6 and numb<11):
    print("[6-10]")