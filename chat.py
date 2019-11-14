import threading 
import os
from socket import *
import time
host=''
port=13000
usernameFile=open("userProfile.txt","r")
messagefile=open("message.txt","r")
username=usernameFile.read()
usernameFile.close()
#chatfile = open("ChatFile.txt","a+") 


def sender():
    global host 
    global port
    #global username
    #global chatfile
    while 1:

        chatfile = open("ChatFile.txt","a+") 
        messagefile=open("message.txt","r+")
        usernameFile=open("userProfile.txt","r")
        username=usernameFile.read()
        usernameFile.close()
        message=messagefile.read()
        if message:
            
            mymsg = username + ' :' + message
            dest = ('<broadcast>',port)
            soc = socket(AF_INET,SOCK_DGRAM)
            soc.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
            soc.sendto(bytes(mymsg, "utf8"),dest)
            chatfile.write(mymsg+'\n')
            messagefile.truncate(0)
        messagefile.close()
        chatfile.close()


def recieve():
        global host 
        global port
        #global chatfile
        sock=socket(AF_INET,SOCK_DGRAM)
        sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        sock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
        sock.bind((host,port))

        while 1:
            chatfile=open("chatFile.txt","a+")
            try:
                usernameFile=open("userProfile.txt","r")
                username=usernameFile.read()
                usernameFile.close()
                message,address=sock.recvfrom(port)
                recievedMsg=message.decode("utf8")
                tempUname=recievedMsg.split(" :")
                #print(tempUname)
                if tempUname[0]==username :
                    #print("inside if")
                    continue
                else:
                    chatfile.write(recievedMsg+'\n')
                
            except(KeyboardInterrupt,SystemExit):
                raise
            except:
                pass
            chatfile.close()

        

   
        
            








if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=recieve, args=()) 
    t2 = threading.Thread(target=sender, args=()) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 

