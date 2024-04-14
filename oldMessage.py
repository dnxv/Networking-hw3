class Message:
  def __init__(self, seq, ack, ttl, payloadLength, payload):

    # self.windowSize = windowSize
    # TCP checksum?

    self.seq = seq
    self.ack = ack
    self.ttl = ttl
    self.payloadLength = payloadLength
    self.payload = payload

  def convertToPacket(self):
    """
    convert message instance into string payload to send to server
    Note: This would require buffering

    Returns:
        string: The entire packet of SEQ#, ACK, TTL, Payload
    Example:
        >>> seq, ack, ttl, payload = 100, 100, 5, 'abcd'
        >>> pre-payload = Message(seq, ack, ttl, payload)
        >>> packet = pre-payload.convertToPacket()
        >>> packet
        1001005abcd
    """
    packet = ""
    packet += "" + str(self.seq) + str(self.ack) + str(self.ttl) + str(self.payloadLength) + self.payload
    return packet
  
  def convertToPacketPlus(self):
    """
    convert message instance into string payload (seperated by periods) to send to server
    
    Returns:
        string: The entire packet of SEQ#, ACK, TTL, Payload
    Example:
        >>> seq, ack, ttl, payload = 100, 100, 5, 'abcd'
        >>> pre-payload = Message(seq, ack, ttl, payload)
        >>> packet = pre-payload.convertToPacket()
        >>> packet
        100.100.5.abcd
    """
    packet = ""
    packet += "" + str(self.seq) + "." + str(self.ack) + "." + str(self.ttl) + "." + str(self.payloadLength) + "." + self.payload
    return packet