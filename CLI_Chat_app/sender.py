
import socket
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP Protocol

ip_address = "127.0.0.1"  # for single person
port_no = 2525  # 0 - 65353 Range of port
sender_host = 'Sender_side'
complete_address = (ip_address, port_no)

while True:
    message = input("Enter your message to send: ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    encrypted_message = message.encode()
    s.sendto(encrypted_message, complete_address)

    with open(sender_host + '.txt', 'a+') as file:
        file.write(f"[{timestamp}] Sender: {message}\n")

    response, _ = s.recvfrom(1024)
    decrypted_response = response.decode()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] Response from receiver: {decrypted_response}")

    with open(sender_host + '.txt', 'a+') as file:
        file.write(f"[{timestamp}] Receiver: {decrypted_response}\n")
