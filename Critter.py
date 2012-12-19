__author__ = "Jason and Evan"
__version__ = 6.9

import random
from Organism import Organism

MATING_THRESHOLD = 40
HUNGER_THRESHOLD = 30
METABOLISM = 1

class critter(Organism):

    def __init__(self, startingEnergy, senseOfSmell, startingSmell):
        Organism.__init__(self, startingEnergy, startingSmell, METABOLISM)

        self.sense = senseOfSmell
        self.hungerThreshold = HUNGER_THRESHOLD 
        self.matingThreshold = MATING_THRESHOLD
        self.checkHunger()


    def getSmellDistance(self):
        return self.sense

        
    def decide(self, critterTuple, fruitTuple):

        if self.hungry:
            self.pickHighest(fruitTuple)
        else:
            self.pickHighest(critterTuple)

        
    def iterate(self, passed):
        if passed.__type__ == "Critter":
            self.mate(passed)
        elif passed.__type__ == "Fruit":
            self.eat(passed)
        else:
            pass

        self.loseEnergy()


    def loseEnergy(self):
        Organism.loseEnergy(self)
        self.checkHunger()

        
    def checkHunger(self):
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

        if choiceList[0][0] != -1:
            return choiceList[0][1]
