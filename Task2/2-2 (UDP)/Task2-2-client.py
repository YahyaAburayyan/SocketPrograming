from socket import *

serverName = 'localhost'
portNum = 1971

clientSocket = socket(AF_INET, SOCK_DGRAM) #creating a socket for a UDP connection 
while True: # infinite loop so the clint can send more than one time and if s/he wants to stop sending messages just enter "bye"
    clientMsg = input('Enter message to server : ')
    if clientMsg == 'bye':
        clientSocket.sendto(clientMsg.encode(),(serverName, portNum)) # sending at the spacific port num 
        #msgFromServer,serverAddress = clientSocket.recvfrom(1024)
        #print('Server response : ' ,msgFromServer.decode() )
        break
    else :
        clientSocket.sendto(clientMsg.encode(),(serverName, portNum)) # sending at the spacific port num 
        msgFromServer,serverAddress = clientSocket.recvfrom(1024)
        print('Server response : ' ,msgFromServer.decode() ) # printing the server response

