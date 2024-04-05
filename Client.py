# Client:                Server:
# - N_msg = input("")    - ACK = msg.seq
# - win_size = 5         - win_size = 5
# 				         - go_back_n() or selective_repeat()
# - seq = 100            - in-order delivery (print if out-of-order)
# - print statements x4

#Client
from socket import *
import time
from Message import Message

serverName = 'localhost' 
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# part i) User Input
print('Hi, please input the following:')
n_messages = input('how many total N messages would you like to send: ')  
print() 

#format: nth message: b_bytes
list_of_messages = {}
for i in range(int(n_messages)):
	seq = 100
	ack = 100
	ttl = 5
	payload = "abcd"

	full_message = Message(seq, ack, ttl, payload)
	
	list_of_messages[str(i)] = full_message
print(list_of_messages)
print('Processing...')

# part ii) Sending message and part iii) Round Trip Time
for index in list_of_messages:
	
	packet = list_of_messages[index].convertToPacketPlus()
	print("sending message: ", packet)
	start_time = time.time()
	clientSocket.sendto(packet.encode(), (serverName, serverPort))
	
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print(modifiedMessage.decode()) 
	end_time = time.time()
	print("The RTT for this message was ", (end_time - start_time), " seconds")
clientSocket.close()


#Print Statements
#	- SEQ of each message being sent using the following string : 
print("Message with SEQ# ___ sent")

#	- SEQ of each acknowledges message using the following string: 
print("Message with SEQ# ___ ACKd")

#	- Window size before every transmission is sent and after every ACK is received using the following string: 
print("Current window size: ___")

#	- Any timeout event and event handling using the following string: 
print("Timeout event occurred. Message SEQ# ____ resent.")