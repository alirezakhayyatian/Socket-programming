# -*- coding: utf-8 -*-

import select, socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)


server.bind(('', 1111))
server.listen(5)
inputs = [server]
outputs = []
message_list =[]
z=0
print ("Server is Listening")
while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
            
            #print(connection, client_address)
            
        else:
            
            msg = s.recv(1024)
            sentence = msg.decode(encoding='UTF-8',errors='strict')
            
            if(z==1):
                z=0
                if(sentence == 'b'):
                    print(str(s.getpeername()) + 'going to remove')
                    inputs.remove(s)
                    continue

                     
            
            if( sentence == 'view'  ):
                #s.send( (str(len(message_list))).encode('UTF-8') )
                mess = ['<'+ str( message_list[i][0][0] )+ ' , ' + str( message_list[i][0][1] ) + '>'+' said:' + message_list[i][1]  for i in range(len(message_list) )]
                s.send( ( '\n'.join(mess) ).encode('UTF-8'))
                z=1

            elif( sentence == 'bye' ):
                print(str(s.getpeername()) + 'going to remove')
                inputs.remove(s)
                continue
            elif(( (sentence != 'e') and (sentence != 'eview') ) and (sentence != 'view') ):
                print(s.getpeername(), sentence)
                message_list.append([s.getpeername(),sentence])
                
            
        
