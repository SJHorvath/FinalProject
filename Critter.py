__author__ = "Jason and Evan"
__version__ = 6.9

import random
from Organism import Organism

MATING_THRESHOLD = 40
HUNGER_THRESHOLD = 30
METABOLISM = 1

class Critter(Organism):

    def __init__(self, startingEnergy, senseOfSmell, startingSmell):
        '''Creates a new critter with the specified energy level, sense of smell (as a radius), and smell strength.'''
        #Initialize all the parameters contained in the Organism superclass
        Organism.__init__(self, startingEnergy, startingSmell, METABOLISM)

        #Set sense of smell radius, hunger, and mating thresholds
        self.sense = senseOfSmell
        self.hungerThreshold = HUNGER_THRESHOLD 
        self.matingThreshold = MATING_THRESHOLD

        #Sets self.hungry based on energy
        self.checkHunger()


    def getSmellDistance(self):
        '''Returns the distance around the critter that it can smell to sense fruit and other critters.'''
        return self.sense

        
    def move(self, critterTuple, fruitTuple):
        '''Takes two tuples from the World, containing the total smell of critters and fruit (respectively) in each of the four cardinal directions.  The critter then moves toward direction with the strongest smell: if it is hungry, it seeks out fruit.  Otherwise, it seeks out other critters to reproduce.'''

        if self.hungry:
            self.pickHighest(fruitTuple)
        else:
            self.pickHighest(critterTuple)

        
    def processCollision(self, passed):
        '''Takes any objects the critter has colided with from the World.  If it has collided with another critter, it returns the traits of any offspring they would have.  If it has collided with a fruit, it adds the fruit's energy to its own.  In both cases the World is responsible for creating/destroying critters and fruits.'''
        #If we were passed a critter, mate with it.
        if passed.__type__ == "Critter":
            self.mate(passed)
            
        #If we were passed a fruit, eat it.
        elif passed.__type__ == "Fruit":
            self.eat(passed)
            
        #Otherwise, do nothing.
        else:
            pass


    def loseEnergy(self):
        '''Decreases the critter's energy based on its metabolic rate, returns the amount of energy lost, and updates whether or not it is hungry.'''
        #Superclass method!
        Organism.loseEnergy(self)
        self.checkHunger()

        
    def checkHunger(self):
        '''Updates whether or not the critter is hungry (if it isn't, it's ready to mate) based on its energy level.'''
        if not self.hungry:
            if self.energy < self.hungerThreshold:
                self.hungry = True
        else:
            if self.energy > self.matingThreshold:
                self.hungry = False


    def mate(self, otherCritter):
        
        if not self.hungry:
            newEnergy = self.energy/2
            newSmell = self.randomBetween( self.smell, otherCritter.getSmell() )
            newSense = self.randomBetween( self.sense, otherCritter.getSmellDistance() )

            return (newEnergy, newSmell, newSense)
        
        else:
            return None


    def randomBetween(self, value1, value2):
        sortingList = [value1, value2]
        sortingList.sort()

        return random.random(sortingList[0] - 1, sortingList[1] + 1)
    

    def eat(self, fruit):
        self.energy += fruit.getEnergy()
        self.checkHunger()


    def pickHighest(self, choices):
        directionList = []

        for i in range(len(choices)):
            directionList.append((choices[i], i))
            
        choiceList.sort()

        #Negative values 
        if choiceList[0][0] >= 0:
            return choiceList[0][1]


    def isReadyToMate(self):
        return not self.hungry
