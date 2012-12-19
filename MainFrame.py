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
		self.fruitEnergy = 10
		self.critterEnergy = 100

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
		self.totalEnergy += self.critterEnergy

	def deleteCritter(self, index):
		self.critterList.pop(index)
		totalEnergy += -self.critterEnergy

	def createFruit(self):
		'''adds a fruit at a random spot on the grid.'''
		x, y = self.randomCoordinate()
		row = self.rows[x]
		row[y] = 2
		individualCritter = [Critter(startingEnergy, smellRadius, startingSmell), x, y]
		self.critterList.append[individualCritter]
		self.totalEnergy += self.fruitEnergy

	def deleteFruit(self, index):
		self.fruitList.pop(index)
		totalEnergy += -self.fruitEnergy

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
		if self.totalEnergy < (self.energyLimit - self.fruitEnergy):
			createFruit()
			self.totalEnergy += self.fruitEnergy
			maintainTotalEnergy()

	def fruitCollide(self, critterIndex, fruitIndex):
		critterX = self.critterList[critterIndex][1]
		critterY = self.critterList[critterIndex][2]
		fruitX = self.fruitList[fruitIndex][1]
		fruitY = self.fruitList[fruitIndex][2]
		if critterX == fruitX and critterY == fruitY:
			return True
		else:
			return False

	def critterCollide(self, index1, index2):
		x1 = self.critterList[index1][1]
		y1 = self.critterList[index1][2]
		x2 = self.critterList[index2][1]
		y2 = self.critterList[index2][2]

		set1 = createRadius(x1, y1, 1)
		set2 = createRadius(x2, y2, 1)

		for i in range(len(set1)):
			if set1[i] = (x2, y2):
				critter1 = 
		for z in range(len(set2)):
			if set2[z] = (x1, y1):
				return True
		return False

	def createInitialCritters(self, number):
		'''Creates a certain number of critters, with sequential names'''
		for i in range(number):
			startingEnergy = randRange(100, 130)
			smellRadius = randRange(1, 5)
			startingSmell = randRange(1, 5)
			self.createCritter(startingEnergy, smellRadius, startingSmell)

	def generateName(self, type):
		if type == "c":
			nameString = "Critter%i" % (self.critterCounter)
			self.critterCounter += 1
		if type == "f":
			nameString = "Fruit%i" % (self.fruitCounter)
			self.fruitCounter += 1
		return nameString

	def start(self):
		for i in range(8):
			self.createBlock()
		self.createInitialCritters(10)
		self.maintainTotalEnergy

	def iterate(self):
		self.maintainTotalEnergy()

	def makeHungerList(self, index):
		'''creates a list of 4 values, containing the specified 
		critter's desire to go, in order, left, up, right, and down'''
		hungerList = [0, 0, 0, 0]
		critter = self.critterList[index]
		x = critter[1]
		y = critter[2]
		radius = critter[0].getSmellDistance()
		radiusList = createRadius(x, y, radius)

		for fruit in self.fruitList:
			fruitX = fruit[1]
			fruitY = fruit[2]
			for coordinates in radiusList:
				if (fruitX, fruitY) == coordinates:
					desireX = fruitX - x
					desireY = fruitY - y
					if desireX > 0:
						hungerList[2] += desireX
					else:
						hungerList[0] += abs(desireX)
					if desireY > 0:
						hungerList[1] += desireY
					else:
						hungerList[3] += abs(desireY)
		return hungerList

	def makeHornyList(self, index):
		'''creates a list of 4 values, containing the specified 
		critter's desire to go, in order, left, up, right, and down'''
		hornyList = [0, 0, 0, 0]
		myCritter = self.critterList[index]
		x = myCritter[1]
		y = myCritter[2]
		radius = myCritter[0].getSmellDistance()
		radiusList = createRadius(x, y, radius)

		for critter in self.critterList:
			critterX = critter[1]
			critterY = critter[2]
			for coordinates in radiusList:
				if (critterX, critterY) == coordinates:
					desireX = critterX - x
					desireY = critterY - y
					if desireX > 0:
						hornyList[2] += desireX
					else:
						hornyList[0] += abs(desireX)
					if desireY > 0:
						hornyList[1] += desireY
					else:
						hornyList[3] += abs(desireY)
		return hornyList

if __name__ == "__main__":
	myFrame = MainFrame()
	myFrame.createMatrix(8, 8)
	# print myFrame.createRadius(1, 1, 20)
	myFrame.printMatrix()
