class Message:
  def __init__(self, seq, ack, ttl, payload):
    # self.headerLength = headerLength
    # self.windowSize = windowSize
    # TCP checksum

    self.seq = seq
    self.ack = ack
    self.ttl = ttl
    self.payload = payload

  def convertToPacket(self):
    packet = ""
    packet += "" + str(self.seq) + str(self.ack) + str(self.ttl) + self.payload
    return packet
  
  def convertToPacketPlus(self):
    packet = ""
    packet += "" + str(self.seq) + "." + str(self.ack) + "." + str(self.ttl) + "." + self.payload
    return packet