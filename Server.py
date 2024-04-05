# Client:                Server:
# - N_msg = input("")    - ACK = msg.seq
# - win_size = 5         - win_size = 5
# - msg = 'abcd'         - go_back_n() or selective_repeat()
# - seq = 100            - in-order delivery (print if out-of-order)
# - print statements x4

#Server
from socket import *

# Create a socket and set the server port
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the server socket to any IP address and the specified port
serverSocket.bind(('', serverPort))

print("The server is ready to receive messages...")

counter = 1

while True:
    # Wait for a message to arrive
    message, clientAddress = serverSocket.recvfrom(2048)
    print("============ Message: ", counter, "==============")
    print("The address: ", clientAddress)
    print("The content: ", message)
    print()
    
    #Echo back
    serverSocket.sendto(message, clientAddress)
    print("The following message: ", message)
    print("was sent back to address: ", clientAddress)
    print('Message echoed back to client')
    print()
    
    counter += 1
