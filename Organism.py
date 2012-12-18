__author__ = "Jason, Evan, Patrick, Christina"
__version__ = 1.0

'''Superclass which defines the functions shared by both fruit and critters.'''

class Organism:

    def __init__(self, startingEnergy, startingSmell, startingMetabolism):
        self.energy = startingEnergy
        self.smell = startingSmell
        self.metabolism = startingMetabolism


    def getEnergy(self):
        return self.energy

    
    def getSmellRadius(self):
        return self.smellRadius


    def loseEnergy(self):
        self.energy -= self.metabolism
        return self.metabolism
