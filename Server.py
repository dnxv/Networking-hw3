# Server:
# - ACK = msg.seq
# - win_size = 5
# - go_back_n() or selective_repeat()
# - in-order delivery (print if out-of-order)

################################################
#####		 		IMPORTS				   #####
################################################
from socket import *
from Message import Message

################################################
#####               METHODS				   #####
################################################
def deconstructMessage(message):
    splitMessage = message.split('.')
    seq = splitMessage[0]
    ack = splitMessage[1]
    ttl = splitMessage[2]
    payloadLength = splitMessage[3]
    payload = splitMessage[4]
    return seq, ack, ttl, payloadLength, payload 

################################################
#####		 		 MAIN				   #####
################################################
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
    print("The address: ", clientAddress, " The content: ", message)
    print()

    #deconstruct message into respective headers
    seq, ack, ttl, payloadLength, payload = deconstructMessage(message.decode())

    #send back new message
    # newMessage =       seq,   ack,                            ttl,           payloadLength, 
    #                    |      |                               |              |  payload
    newMessage = Message(ack, (int(seq) + int(payloadLength)), (int(ttl) - 1), 0, '')
    packet = newMessage.convertToPacketPlus()
    
    serverSocket.sendto(packet.encode(), clientAddress)
    print("The following message: ", packet, " was sent back to address: ", clientAddress)
    print()
    
    counter += 1
