#An api to send and receive GCode commands and files to the Adventurer 3 3D Printer via TCP.

import socket
import threading

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8899

connectedip = (None, None) # (ip, port)

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
