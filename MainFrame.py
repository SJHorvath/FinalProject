'''This is the main document which runs and maintains the 'world'.'''
__author__ = "Julian Katz, RJ Silberman, and Jay Batavia"
__version__ = 1.0

import random
from Critter import Critter
from Fruit import Fruitf

#empty = 0
#block = -1
#fruit = 2
#critter = 3

class MainFrame:

	def __init__(self):
		self.rows = []
		self.critterList = []
		self.fruitList = []
		self.width = 0
		self.height = 0
		self.totalEnergy = 0
		self.energyLimit = 2000
		self.critterCounter = 0
		self.fruitCounter = 0

	def createMatrix(self, width, height):
		'''Creates list of lists (matrix).'''
		self.width = width
		self.height = height
		for i in range(height):
			row = []
			self.rows.append(row)
		self.fillMatrix(width)

	def fillMatrix(self, width):
		'''Fills matrix with zeros'''
		for i in range(len(self.rows)):
			for x in range(self.width):
				if i == 0 or i == len(self.rows) - 1:
					self.rows[i].append(-2)
				elif x == 0 or x == self.width - 1:
					self.rows[i].append(-2)
				else:
					self.rows[i].append(0)

	def getMatrix(self):
		'''returns the matrix'''
		return self.rows

	def printMatrix(self):
		'''prints matrix neatly.'''
		for row in self.rows:
			print row

	def createVisuals(self):
		'''Calls visual functions.'''
		pass

	def createCritter(self, startingEnergy, smellRadius, startingSmell):
		'''adds a critter at a random spot on the grid.'''
		x, y = self.randomCoordinate()
		row = self.rows[x]
		row[y] = 3
		individualCritter = [Critter(startingEnergy, smellRadius, startingSmell), x, y]
		self.critterList.append[individualCritter]

	def createFruit(self):
		'''adds a fruit at a random spot on the grid.'''
		x, y = self.randomCoordinate()
		row = self.rows[x]
		row[y] = 2
		#create fruit
		#set fruit location (object)
		#add fruit to self.fruitList

	def createBlock(self):
		'''adds a block at a random spot on the grid.'''
		x, y = self.randomCoordinate()
		row = self.rows[x]
		row[y] = -1

	def randomCoordinate(self):
		x = random.randrange(1, self.width - 1)
		y = random.randrange(1, self.height - 1)
		if self.isEmpty(x, y):
			return (x, y)
		else:
			return self.randomCoordinate()

	def isEmpty(self, x, y):
		'''Checks if a coordinate is filled.  If it is empty (0), returns True.'''
		row = self.rows[x]
		if row[y] == 0:
			return True
		else:
			return False

	def createRadius(self, x, y, radius):
		radiusPoints = []
		for i in range(x - radius, x + radius):
			for z in range(y - radius, y + radius):
				if i >= 0 and z >= 0:
					if i < self.width and z < self.height:
						coordinate = (i, z)
						radiusPoints.append(coordinate)
		return radiusPoints

	def maintainTotalEnergy(self):
		if self.totalEnergy < (self.energyLimit - 10):
			createFruit()
			self.totalEnergy += 10
			maintainTotalEnergy()

	def collide(self, object1, object2):
		pass

	def createCritters(self, number):
		'''Creates a certain number of critters, with sequential names'''
		names = []
		for i in range(number):
			names.append(self.generateName("c"))
		for name in names:
			createCritter()

	def generateName(self, type):
		if type == "c":
			nameString = "Critter%i" % (self.critterCounter)
			self.critterCounter += 1
		if type == "f":
			nameString = "Fruit%i" % (self.fruitCounter)
			self.fruitCounter += 1
		return nameString

	def start(self):
		self.createCritters(10)

		pass

	def iterate(self):
		self.maintainTotalEnergy()

	# def makeHungerList(self, object):
	# 	'''creates a list of 4 values, containing the specified 
	# 	critter's desire to go, in order, left, up, right, and down'''
	# 	hungerList = [0, 0, 0, 0]
	# 	#these values are hardcoded
	# 	#these should be obtained from the object
	# 	#x, y = object.getLocation()
	# 	x = 2
	# 	y = 3
	# 	#radius should also be obtained from the object
	# 	#radius = object.getRadius()
	# 	radius = 3
	# 	radiusList = createRadius(x, y, radius)

	# 	for fruit in self.fruitList:
	# 		#get fruitLocation
	# 		#if fruitLocation matches on of the radiusList
	# 			#desire = distanceFromObject
	# 			#made for both x and y and added
	# 			#to the correct parts of the hungerList

	# def makeHornyList(self, object):
	# 	'''creates a list of 4 values, containing the specified 
	# 	critter's desire to go, in order, left, up, right, and down'''
	# 	hornyList = [0, 0, 0, 0]
	# 	#these values are hardcoded
	# 	#these should be obtained from the object
	# 	#x, y = object.getLocation()
	# 	x = 2
	# 	y = 3
	# 	#radius should also be obtained from the object
	# 	#radius = object.getRadius()
	# 	radius = 3
	# 	radiusList = createRadius(x, y, radius)

	# 	#check the radiusList against the locations of all the objects in 
	# 	#the object lists
	# 	for critter in self.critterList:
	# 		#get critter location
	# 		#if critterLocation matches one of the radiusList
	# 			#smelly = critter.getSmelly()
	# 			#desire = smelly - distanceFromObject
	# 			#this should be made for both the x and y, and added 
	# 			#to the correct parts of hornyList

if __name__ == "__main__":
	myFrame = MainFrame()
	myFrame.createMatrix(8, 8)
	# print myFrame.createRadius(1, 1, 20)
	myFrame.printMatrix()
