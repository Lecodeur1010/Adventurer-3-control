import tkinter as tk
import socket
import Adv3Api as Api


socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Notready = False
AutoIp = "CustomIp"
PORT=8899

if not Api.Connect(AutoIp) :
   print("Connected using predefined ip : "+AutoIp)

while Notready :
 print("Adventurer 3 control")
 ip = input("Printer IP : ")
 if Api.Connect(ip) :
    Notready = False
 else : 
    print("Error to connect to printer")

root = tk.Tk(screenName="ADV3",className="ADV3")


      
def Send1() :
   Send2()

def Lamp1():
    Api.SendGCode("M146 r255 g255 b255 F0")

def Lamp2():
    Api.SendGCode("M146 r0 g0 b0 F0")

def Fan1():
    Api.SendGCode("M651")

def Fan2():
    Api.SendGCode("M652")
Lamp1v = tk.Button(root, text="Turn on lamp", command=Lamp1)
Lamp2v = tk.Button(root, text="Turn off lamp", command=Lamp2)
Fan1v = tk.Button(root, text="Turn on fan", command=Fan1)
Fan2v = tk.Button(root, text="Turn off fan", command=Fan2)
Hotendtxt = tk.Label(root, text = "Hotend temp : " )
Hotend = tk.Entry(root)
Bed = tk.Entry(root)
CMD = tk.Entry(root)
Bedtxt = tk.Label(root, text = "Bed temp : " )
CMDtxt = tk.Label(root, text = "Other CMD : " )
SendCMD = tk.Button(root, text="Send data", command=Send1)

def Send2():
   tbed=Bed.get()
   thotend=Hotend.get()
   other1=CMD.get()
   if tbed :
    Api.SendGCode("M140 S"+tbed)
   if thotend :
    Api.SendGCode("M104 S"+thotend)
   if other1 :
    Api.SendGCode(other1)

Lamp1v.grid(row=0, column=0)
Lamp2v.grid(row=1, column=0)
Fan1v.grid(row=0, column=1)
Fan2v.grid(row=1, column=1)
Hotendtxt.grid(row=2,column=0)
Bedtxt.grid(row=3,column=0)
CMDtxt.grid(row=4,column=0)
Hotend.grid(row=2,column=1)
Bed.grid(row=3,column=1)
CMD.grid(row=4,column=1)
SendCMD.grid(row=5)



root.mainloop()



