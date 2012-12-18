__author__ = "Jason, Evan, Patrick, Christina"
__version__ = 1.0

'''Fruit class - doesn't do much besides sit and decompose.'''

from Organism import Organism

DECAY_RATE = 1
SMELL = 1

class Fruit(Organism):

    def __init__(self, startingEnergy, startingSmell):
        Organism.__init__(self, startingEnergy, SMELL, DECAY_RATE)
