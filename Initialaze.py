import string
from Socket import sendMessage


def joinRoom(s):
  readBuffer = ""
  loading = True
  count = 0;
  while loading:
    readBuffer = readBuffer + (s.recv(1024)).decode()
    temp = readBuffer.split("\n")
    readBuffer = temp.pop()

    for line in temp:
      print(line)
      count = count + 1
      loading = loadingComplete(line, count)
      
  print('Odaya katıldı.')
  #sendMessage(s, "Chat katılma işlemi başarılı.")


def loadingComplete(line, count):
  if(count > 9):
    return False
  else:
    return True