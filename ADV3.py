#all import and other function

import socket
import os.path
import threading

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8899
error = 0

#all function

def Connect(ip: str, port=PORT):
    global connectedip
    """
    Connect to the printer at the given ip and port.
    Returns:
        socket.socket: The socket :)
    """
    try:
        socket1.connect((ip, port))
    except:
        return False
    print("Connected")
    socket1.close()
    #return socket1
    connectedip = (ip, port)
    return True

def SendGCode(gcode, wait=True, smart=True):
    """
    Send the given gcode to the printer.
    Returns:
        str: The response from the printer (if wait is True)
    """
    if smart:
        split = gcode.split(" ")
        if split[0] == "G0":
            split[0] = "G1"
        gcode = " ".join(split)
    gcode = "~" + gcode + "\r\n"
    #print(gcode)

    result = SendTCP(gcode, wait)

    #print(result)

    return result

socket_lock = threading.Lock()

def SendTCP(data, wait=True):
    """
    Send the given data to the printer.
    Returns:
        str: The response from the printer (if wait is True)
    """
    with socket_lock:
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket1.connect(connectedip)
        socket1.send(data.encode())
        if wait:
            socket1.settimeout(2)  # Set a timeout of 2 seconds
            try:
                response = socket1.recv(1024).decode()
            except socket.timeout:
                response = "Timeout"  # Return "Timeout" if there is no response within 2 seconds
            socket1.close()
            return response
        socket1.close()

def Command(show = False):
    if show :
       print("1.Turn on lamp")
       print("2.Turn off lamp")
       print("3.Stop printing")
       print("4.Turn on chasis fan")
       print("5.Turn off chasis fan")
       print("6.Set bed temperature")
       print("7.Set hotend temperature")
       print("8.Other command")

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
        return SendGCode("M652 S"+bedtemp)
    elif choice == "7" :
        hotendtemp = input("Hotend temperature : ")
        return SendGCode("M104 S"+hotendtemp)
    elif choice == "8" :
        cmd = input("Command : ")
        return SendGCode(cmd)
    else : print("To select an option, enter the number (e.g. 1)")



print("Adventurer 3 control")
ip = input("Printer IP : ")
if Connect(ip) :
    print(Command(True))
    while True :
        print(Command())


else : 
    print("Error to connect to printer")



