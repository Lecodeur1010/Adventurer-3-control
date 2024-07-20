#all import and other function

import socket
import os
import Adv3Api as API

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8899
error = 0
loop = True
show = True
AutoIp = "CustomIP"
#all function

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def ShowCMD():
        print("1.Turn on lamp")
        print("2.Turn off lamp")
        print("3.Stop printing")
        print("4.Turn on chasis fan")
        print("5.Turn off chasis fan")
        print("6.Set bed temperature")
        print("7.Set hotend temperature")
        print("8.Clear screen")
        print("?.Show available command")
        print("To send other command,simply write")

def Command():
    choice = input("What do you want ?")
    if choice == "1" :
        return SendGCode("M146 r255 g255 b255 F0")
    elif choice == "2" :
        return SendGCode("M146 r0 g0 b0 F0")
    elif choice == "3" :
        return SendGCode("M26")
    elif choice == "4" :
        return SendGCode("M651")
    elif choice == "5" :
        return SendGCode("M652")
    elif choice == "6" :
        bedtemp = input("Bed temperature : ")
        return SendGCode("M140 S"+bedtemp)
    elif choice == "7" :
        hotendtemp = input("Hotend temperature : ")
        return SendGCode("M104 S"+hotendtemp)
    elif choice == "8" :
        cls()
    elif choice == "?" :
        ShowCMD()
    else : 
        return SendGCode(choice)
    
def main() :
    ShowCMD
    while True :
     reponse = Command()
     print(reponse)

if Connect(AutoIp) :
 print("Connected using pre-configured ip : "+AutoIp)
 main()


while True :
 print("Adventurer 3 control")
 ip = input("Printer IP : ")
 if Connect(ip) :
    print("Connected")
    main()
 else : 
    print("Error to connect to printer")

