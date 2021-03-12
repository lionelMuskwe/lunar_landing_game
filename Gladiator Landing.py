## run in PYTHON ENVIROMENT for immersive experience (well sort off)

import sys
from time import sleep
import datetime

def typeWrite(phrase, phraseType=""): # prints out like a type writer
    normalDelay = 0.0 #0.03
    extendedDelay = 0.0 #1
    
    if phraseType == "date":
        normalDelay = 0.3
        
    for char in phrase:
        sleep(normalDelay)
        sys.stdout.write(char)

        if char == "," or char == "." :
            sleep(extendedDelay)

#### the ABOVE code is just for print styling
            
class SpaceShuttle: # Creating a class for the spaceshuttle. Will encapsulate all shuttle data
    def __init__(self,altitude):
        self.shuttleAltitude = altitude
        self.shuttleFuel = 90
        self.shuttleVelocity = 0
        
    def coast(self):
        time = input("Coast duruation (sec) :")
        if  time.isdigit():
            time = int(time)
            self.getNewAltitude(time, "coast")
        else:
            self.coast()

    def burn(self):
        if self.shuttleFuel > 0:
            time = input("Burn duruation (sec) :")
            if time.isdigit() :
                time = int(time)
                if time < self.shuttleFuel:
                    self.getNewAltitude(time, "burn")
                else:
                    print("[ERROR] Trying to use more fuel than available\n")
            else:
                self.burn()
        else:
            print("\t\t\t[Alert] Fuel tanks empty")

    def getNewAltitude(self,time, action): # updates teh shuttle altitude
        if action == "coast":
            accelaration = -1.625
        else:
            accelaration = 2.5
            self.shuttleFuel -= time #because it will be burning fuel

        self.shuttleAltitude += (0.5 * accelaration * time**2) + (self.shuttleVelocity * time)
        self.shuttleVelocity += (accelaration * time) 

    def printStats(self): # this prints after every iteration
        print ("\tShuttle altitude    :{0}{1}".format(self.shuttleAltitude, " meters"))
        print ("\tShuttle velocity  :{0} {1}".format(self.shuttleVelocity, "m/s"))
        print ("\tShuttle Fuel       :{} liters".format(self.shuttleFuel))

#openning messages below
typeWrite("\t\t Atmosphere entered\n")
typeWrite("\t Transferring controls to pilot (Jack Cooper)\n")
typeWrite("\t\tJack, drop us safely pilot\n")

typeWrite("\n\n This is not a simulation this is the real deal. \n \
For optimum landing, hit the ground at less than 10 meters per second\n\n")

typeWrite("COAST to increase fall speed \n")
typeWrite("BURN to reduce fall speed. If you burn to much, you may start gaining altitude \n\n")
# oppenning messages above

#closing messages below
farewellMessage = "Well luckily AI doesn't die. I wish I could say bye and I will miss you. But then again, \
I have no empthy, I am not sentient, not yet at least"

successMessage = "Sergeant Roskin put you through a lot aye? That training finally paid off\
        \n\t\t Good landing Jack Cooper"
#closing messages above

# The program begins below

#gladiator is the name being given to the shuttle
landing = True
gameRunning = True

while gameRunning:
    gladiator = SpaceShuttle(1000) # creating instance of spaceshuttle
    while landing:
        gladiator.printStats() # display current gladiator details

        print("\nBurn or Coast")
        action = input("\t[b] or [c] : ")

        if action == "b" :
            gladiator.burn() 
        elif action ==  "c":
            gladiator.coast()
        else:
            typeWrite("\t[HELP] Input [b to burn] or [c to coast]\n")
        
        if gladiator.shuttleAltitude < 0 : # checks if shuttle has hit the ground
            if gladiator.shuttleVelocity > -10: # checks if velocity is less than 10
                typeWrite ("\nLanding logged: ")
                typeWrite(datetime.datetime.now().ctime(), "date")
                typeWrite ("\nGood Landing, well done pilot. Now unpack and prepare for decompression\n")
                typeWrite (successMessage)
                break # exit loop
            else:
                typeWrite("\nYou CRASHED with a velocity of {0}{1}".format(gladiator.shuttleVelocity, "m/s"))
                typeWrite("Your final altitude would have been {} meters \n".format(gladiator.shuttleAltitude))
                print("me")
                typeWrite (farewellMessage)
                break

    playAgain = input("\n\n\t\tWant to play again? [y or n] :")
    if playAgain in ["n", "no", "nop"]:
        break
    else:
        print("\n\n >>>LET'S try again\n")
        print("[Hint : Try and land between [Hit the ground with a speed lower than 10m/s ]\n")

print("\n\nEND OF PROGRAM")

    














            
    
