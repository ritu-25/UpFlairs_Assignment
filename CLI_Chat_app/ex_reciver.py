import socket
#from datetime import datetime

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM ) # UDP Protocol

# ip_address = "192.168.1.72"   # for center wifi  for multiple user connected
ip_address = "127.0.0.1"   # for single person
port_no = 2525   #  0 - 65353 Range of port

complete_address = (ip_address,port_no)
s.bind(complete_address) # for register an addesss 


print(" Hey I am reciving your message !........")
while True:
    message  = s.recvfrom(100)
    #print(message)   # (b'lucknow', ('127.0.0.1', 58763))
    # s.sendto()
    sender_address = message[1][0]  # '127.0.0.1'.txt
    recived_message = message[0]
    decrypted_message = recived_message.decode('ascii')
    # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(decrypted_message)
    
            # '127.0.0.1'.txt

    with open(sender_address +'.txt','a+') as file:
        file.write(decrypted_message +'\n')

