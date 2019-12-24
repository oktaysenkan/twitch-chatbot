import string
from Socket import sendMessage
from Socket import openSocket, sendMessage
from Read import getUser, getMessage

class Initialaze:
  def __init__(self, listener):
    self.socket = openSocket()
    self.listener = listener
    self.readBuffer = ""

  def connect(self):
    loading = True
    while loading:
      self.readBuffer = self.readBuffer + (self.socket.recv(1024)).decode()
      temp = self.readBuffer.split("\r\n")
      self.readBuffer = temp.pop()

      for line in temp:
        loading = self.loadingComplete(line)
    print('Connected to chat room!')
    self.listenChat()

  def listenChat(self):
    while True:
      try:
        self.readBuffer = self.readBuffer + (self.socket.recv(1024)).decode()
        temp = self.readBuffer.split("\r\n")
        self.readBuffer = temp.pop()
      except:
        print("Decode error.")

      for line in temp:
        user = getUser(line)
        message = getMessage(line)

        if user is not None and message is not None:
          self.listener(user, message, self.socket)

  def loadingComplete(self, line):
    if "End of /NAMES list" in line:
      return False
    else:
      return True