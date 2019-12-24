import string
from settings import CHANNEL

def getUser(line):
  try:
    seperate = line.split(':', 2)
    user = seperate[1].split("!", 1)[0]
    return user
  except:
    return None

def getMessage(line):
  try:
    seperate = line.split(":", 2)
    message = seperate[2]
    return message
  except:
    return None

def sendMessage(s, message):
  messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
  s.send((messageTemp + "\r\n").encode())
  print("Sent: " + messageTemp)