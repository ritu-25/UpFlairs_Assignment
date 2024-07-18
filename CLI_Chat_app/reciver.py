import socket
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP Protocol

ip_address = "127.0.0.1"  # for single person
port_no = 2525  # 0 - 65353 Range of port
received_host = 'Receiver_side'

complete_address = (ip_address, port_no)

s.bind(complete_address)  # for registering an address
print("Connecting to the sender ........ ")
print("Hey, I am receiving your message!........")

while True:
    message, sender_address = s.recvfrom(1024)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    received_message = message.decode()
    print(f"[{timestamp}] Message from the sender: {received_message}")

    with open(received_host + '.txt', 'a+') as file:
        file.write(f"[{timestamp}] Sender: {received_message}\n")

    response = input("Enter your response message: ")
    encrypted_response = response.encode()
    s.sendto(encrypted_response, sender_address)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(received_host + '.txt', 'a+') as file:
        file.write(f"[{timestamp}] Receiver: {response}\n")
