import socket
# from datetime import datetime

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM ) # UDP Protocol

#target_ip = "192.168.1.75" 
target_ip = "127.0.0.1"   # for single person
port_no = 2525 

target_address = (target_ip,port_no)

print("Connection to the reciver side ......")

print("Type 'exit' to stop the sender.....")

condition = True
while condition:
    message = input("Plz write your message here : ")
    
    encrypt_message = message.encode('ascii')
    #timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    s.sendto(encrypt_message,target_address)