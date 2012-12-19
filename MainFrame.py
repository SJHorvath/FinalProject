'''This is the main document which runs and maintains the 'world'.'''
__author__ = "Julian Katz, RJ Silberman, and Jay Batavia"
__version__ = 1.0

import random

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
		for row in self.rows:
			for x in range(self.width):
				row.append(0)

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

	def createCritter(self, name):
		'''adds a critter at a random spot on the grid.'''
		x, y = self.randomCoordinate()
		row = self.rows[x]
		row[y] = 3
		#create critter
		#set critter location (object)
		#add critter to self.critterList

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
		x = random.randrange(0, self.width)
		y = random.randrange(0, self.height)
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
		for i in range(1, number + 1):
			nameString = "Critter%i" % (i)
			names.append(nameString)
		for name in names:
			matrixAddCritter(name)


	def start(self):
		#create desired number of critters
		pass

	def iterate(self):
		self.maintainTotalEnergy()

	def makeHungerList(self, object):
		'''creates a list of 4 values, containing the specified 
		critter's desire to go, in order, left, up, right, and down'''
		hungerList = [0, 0, 0, 0]
		#these values are hardcoded
		#these should be obtained from the object
		#x, y = object.getLocation()
		x = 2
		y = 3
		#radius should also be obtained from the object
		#radius = object.getRadius()
		radius = 3
		radiusList = createRadius(x, y, radius)

		for fruit in self.fruitList:
			#get fruitLocation
			#if fruitLocation matches on of the radiusList
				#desire = distanceFromObject
				#made for both x and y and added
				#to the correct parts of the hungerList

	def makeHornyList(self, object):
		'''creates a list of 4 values, containing the specified 
		critter's desire to go, in order, left, up, right, and down'''
		hornyList = [0, 0, 0, 0]
		#these values are hardcoded
		#these should be obtained from the object
		#x, y = object.getLocation()
		x = 2
		y = 3
		#radius should also be obtained from the object
		#radius = object.getRadius()
		radius = 3
		radiusList = createRadius(x, y, radius)

		#check the radiusList against the locations of all the objects in 
		#the object lists
		for critter in self.critterList:
			#get critter location
			#if critterLocation matches one of the radiusList
				#smelly = critter.getSmelly()
				#desire = smelly - distanceFromObject
				#this should be made for both the x and y, and added 
				#to the correct parts of hornyList

if __name__ == "__main__":
	myFrame = MainFrame()
	myFrame.createMatrix(5, 8)
	myFrame.matrixAddBlock(0, 0)
	myFrame.matrixAddFruit(0, 1)
	myFrame.matrixAddCritter(1, 1)
	# print myFrame.createRadius(1, 1, 20)
	myFrame.printMatrix()
	print myFrame.createCritters(10)
