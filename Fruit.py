__author__ = "Jason, Evan, Patrick, Christina"
__version__ = 1.0

'''Fruit class - doesn't do much besides sit and decompose.'''

from Organism import Organism

DECAY_RATE = 1

class Fruit(Organism):

    def __init__(self, startingEnergy):
        '''Creates a new Fruit with the specified amount of energy.'''
        self.__type__ = "Fruit"
        Organism.__init__(self, startingEnergy, startingEnergy, DECAY_RATE)


    def loseEnergy(self):
        '''Decreases the fruit's energy by its decay rate, returns the amount of energy lost in case the World needs to refer to it.'''
        Organism.loseEnergy(self)
        self.updateEnergy()


    def updateEnergy(self):
        '''Update's the fruit's smell so that it is proportional to its energy - this will mean that critters will seek out fruit with more energy.'''
        self.smell = self.energy
