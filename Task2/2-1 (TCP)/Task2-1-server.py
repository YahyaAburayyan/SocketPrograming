from socket import *# import evrey thing in Socket library

serverName = 'localhost'
portNum = 1971#port num 

serverSocket = socket(AF_INET,SOCK_STREAM)#socket inizile for TCP connection
serverSocket.bind((serverName,portNum))#bind the port num with the IP
serverSocket.listen()# make the server listening to a connection 
print('Server is on and ready to receive data')
vowelLatters = ['a','e','i','o','u','A','E','I','O','U']#all the vowels 
while True:  #to keep the server running
    connectionSocket,addr = serverSocket.accept()#make the TCP connection
    data = connectionSocket.recv(1024).decode()#rcv data from client
    editedData = " "
    for latter in data:               #if the latter is not a vowel add it  
        if latter not in vowelLatters:#else add (#) instead
            editedData += latter
        else:
            editedData += '#'

    finalMsg= 'The edited data with repalced vowels is : ' + editedData
    connectionSocket.send(finalMsg.encode())#sending the edited data to client
    connectionSocket.close() # end connection
    break    
    