import time
import os
import SimpleFission as simple

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
    
    notComplete = True
    
    #Menu:
        
    while notComplete:
        
        choice = input("Please Choose an Option: \n1. Simple Fission \n2. Placeholder \n3. Placeholder \n")
    
    
        if choice == '1':
            notComplete = False
            simple.start()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        else:
            print("Error. Please Try Again")
            
            time.sleep(1)
            
            #reminder: possibly make the following into a function since it is being reused:
            
            try: 
                os.system('CLS') #windows
            except:
                pass
            
            try:
                os.system('clear') #linux
            except:
                print("Error")


