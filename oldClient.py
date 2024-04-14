# Client: 
# TODO
# - win_size = 5
# - seq = 100   
# - print statements
# - delete extra prints
# - net em download README.md
# - retransmission
# - out of order msgs

# Sliding window = 5 ||| [A, B, C, D, E], F, G, H, I, J, K, L, M
# Client: send window (A - E)
# Server: send ACK (A - E)
# Client: wait for ACK A
# Client: if ACK A, slide window 		||| A, [B, C, D, E, F], G, H, I, J, K, L, M
# Client: if no ACK A, send window 		||| [A, B, C, D, E], F, G, H, I, J, K, L, M
# Client: if ACK (A - E), send window 	||| A, B, C, D, E, [F, G, H, I, J], K, L, M
# 
# Handle case: when window is here: ||| A, B, C, D, E, F, G, H, I, [J, K, L, M]
# when the last segment is smaller than window size (in this case 4 < 5)

################################################
#####		 					IMPORTS				   				 #####
################################################

from socket import *
from oldMessage import Message

################################################
#####		 					METHODS								   #####
################################################

def receive():
	response, responseAddr = socket.recvfrom(2048)
	ack,

############################

def populateMessages(listOfMessages, nMessages):
	for i in range(int(nMessages)):
		if i == 0:
			listOfMessages[0] = Message(100, 1, 2, 4, "abcd") # seq, ack, ttl, payloadLength, payload
		else:
			seq = listOfMessages[i - 1].seq + listOfMessages[i - 1].payloadLength
			ack = i + 1
			ttl = 2
			payloadLength = 4
			payload = "abcd"

			fullMessage = Message(seq, ack, ttl, payloadLength, payload)
		
			listOfMessages[i] = fullMessage

def updateList(listOfMessages):
	valToRemove = listOfMessages.pop(0)
	return listOfMessages

def deconstructMessage(message):
    splitMessage = message.split('.')
    seq = splitMessage[0]
    ack = splitMessage[1]
    ttl = splitMessage[2]
    payloadLength = splitMessage[3]
    payload = splitMessage[4]
    return Message(seq, ack, ttl, payloadLength, payload)

################################################
#####		 		  			MAIN								   #####
################################################

serverName = 'localhost' 
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# part i) User Input
print('Hi, please input the following:')
nMessages = input('how many total N messages would you like to send: ')  
print() 

#populate list of messages
listOfMessages = {} #format: [nth message: Message()]
populateMessages(listOfMessages, nMessages)

# part ii) Sending message and part iii) Round Trip Time
for index in listOfMessages:

	#convert headers and message to string (aka packet)
	packet = listOfMessages[index].convertToPacketPlus()

	#Send payload
	clientSocket.sendto(packet.encode(), (serverName, serverPort))

	#keep: print("Message with SEQ#", listOfMessages[index].seq ,"sent.")
	print("Message with SEQ#", listOfMessages[index].seq ,"sent. Payload:", packet) 	#delete
	
	#Receive ACK
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	receivedMessage = deconstructMessage(modifiedMessage.decode())
	#keep: print("Message with SEQ#", receivedMessage.ack ,"ACKd. Payload: ", modifiedMessage)
	print("Message with SEQ#", receivedMessage.ack ,"ACKd. Payload: ", modifiedMessage) #delete
	print()

	#confirm ACK (TODO)
	#update list of messages
	# listOfMessages = updateList(listOfMessages)

clientSocket.close()


#Print Statements

#	- Window size before every transmission is sent and after every ACK is received using the following string: 
print("Current window size: ___")

#	- Any timeout event and event handling using the following string: 
print("Timeout event occurred. Message SEQ# ____ resent.")
