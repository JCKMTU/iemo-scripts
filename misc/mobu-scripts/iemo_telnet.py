from pyfbsdk import *
import socket
import sys


HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#Start listening on socket
s.listen(10)
print 'Socket now listening'



def sendFrame(obj1, obj2):
    conn.sendall(str(GetBlendShapeProp(char))[1:-1] + "\n")


#now keep talking with the client
conn, addr = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])

FBSystem().OnUIIdle.Add(sendFrame)


#conn.close()
#s.close()