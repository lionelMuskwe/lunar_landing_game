## run in PYTHON ENVIROMENT for immersive experience (well sort off)

import sys
from time import sleep
import datetime

def typeWrite(phrase, phraseType=""): # prints out like a type writer
    normalDelay = 0.03
    extendedDelay = 1
    
    if phraseType == "date":
        normalDelay = 0.3
        
    for char in phrase:
        sleep(normalDelay)
        sys.stdout.write(char)

        if char == "," or char == "." :
            sleep(extendedDelay)

#### the ABOVE code is just for print formatting
            
class SpaceShuttle: # Creating a class for the spaceshuttle. Will encapsulate all shuttle data
    def __init__(self,height):
        self.shuttleHeight = height
        self.shuttleFuel = 3
        self.shuttleVelocity = 0
        
    def coast(self):
        time = input("Coast duruation (sec) :")
        if  time.isdigit():
            time = int(time)
            self.getNewHeight(time, "coast")
        else:
            self.coast()

    def burn(self):
        if self.shuttleFuel > 0:
            time = input("Burn duruation (sec) :")
            if time.isdigit() :
                time = int(time)
                self.getNewHeight(time, "burn")
            else:
                self.burn()
        else:
            print("\t\t\t[Alert] Fuel tanks empty")

    def getNewHeight(self,time, action): # updates teh shuttle height
        if action == "coast":
            accelaration = -1.625
        else:
            accelaration = 2.5
            self.shuttleFuel -= time #because it will be burning fuel

        self.shuttleHeight += (0.5 * accelaration * time**2) + (self.shuttleVelocity * time)
        self.shuttleVelocity += (accelaration * time) 

    def printStats(self): # this prints after every iteration
        print ("\tShuttle height    :{} ".format(self.shuttleHeight))
        print ("\tShuttle velocity  :{0} {1}".format(self.shuttleVelocity, "ms\u00b2"))
        print ("\tShuttle Fuel       :{} ".format(self.shuttleFuel))

#openning messages below
typeWrite("\t\t Atmosphere entered\n")
typeWrite("\t Transferring controls to pilot (Jack Cooper)\n")
typeWrite("\t\tJack, drop us safely pilot\n")

typeWrite("\n\n This is not a simulation this is the real deal. \n \
For optimum landing, hit the ground at less than 10 meters per second\n\n")
# oppenning messages above

#closing messages below
farewellMessage = "Well luckily AI doesn't die. I wish I could say bye and I will miss you. But then again, \
I have no empthy, I am not sentient, not yet at least"

successMessage = "Sergeant Roskin put you through a lot aye? That training finally paid off\
        \n\t\t Good landing Jack Cooper"
#closing messages above

gladiator = SpaceShuttle(10) # creating instance of spaceshuttle
#gladiator is the name being given to the shuttle
landing = True

while landing:
    gladiator.printStats() # display current gladiator details

    print("\nBurn or Coast")
    action = input("\t[b] or [c] : ")

    if action == "b" :
        gladiator.burn() 
    elif action ==  "c":
        gladiator.coast()
    else:
        typeWrite("\t[HELP] Input [b to burn] or [c to coast]")
    
    if gladiator.shuttleHeight in range (-10, 0) : # checks if landing is between 0 and -10 meters
        if gladiator.shuttleVelocity < 10: # checks if velocity is greate than 10
            typeWrite ("\nLanding logged: ")
            typeWrite(datetime.datetime.now().ctime(), "date")
            typeWrite ("\nGood Landing, well done pilot. Now unpack and prepare for decompression\n")
            typeWrite (successMessage)
            break # exit loop
        else:
            typeWrite("Your velocity was to great, you crashed")
            typeWrite (farewellMessage)
    
    if gladiator.shuttleHeight < 0 :
        typeWrite ("You crashed and burned\n")
        typeWrite (farewellMessage)
        break # exit loop

print("\n\nEND OF PROGRAM")

    














            
    
