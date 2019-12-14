from socket import *
import time as time


srvAdr = input("What's  Server IP ? ")
srvPort =int( input( "What's Server Port "))
#srvAdr = 'localhost'
#srvPort = 1111
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((srvAdr, srvPort))
print('Connection Established')


mode = 1

while clientSocket.fileno() != -1:
    if mode ==1:
        command = input("type in your text:")
    
    if ( command == 'view' ):
        mode = 2
        clientSocket.send(bytes(command, 'UTF-8'))        
        #length = clientSocket.recv(2048)
        #[ print(  clientSocket.recv(2048) ) for i in range(int(length)) ]
        x=( clientSocket.recv(2048) ).decode(encoding='UTF-8',errors='strict')
        print( x )
        #time.sleep(.5)
        ina = input('press e or b  or other ')
        if( ina == 'e' ):
            mode = 1
            clientSocket.send(bytes(ina, 'UTF-8'))
        elif( ina == 'b'):
            clientSocket.send(bytes(ina, 'UTF-8'))  
            #time.sleep(.5)
            clientSocket.close()

    elif( command == 'bye' ):
         mode =3
         clientSocket.send(bytes(command, 'UTF-8'))        
         clientSocket.close()
    
    if mode ==1:
        clientSocket.send(bytes(command, 'UTF-8')) 



