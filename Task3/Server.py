from socket import *

serverPort = 3046
#define TCP server
serverSocket = socket(AF_INET, SOCK_STREAM) 
#make binding with any ip address by ''
serverSocket.bind(('', serverPort))
# listen for requests
serverSocket.listen(1) 
# print for the server is ready 
print('server is ready ...')

#opening all the files and images 
#main_en.html
with open('main_en.html', 'r',encoding='utf-8') as f1:
    mainEn = f1.read()
#main_ar.html
with open('main_ar.html','r', encoding='utf-8') as f2:
    mainAr = f2.read()
#get img page
with open('mySite1221971.html','r', encoding='utf-8') as f3:
    getImg = f3.read()
#error request page 
with open ('notFound404.html','r',encoding='utf-8') as f4:
    notFound = f4.read()
#style.css
with open('style.css','r', encoding='utf-8') as f5:
    css = f5.read()
#all the used images
with open('pal.jpg', 'rb') as f6:
    pal=f6.read()
with open('pal2.jpg', 'rb') as f7:
    pal2 = f7.read()
with open('yahya.png', 'rb') as f8:
    yahya = f8.read()
with open('laith.png', 'rb') as f9:
    laith = f9.read()
with open('masarra.png', 'rb') as f10:
    masarra = f10.read()
with open('bzu.png', 'rb') as f11:
    bzu = f11.read()
while True:
    #accept the connection  
    connectionSocket, addr = serverSocket.accept()
    ip = addr[0]
    port = addr[1]
    print('Got connection from', "IP: " + ip + ", Port: " + str(port))
    #receve http reqeust 
    sentence = connectionSocket.recv(4096).decode()
    #split the request to get the request line from user input
    match= sentence.split('\n')[0] 
    response= match.split(' ')[1]
    print("\\\\\\"+response+"//////") # print http request intermanel 
    print(sentence)
    # for any of this we handle the request depinding on the url
    # for the base mian_en.gtml file :
    if(response=="/" or response=="/index.html" or response=="/main_en.html" or response=="/en"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(mainEn.encode())
    #for the get img page :
    elif(response == "/mySite1221971.html"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(getImg.encode())
    #if this statment(mySite1221971.html?imageName) in the url then the user submit a img name in the html form
    elif 'mySite1221971.html?imageName' in response :
        img1 = response.split('=')[1] #to get the image name alone 
        with open(str(img1),'rb') as anyImg : # open the img
            img2 = anyImg.read()
        #to check what the img type is , to send the correct http response 
        if (img1.endswith('.jpg')) : 
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: image/jpg;\r\n".encode())
            connectionSocket.send("\r\n".encode()) 
            connectionSocket.send(img2)
        else :
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: image/png;\r\n".encode())
            connectionSocket.send("\r\n".encode()) 
            connectionSocket.send(img2)
    #main_en page background img
    elif(response=="/pal.jpg"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpg;\r\n".encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.send(pal)
    #main_ar page background img
    elif (response =="/pal2.jpg"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpg;\r\n".encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.send(pal2)
    #our imgs in the both pages (en,ar)
    elif (response =="/yahya.png"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png;\r\n".encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.send(yahya)
    elif (response =="/laith.png"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png;\r\n".encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.send(laith)
    elif (response =="/masarra.png"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png;\r\n".encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.send(masarra)
    #for main_ar.html page 
    elif(response=="/ar" or response=="/main_ar.index"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(mainAr.encode())
    #for the css file 
    elif (response =="/style.css"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/css;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(css.encode())
    #if the client request any file of html type
    elif (response.endswith('.html')):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(mainEn.encode())
    #if the client request any file of css type
    elif(response.endswith('.css')):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/css;\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(css.encode())
    #if the client request any img of png type
    elif(response.endswith('.png')):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png;\r\n".encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.send(bzu)
    #if the client request any img of jpg type
    elif (response.endswith('.jpg')):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpg;\r\n".encode())
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.send(pal)
    #opening stackoverflow website
    elif (response == "/so"):
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send('Content-Type: text/html; charset=utf-8\r\n'.encode())
        connectionSocket.send("Location:http://www.stackoverflow.com\r\n".encode())
        connectionSocket.send('\r\n'.encode())
        print("stackoverflow.com website is connected\r\n")   
    # opening itc website
    elif (response == "/itc"):
        connectionSocket.send('HTTP/1.1 307 Temporary Redirect\r\n'.encode())
        connectionSocket.send('Content-Type: text/html; charset=utf-8\r\n'.encode())
        connectionSocket.send("Location:https://itc.birzeit.edu/course/index.php\r\n".encode())
        connectionSocket.send('\r\n'.encode())
        print("itc.com website is connected\r\n")
    #if the client made any request that dose not exisits    
    else:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(notFound.encode())