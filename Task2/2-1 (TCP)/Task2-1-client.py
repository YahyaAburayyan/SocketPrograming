from socket import * # import evrey thing in Socket library 

serverName = 'localhost' 
portNum = 1971 #port num 

clientSocket = socket(AF_INET, SOCK_STREAM)#socket inizile for TCP connection
clientSocket.connect((serverName, portNum))#connect the clint to server
print('Enter data to replace vowels with (#)')#asking for data
data = input('Enter data to replace vowels : ')#read data from client
clientSocket.send(data.encode())#sending the data to server with the above connection
editedData = clientSocket.recv(1024)#reciving the edited data from the server
print('edited data : ', editedData.decode())#printing the edited data
clientSocket.close() # close the connection with the server