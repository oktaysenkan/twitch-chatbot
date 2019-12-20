import string

def getUser(line):
  try:
    seperate = line.split(':', 2)
    user = seperate[1].split("!", 1)[0]
    return user
  except:
    return "Unknown error"

def getMessage(line):
  try:
    seperate = line.split(":", 2)
    message = seperate[2]
    return message
  except:
    return "Unknown error"
