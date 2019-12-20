import string

from Socket import openSocket, sendMessage
from Initialaze import joinRoom
from Read import getUser, getMessage

s = openSocket()
joinRoom(s)
readBuffer = ""

while True:
  try:
    readBuffer = readBuffer + (s.recv(1024)).decode()
    temp = readBuffer.split("\n")
    readBuffer = temp.pop()
  except:
    print("Unknown error.")

  for line in temp:
    user = getUser(line)
    message = getMessage(line)
    print(user + ": " + message)

    if (message == "selam"):
      sendMessage(s, "Ooooooooooo aleykum selam kardeşim.")