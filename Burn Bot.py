import time

name= input("What is your name? ")
if name == "Burn Bot":
    print("Fatal Error Dectected: More than one Burn Bot detected")
    print("BurnBot.exe has crashed")
    exit()
else:
    age = int(input("How old are you? "))
    height= input("How tall are you? ")
    print("Welcome",name,"to the Burn Bot")
    print("Hello",name,"you are",age,"years old and",height,"tall")
    print("generating burn")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("burn generated")

if age < 21:
    print("Come back when you’re old enough to remember dial-up internet!")
elif age > 21:
    print("Careful, don’t throw out your back trying to keep up with the kids!")
time.sleep(1)
if height <= "5'4":
    print("you cant even use the weather app because it take rain 3 to 5 business days to reach you")
elif height > "5'4":
    print("you cant even use the weather app because you are above the clouds")

