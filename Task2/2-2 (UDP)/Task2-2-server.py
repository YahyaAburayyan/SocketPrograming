from socket import *

serverNum ='localhost'
portNum= 1971 # port num

serverSocket = socket(AF_INET,SOCK_DGRAM) # creating a socket for a UDP connection 
serverSocket.bind((serverNum,portNum)) # bind the socket to the port num
clientsNum =0 # counter to the clints 
clientsPeers = {} #to store all the peers (clients) that send and risives from the server
print('Server is Running ...')

while True:
    msg,clientAddress = serverSocket.recvfrom(1024)
    if clientAddress not in clientsPeers: # checks if the peer is already exisits or not
        clientsNum += 1 # if not then increment the num of peers and add the new peer the the list using it's IPAddress as a indecator for it 
        clientsPeers[clientAddress] = clientsNum
    

    clientMsg = 'Message from client' + str(clientsPeers[clientAddress]) + ' :' +msg.decode() # geting the client num from the list
    print(clientMsg)
    if msg.decode() == 'bye' :
        print ('The client', str(clientsPeers[clientAddress]) ,' stops sending messages.')
        continue
    else :
        x = 'Enter message for client' + str(clientsPeers[clientAddress]) + ' : '#clientsPeers[clientAddress] is to get the num of the client with this address
        serverMsg = input(x)
        serverSocket.sendto(serverMsg.encode(),clientAddress) # sending server message to the spacific client
    #no break here to keep the server runing for more that one connection
