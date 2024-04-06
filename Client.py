# Client: 
# TODO
# - win_size = 5
# - seq = 100   
# - print statements

from socket import *
import time
from Message import Message

def updateList(listOfMessages):
	valToRemove = listOfMessages.pop(0)
	return listOfMessages


################################################
#####		 		  MAIN				   #####
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
for i in range(int(nMessages)):
	seq = 100
	ack = 100
	ttl = 5
	payload = "abcd"

	fullMessage = Message(seq, ack, ttl, payload)
	
	listOfMessages[str(i)] = fullMessage
print('Processing...')

# part ii) Sending message and part iii) Round Trip Time
for index in listOfMessages:
	
	#convert headers and message to string (aka packet)
	packet = listOfMessages[index].convertToPacket()
	print("sending message: ", packet)

	#Send payload
	startTime = time.time()
	clientSocket.sendto(packet.encode(), (serverName, serverPort))
	print("Message with SEQ# ", listOfMessages[index].seq ," sent")
	
	#Receive ACK
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print(modifiedMessage.decode()) 
	endTime = time.time()
	print("The RTT for this message was ", (endTime - startTime), " seconds")

	#confirm ACK (TODO)
	#update list of messages
	listOfMessages = updateList(listOfMessages)

clientSocket.close()


#Print Statements
#	- SEQ of each acknowledges message using the following string: 
print("Message with SEQ# ___ ACKd")

#	- Window size before every transmission is sent and after every ACK is received using the following string: 
print("Current window size: ___")

#	- Any timeout event and event handling using the following string: 
print("Timeout event occurred. Message SEQ# ____ resent.")
