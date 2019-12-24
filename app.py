from Socket import sendMessage
from Initialaze import Initialaze

def onMessageRecieved(nickname, message, socket):
  print(nickname + ": " + message)
  if message == "selam":
    sendMessage(socket, "Ooooooooooo aleykum selam kardeşim.")
  elif message == "abi":
    sendMessage(socket, "@" + nickname + " efendim kardeşim.")
  elif message == "sa":
    sendMessage(socket, "@" + nickname + " aleykum selam kardeşim.")
  elif message == "naber":
    sendMessage(socket, "@" + nickname + " iyidir asıl seni sormalı kardeşim.")
  elif "!raffle" in message:
    sendMessage(socket, "@" + nickname + " SantaHat 70cl Yeni Rakı yılbaşı çekilişine katıldınız.")

client = Initialaze(onMessageRecieved)
client.connect()