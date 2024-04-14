from message import encapsulate, decapsulate
from socket import *
import time

socket = socket(AF_INET, SOCK_DGRAM)
window = 4
timeout = 60

def send(mesg, addr, port, batch):
    
    for seq in batch:
        socket.sendto(encapsulate(seq, mesg).encode(), (addr, port))
        batch[seq] = time.time() #update time

def recv(mesg, addr, port, batch):
    keys = list(batch)
    while(len(batch) > 0):
        seqsLeft = list(batch)

        #counts as first send and also transmit
        send(mesg, addr, port, batch)
        
        for seq in seqsLeft:
            endtime = time.time()

            keys = batch.keys()
            huh = batch

            if seq not in batch:
                break

            diff = endtime - batch[seq]

            if diff >= timeout:
                print("need to resend")
                send(mesg, addr, port, batch)
            else:
                data, addrServer = socket.recvfrom(2048)
                ack, mesgRecv = decapsulate(data.decode())
        
                if (ack in batch):
                    batch.pop(ack)
                    print(ack, mesgRecv)

def main():
    dest = input('Destination: ')
    mesg = input('Message: ')
    total = int(input('Number times to send: '))

    addr = dest.split(':')[0]
    port = int(dest.split(':')[1])

    print('\n-------------------------------------------')
    for i in range(0, total, window):
        batchLength = i + window

        if (batchLength > total):
            batchLength = total

        
        #send message at this time 115
        #time passes
        #timeout: current end: 120 - start: 115...5
        # if diff >= 5, resend

        batch = {} # {0:timestamp, 1:timestamp}
        for seq in range(i, batchLength): # [0, 1, 2, 3]
          timestamp = time.time() # 1713064386.4455032
          batch[seq] = timestamp

        # send(mesg, addr, port, batch)
        recv(mesg, addr, port, batch)  # recv([0, 1, 2, 3])
        print('-------------------------------------------')

    socket.close()

if __name__ == '__main__':
    main()
