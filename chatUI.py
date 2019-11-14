from tkinter import *
import tkinter as tk
import os
import subprocess
import time
from socket import *
import threading
from functools import partial



r = Tk()
enteredChat=0
chatRoom=0
print("Hi")

chatFile1=open("chatFile.txt","w")
message1=open("message.txt","w")
userProfile1=open("userProfile.txt","w")
# chatFile.close()
# message.close()
# userProfile.close()

#r = Tk()
givename=0
userName=StringVar()
msg=StringVar()
mylist=Listbox(r)
mylist1=Listbox(r)
#pack_propagate(0)

labels=[]
def setProperFrameWidth(window,msg):
    print("ProoperFrame")
    window.title(msg)
    window.geometry("550x550")#You want the size of the app to be 500x500
    window.resizable(0,0)#Don't allow resizing in the x or y direction
    background=tk.Frame(master=window)
    background.grid_propagate(0)#Don't allow the widgets inside to determine the frame's width / heights

def sendMsg(sentence):
         getMsg= Entry(r,textvariable=msg)
         getMsg.grid(row=1, column=1)
         sentence=msg.get()        
         print("Senetence :",sentence)
         messageFile=open("message.txt","w")
         messageFile.write(sentence)
         messageFile.close()

def clearscreen(labels):
    #global labels
    for labe in labels:
        labe.destroy()

def quitChat(r):
    #connectionSocket.close()
   
    messageFile=open("message.txt","w")
    messageFile.write(" Logged Out .")
    messageFile.close()
    r.destroy()
def enterChat(labels):
    global enteredChat
    enteredChat=1
    clearscreen(labels)
    global chatRoom
    global userName
    global givename 
    setProperFrameWidth(r,"CHAT ROOM")
    userProfileFile=open("userProfile.txt","w+")   
    uname=userName.get()
    print(uname)
    userProfileFile.write(uname)
    userProfileFile.close()
    
    Label(r,text="Users ONLINE:").grid(row=5,column=1)

    Label(r, text="Welcome to CHAT ROOM "+ str(uname)).grid(row=1,column=0)
    Label(r, text='').grid(row=1,column=1,columnspan=10,rowspan=10)
    Label(r, text='').grid(row=2,column=1)

    getMsg= Entry(r,textvariable=msg)
    getMsg.grid(row=1, column=1)
    sentence=msg.get()

    sendBtn = tk.Button(r, text='SendMsg', width=25,bg="orange",fg="red", command=partial(sendMsg,sentence))
    sendBtn.grid(row=2,column=1)

    quitBtn = Button(r, text='QUIT', width=25,bg="red",fg="orange", command=partial(quitChat,r))
    quitBtn.grid(row=3,column=1)

    global mylist

    scrollbar = Scrollbar(r)
    scrollbar.grid( row=5,column=0,sticky=(E) )

    mylist = Listbox(r, xscrollcommand = scrollbar.set,yscrollcommand = scrollbar.set ,width="60",height="22",fg="green")
    
    #for line in range(100):
        #mylist.insert(END, "This is line number " + str(line))

    mylist.grid(row=6,column=0,sticky=(N,E,S,W) )
    
    scrollbar.config( command = mylist.yview )

    #online people

    global mylist1
    scrollbar1 = Scrollbar(r)
    scrollbar1.grid( row=5,column=1,sticky=(E) )

    mylist1 = Listbox(r, xscrollcommand = scrollbar1.set,yscrollcommand = scrollbar1.set ,width="5",height="22",fg="green")
    
    #for line in range(100):
        #mylist.insert(END, "This is line number " + str(line))

    mylist1.grid(row=6,column=1,sticky=(N,E,S,W) )
    
    scrollbar1.config( command = mylist1.yview )

    



usersOnline=set()
NoOfUsers=0
chatFileLength=0
def readChatFile():
    global chatFileLength
    global mylist
    global mylist1
    global NoOfUsers
    
    chatFile=open("chatFile.txt","r")
    chatFileLength=chatFile.readlines()
    chatFileLength=len(chatFileLength)
    chatFile.close()
    while 1:
        chatFile=open("chatFile.txt","r")
        updatedFile=chatFile.readlines()
        lengthOffile=len(updatedFile)
        chatFile.close()
        if lengthOffile>chatFileLength and lengthOffile!=0:
            chatFileLength=lengthOffile
            latestMsg=updatedFile[lengthOffile-1]
            tempUname=latestMsg.split(" :")
            print(tempUname,usersOnline)
            if tempUname[1]==" Logged Out .\n":
                for i in range(mylist1.size()):
                    if mylist1.get(i)==tempUname[0]:
                        mylist1.delete(i)
                        usersOnline.remove(tempUname[0])
                        NoOfUsers-=1
                        break
            else:

                usersOnline.add(tempUname[0])
                #print(tempUname,usersOnline)
                # newmsg=Label(mylist,text=latestMsg)
                # newmsg.grid()
                temp=len(usersOnline)

                #mylist1.insert(index,"hello")
                if temp>NoOfUsers:
                    print("if",tempUname,usersOnline)
                    NoOfUsers=temp
                    mylist1.insert(END,tempUname[0])
                #mylist1.see((mylist1.size())-1)
            mylist.insert(END,latestMsg)
            mylist.see(mylist.size()-1)
        chatFile.close()
        #index+=1


def runChatCode():
    cmd="chat.py"
    subprocess.call(["python",cmd])










runChatFile=threading.Thread(target=runChatCode, args=()) 
runChatFile.start()




setProperFrameWidth(r,'Login Into Chat RoomServer')


label=Label(r, text='')
labels.append(label)
label.grid(row=1,column=1,columnspan=10,rowspan=10)


label=Label(r, text='')
label.grid(row=2,column=2)
labels.append(label)
label=Label(r, text='                  ')
label.grid(row=3,column=3)
labels.append(label)
label=Label(r, text='                            ')
label.grid(row=4,column=4)
labels.append(label)
label=Label(r, text='')
label.grid(row=5,column=5)
labels.append(label)
label=Label(r, text='')
label.grid(row=6,column=6)
labels.append(label)
label=Label(r, text='Enter Name  :')
label.grid(row=7,column=4)
labels.append(label)



e1 = Entry(r,textvariable=userName)
e1.grid(row=7, column=5)
labels.append(e1)


uname=userName.get()
print(type(uname))
#uname


Loginbutton = tk.Button(r, text='Login', width=25,bg="orange",fg="red", command=partial(enterChat,labels))
label=Label(r, text='')
label.grid(row=8,column=5)
labels.append(label)
labels.append(Loginbutton)
Loginbutton.grid(row=9, column=5)
#print(labels)

#time.sleep(100)
#r.destroy()



readMsg=threading.Thread(target=readChatFile, args=()) 
readMsg.start()



r.mainloop()

readMsg.join()
runChatFile.join()