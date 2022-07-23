import time
import os

def infoStartup():

  print("FissionSys\n")
  #aim to replace these version names with reads from file so code is self aware.
  print("Gui Version: " + "Console-0")
  print("Maths Version: " + "Maths-0")
  print("Output Version: " + "Graphs-0")

  time.sleep(1)

  #to clear console before full UI startup
  try: 
    os.system('CLS') #windows
  except:
    pass
  
  try:
    os.system('clear') #linux
  except:
    print("Error")

def startup():
  input('')



