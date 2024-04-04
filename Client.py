#Client
from socket import *
import time

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
	b_bytes = int(input('size of each message in B bytes: '))
	list_of_messages[str(i)] = b_bytes
	print()
print('Processing...')

# part ii) Sending message and part iii) Round Trip Time
for index in list_of_messages:
	# message = "\x00" * numBytes
	message = "\x00" * list_of_messages[index]
	
	print("sending message: ", message.encode())
	start_time = time.time()
	clientSocket.sendto(message.encode(), (serverName, serverPort))
	
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print(modifiedMessage.decode()) 
	end_time = time.time()
	print("The RTT for this message was ", (end_time - start_time), " seconds")
clientSocket.close()