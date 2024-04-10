
# How to use
Run /hw3/Server.py
```python Server.py```

Run /hw3/Client.py 
```python Client.py```

You will be prompted the following (on Client.py):
```
Hi, please input the following:
how many total N messages would you like to send:
```
Type `5` and Hit `Enter`

The next output (on Client.py):
```
Processing...
sending message: 1001005abcd
Message with SEQ# 100 sent
1001005abcd
The RTT for this message was 0.010540962219238281 seconds
``` 

# Purpose of this code

The purpose of this code is to build on top of UDP by adding extra headers to create more reliability of ensuring messages are being sent.

# Architecture/Design
```
# self.windowSize = windowSize
# TCP checksum?

self.seq  =  seq
self.ack  =  ack
self.ttl  =  ttl
self.payload  =  payload
```
# Error Detection
Packets are being sent as strings, but to increment SEQ# or ACK then we will need to convert to integer type.

# Updates
4/7/2024 12:30
- added payload_length to message.py (we'll use 4)
- changed ACK to 1
- changed TTL to 2 (2 hops max)

### Output
