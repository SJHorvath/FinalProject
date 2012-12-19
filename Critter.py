__author__ = "Jason and Evan"
__version__ = 6.9

'''Class representing the single type of critter in our life simular. '''

import random
from Organism import Organism

HUNGER_THRESHOLD = 110
METABOLISM = 1

class Critter(Organism):

    def __init__(self, startingEnergy, senseOfSmell, smellRatio, endurance):
        '''Creates a new critter with the specified energy level, sense of smell (as a radius), and smell strength.'''
        self.__type__ = "Critter"
        
        #Initialize all the parameters contained in the Organism superclass
        Organism.__init__(self, startingEnergy, int(startingEnergy/smellRatio), METABOLISM)

        #Set sense of smell radius, hunger and mating thresholds, and energy-to-smell ratio
        self.smellRatio = smellRatio
        self.sense = senseOfSmell
        self.hungerThreshold = HUNGER_THRESHOLD
        self.matingThreshold = HUNGER_THRESHOLD + endurance

        #Sets self.hungry based on energy
        self.hungry = True
        self.checkHunger()


    def getSmellDistance(self):
        '''Returns the distance around the critter that it can smell to sense fruit and other critters.'''
        return self.sense

        
    def move(self, critterList, fruitList):
        '''Takes two lists from the World, containing the total smell of critters and fruit (respectively) in each of the four cardinal directions. The critter then moves toward direction with the strongest smell: if it is hungry, it seeks out fruit. Otherwise, it seeks out other critters to reproduce.'''
        if self.hungry:
            #If the critter is hungry, it checks fruit-smells in each direction.
            return self.pickHighest(fruitList)
            
        else:
            #Otherwise, it checks critter smells.
            return self.pickHighest(critterList)

        
    def processCollision(self, passed):
        '''Takes any objects the critter has colided with from the World. If it has collided with another critter, it returns the traits of any offspring they would have. If it has collided with a fruit, it adds the fruit's energy to its own. In both cases the World is responsible for creating/destroying critters and fruits.'''
        #If we were passed a critter, mate with it.
        if passed.__type__ == "Critter":
            return self.mate(passed)
            
        #If we were passed a fruit, eat it.
        elif passed.__type__ == "Fruit":
            self.eat(passed)


    def loseEnergy(self):
        '''Decreases the critter's energy based on its metabolic rate, returns the amount of energy lost, and updates whether or not it is hungry.'''
        #Superclass method!
        Organism.loseEnergy(self)
        self.checkHunger()
        self.updateSmell()

        
    def checkHunger(self):
        '''Updates whether or not the critter is hungry (if it isn't, it's ready to mate) based on its energy level.'''
        #If it isn't hungry now, check if it should be:
        if not self.hungry:

            if self.energy < self.hungerThreshold:
                #If energy has fallen back below the hunger threshold...
                self.hungry = True
                
        #If it is hungry, check if it's ready to mate instead.
        else:
            if self.energy > self.matingThreshold:
                #If energy is above the ready-to-mate threshold....
                self.hungry = False


    def updateSmell(self):
        '''Updates the strength of the critter's smell based on its energy level and inherited smell-to-energy-ratio trait.'''
        self.smell = int(self.smellRatio * self.energy)


    def mate(self, otherCritter):
        '''Given another critter, returns a tuple of randomly-chosen inherited traits for their child... if the critter is ready to mate. Otherwise, it returns None.'''
        #If it ain't hungry, it's ready to mate!
        if not self.hungry:
            #The other two traits will be chosen randomly, with the values of its two parents used as the range of possible values.
            newRatio = int(self.randomBetween( self.smellRatio-1, otherCritter.smellRatio+1 ))
            newSense = int(self.randomBetween( self.sense-1, otherCritter.sense+1 ))
            newEndurance = int(self.randomBetween( self.getEndurance()-1, otherCritter.getEndurance()+1 ))

            #Make the critter lose energy after mating, to discourage them from staying in the same place and having lots of babbys
            for i in range(2):
                self.loseEnergy()

            #Tuple!
            NRG = self.energy / 2
            return (NRG, newSense, newRatio newEndurance)
        
        else:
            return None


    def randomBetween(self, value1, value2):
        '''Returns a random integer between the two specified values.'''
        #random.triangular() requires that the range to choose from be in the form (smallest value, largest value). This a quick and easy way to sort the two values so this is always true.
        sortingList = [value1, value2]
        sortingList.sort()

        return random.randint(sortingList[0], sortingList[1])


    def getEndurance(self):
        '''Returns the difference between the critter's mating threshold and its go-back-to-being-hungry threshold.'''
        return self.matingThreshold - self.hungerThreshold


    def eat(self, fruit):
        '''Takes the energy of a given fruit and adds it to the critter's own energy. Assumes that the World will destroy the fruit afterward.'''
        self.energy += fruit.getEnergy()
        self.checkHunger()
        self.updateSmell()

        
    def pickHighest(self, choices):
        '''Takes a list of smells for each direction, returns a value correpsonding to the index of the direction with the highest smell. If multiple directions have the same smell value, the critter will choose randomly between them.'''
        directionList = []
        
        #Create a list of tuples, each containing a (smell value, direction it corresponds to) pair...
        for i in range(len(choices)):
            directionList.append((choices[i], i))
    
        #...Which makes it easy to choose the value with the strongest smell while remembering which direction it corresponds to.
        #sort() sorts by the first item in a tuple by default
        directionList.sort(reverse=False)
        print directionList
        spotCheck = []
        for i in range(0, len(directionList)+1):
            	if directionList[3][0] > directionList[3-(i+1)][0]:		
            		j = 0			
            		while j < i:
            			spotCheck.append(3-j)
            			j+=1
        		if len(spotCheck) != 0:
        			choice = random.choice(spotCheck)			
        			return directionList[choice][1]
        			break
        		else:
        			return directionList[3][1]			
        			break
        		break

        #Now, choose a random direction with the "best smell" and return its original index.
       # return directionList[ int(round(random.triangular(0, choiceRange))) ][1]

        #1. Can't return correct direction, only returns random direction
        #2. random direction can include moving to edge
