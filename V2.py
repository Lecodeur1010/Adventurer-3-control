import tkinter as tk
import socket
import Adv3Api as Api


socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Notready = True
AutoIp = "CustomIp"
PORT=8899

if Api.Connect(AutoIp) :
   print("Connected using predefined ip : "+AutoIp)
   Notready = False

while Notready :
 print("Adventurer 3 control")
 ip = input("Printer IP : ")
 if Api.Connect(ip) :
    Notready = False
 else : 
    print("Error to connect to printer")

a = tk.Tk(screenName="adv3",className="adv3")
b = tk.Tk(screenName="adv3",className="adv3")
help = tk.Tk(screenName="adv3",className="adv3")

def GCode(G) :
   print(Api.SendGCode(G))



#A ------------------------------------------------------
      
def Send1() :
   Send2()

def Lamp1():
   GCode("M146 r255 g255 b255 F0")

def Lamp2():
   GCode("M146 r0 g0 b0 F0")

def Fan1():
   GCode("M651")

def Fan2():
   GCode("M652")

def GetPos():
   GCode("M114")

def GetInfo() :
   GCode("M115")

def GetStat() :
   GCode("M119")
Lamp1v = tk.Button(a, text="Turn on lamp", command=Lamp1)
Lamp2v = tk.Button(a, text="Turn off lamp", command=Lamp2)
Fan1v = tk.Button(a, text="Turn on fan", command=Fan1)
Fan2v = tk.Button(a, text="Turn off fan", command=Fan2)
Hotendtxt = tk.Label(a, text = "Hotend temp : " )
Hotend = tk.Entry(a)
Bed = tk.Entry(a)
CMD = tk.Entry(a)
Bedtxt = tk.Label(a, text = "Bed temp : " )
CMDtxt = tk.Label(a, text = "Other CMD : " )
SendCMD = tk.Button(a, text="Send data", command=Send1)
Pos = tk.Button(a,text="Get position",command=GetPos)
Info = tk.Button(a,text="Get info",command=GetInfo)
Stat = tk.Button(a,text="Get status",command=GetStat)

def Send2():
   tbed=Bed.get()
   thotend=Hotend.get()
   other1=CMD.get()
   if tbed :
    GCode("M140 S"+tbed)
   if thotend :
    GCode("M104 S"+thotend)
   if other1 :
    GCode(other1)

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
SendCMD.grid(row=5,column=0)
Pos.grid(row=5,column=1)
Info.grid(row=6,column=0)
Stat.grid(row=6,column=1)

#b--------------------------------------------------
def sendp1():
   sendp2()
def Home() :
   GCode("G1 X90 Y-90 Z90")

XL=tk.Label(b,text="X Positive = right")
YL=tk.Label(b,text="Y Positive = front")
ZL=tk.Label(b,text="Z Positive = up")
X=tk.Entry(b)
Y=tk.Entry(b)
Z=tk.Entry(b)
SendPos=tk.Button(b,text="Send",command=sendp1)
Homeb=tk.Button(b,text="Homing",command=Home)
Lab=tk.Label(b,text="0 is the center")

XL.grid(row=0, column=0)
YL.grid(row=1, column=0)
ZL.grid(row=2, column=0)
X.grid(row=0, column=1)
Y.grid(row=1, column=1)
Z.grid(row=2, column=1)
SendPos.grid(row=0, column=2)
Homeb.grid(row=1, column=2)
Lab.grid(row=2, column=2)

def sendp2() :
   
   
   
   if not len(X.get()) == 0 :
      GCode("G0 F2000 X"+X.get())
   if not len(Y.get()) == 0 :
      GCode("G0 F2000 Y"+Y.get())
   if not len(Z.get()) == 0 :
      GCode("G0 F2000 Z"+Z.get())


a.mainloop()
b.mainloop()
