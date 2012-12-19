'''This is the main document which runs and maintains the 'world'.'''
__author__ = "Julian Katz, RJ Silberman, and Jay Batavia"
__version__ = 1.0

import random
from Critter import Critter
from Fruit import Fruit
import math

#empty = 0
#block = -1
#fruit = 2
#critter = 3

class MainFrame:

	def __init__(self):
		self.rows = []
		self.critterList = []
		self.fruitList = []
		self.blockList = []
		self.width = 0
		self.height = 0
		self.totalEnergy = 0
		self.energyLimit = 500
		self.critterCounter = 0
		self.fruitCounter = 0
		self.fruitEnergy = 10
		self.critterEnergy = 100
		self.radius = 3

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
					self.rows[i].append(0)
					self.createCertainBlock(x, i)
				elif x == 0 or x == self.width - 1:
					self.rows[i].append(0)
					self.createCertainBlock(x, i)
				else:
					self.rows[i].append(0)

	def setMatrixValue(self, x, y, value):
		row = self.rows[x]
		row[y] = value

	def getMatrix(self):
		'''returns the matrix'''
		return self.rows

	def printMatrix(self):
		'''prints matrix neatly.'''
		print
		for row in self.rows:
			print row
		print

	def createVisuals(self):
		'''Calls visual functions.'''
		pass

	def createCritter(self, startingEnergy, senseOfSmell, smellRatio, endurance):
		'''adds a critter at a random spot on the grid.'''
		x, y = self.randomCoordinate()
		row = self.rows[x]
		row[y] = 3
		individualCritter = [Critter(startingEnergy, self.radius, smellRatio, endurance), x, y]
		self.critterList.append(individualCritter)
		self.totalEnergy += self.critterEnergy

	def deleteCritter(self, index):
		self.critterList.pop(index)
		self.totalEnergy += -self.critterEnergy

	def createFruit(self):
		'''adds a fruit at a random spot on the grid.'''
		x, y = self.randomCoordinate()
		row = self.rows[x]
		row[y] = 2
		temp = [Fruit(self.fruitEnergy), x, y]
		self.fruitList.append(temp)
		self.totalEnergy += self.fruitEnergy

	def deleteFruit(self, index):
		self.fruitList.pop(index)
		self.totalEnergy += -self.fruitEnergy

	def createBlock(self):
		'''adds a block at a random spot on the grid.'''
		x, y = self.randomCoordinate()
		row = self.rows[x]
		row[y] = -1
		out = (x, y)
		self.blockList.append(out)

	def createCertainBlock(self, x, y):
		row = self.rows[y]
		row[x] = -1
		out = (x, y)
		self.blockList.append(out)

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

	def isOccupied(self, x, y):
		for critter in self.critterList:
			if critter[1] == x and critter[2] == y:
				return True
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

	def createBlockRadius(self, x, y, radius):
		blockRadiusPoints = []
		for i in range(x - radius, x + radius):
			coordinate = (i, y)
			blockRadiusPoints.append(coordinate)
		for z in range(y - radius, y + radius):
			coordinate = (x, z)
			blockRadiusPoints.append(coordinate)
		return blockRadiusPoints

	def maintainTotalEnergy(self):
		while self.totalEnergy < (self.energyLimit - self.fruitEnergy):
			self.createFruit()
			self.totalEnergy += self.fruitEnergy

	def fruitCollide(self, critterIndex, fruitIndex):
		critter = self.critterList[critterIndex]
		fruit = self.fruitList[fruitIndex]
		critterX = critter[1]
		critterY = critter[2]
		fruitX = fruit[1]
		fruitY = fruit[2]
		if critterX == fruitX and critterY == fruitY:
			critter[0].eat(fruit[0])
			deleteFruit[fruitIndex]

	def critterCollide(self, index1, index2):
		critter1 = self.critterList[index1]
		critter2 = self.critterList[index2]
		x1 = critter1[1]
		y1 = critter1[2]
		x2 = critter2[1]
		y2 = critter2[2]

		set1 = self.createRadius(x1, y1, 1)
		set2 = self.createRadius(x2, y2, 1)

		for i in range(len(set1)):
			if set1[i] == (x2, y2):
				myReturn = critter1.mate(critter2)
				if myReturn:
					startingEnergy, smellRadius, startingSmell, endurance = myReturn
					self.createCritter(startingEnergy, smellRadius, startingSmell, endurance)
		for z in range(len(set2)):
			if set2[z] == (x1, y1):
				myReturn = critter1.mate(critter2)
				if myReturn:
					startingEnergy, smellRadius, startingSmell, endurance = myReturn
					self.createCritter(startingEnergy, smellRadius, startingSmell, endurance)

	def createInitialCritters(self, number):
		'''Creates a certain number of critters, with sequential names'''
		for i in range(number):
			startingEnergy = random.randrange(100, 130)
			# senseOfSmell = random.randrange(1, 3)
			senseOfSmell = 2
			smellRatio = random.randrange(1, 5)
			endurance = random.randrange(0, 100, 10)
			self.createCritter(startingEnergy, senseOfSmell, smellRatio, endurance)

	def generateName(self, type):
		if type == "c":
			nameString = "Critter%i" % (self.critterCounter)
			self.critterCounter += 1
		if type == "f":
			nameString = "Fruit%i" % (self.fruitCounter)
			self.fruitCounter += 1
		return nameString

	def start(self):
		# for i in range(8):
		# 	self.createBlock()
		self.createInitialCritters(1)
		self.maintainTotalEnergy()

	def iterate(self):
		toDelete = []
		for i in range(len(self.critterList)):
			item = self.critterList[i]
			critter = item[0]
			hungList = self.makeHungerList(i)
			hornList = self.makeHornyList(i)
			movement = critter.move(hornList, hungList)
			self.myMove(i, movement)
			if critter.getEnergy() == 0:
				toDelete.append[i]
		for value in toDelete:
			self.deleteCritter(value)

		self.maintainTotalEnergy()
		#this return is for the visual people
		return self.rows

	def myMove(self, index, direction):
		print "direction:", direction
		item = self.critterList[index]
		xInit = item[1]
		yInit = item[2]	
		xFinal = item[1]
		yFinal = item[2]
		if direction == 0:
			xFinal += -1
			print "moved"
		if direction == 1:
			yFinal += 1
			print "moved"
		if direction == 2:
			xFinal += 1
			print "moved"
		if direction == 3:
			yFinal += -1
			print "moved"
		self.critterList[index][1] = xFinal
		self.critterList[index][2] = yFinal
		self.setMatrixValue(xFinal, yFinal, 3)
		if not self.isOccupied(xInit, yInit):
			self.setMatrixValue(xInit, yInit, 0)

	def makeHungerList(self, index):
		'''creates a list of 4 values, containing the specified 
		critter's desire to go, in order, left, up, right, and down'''
		hungerList = [0, 0, 0, 0]
		print hungerList
		critter = self.critterList[index]
		x = critter[1]
		print "critter x:", x
		y = critter[2]
		print "critter y:", y
		radius = critter[0].getSmellDistance()
		radiusList = self.createRadius(x, y, radius)
		blockRadiusList = self.createBlockRadius(x, y, radius)
		

		for fruit in self.fruitList:
			fruitX = fruit[1]
			print "fruit x:", fruitX
			fruitY = fruit[2]
			print "fruit y:", fruitY
			for coordinates in radiusList:
				if (fruitX, fruitY) == coordinates:
					desireX = int(math.ceil((float(fruitX) - float(x)) / self.radius))
					desireY = int(math.ceil((float(fruitY) - float(y)) / self.radius))
					if desireX < 0:
						hungerList[2] += abs(desireX)
						print desireX
						# print "1:", hungerList
					if desireX > 0:
						hungerList[0] += abs(desireX)
						print desireX
						# print "2:", hungerList
					if desireY > 0:
						hungerList[1] += abs(desireY)
						print desireY
						# print "3:", hungerList
					if desireY < 0:
						hungerList[3] += abs(desireY)
						print desireY
						# print "4:", hungerList
		for coordinates in self.blockList:
			for radiusCords in blockRadiusList:
				if coordinates == radiusCords:
					print "hello!"
					_x, _y = coordinates
					xdirect = _x - x
					ydirect = _y - y
					if xdirect > 0:
						hungerList[2] += -1
						print "1!"
					if xdirect < 0:
						hungerList[0] += -1
						print "2!"
					if ydirect > 0:
						hungerList[1] += -1
						print "3!"
					if ydirect < 0:
						hungerList[3] += -1
						print "4!"
		# print self.blockList
		print hungerList
		return hungerList

	def makeHornyList(self, index):
		'''creates a list of 4 values, containing the specified 
		critter's desire to go, in order, left, up, right, and down'''
		hornyList = [0, 0, 0, 0]
		myCritter = self.critterList[index]
		x = myCritter[1]
		y = myCritter[2]
		radius = myCritter[0].getSmellDistance()
		radiusList = self.createRadius(x, y, radius)
		blockRadiusList = self.createBlockRadius(x, y, radius)

		for critter in self.critterList:
			critterX = critter[1]
			critterY = critter[2]
			for coordinates in radiusList:
				if (critterX, critterY) == coordinates:
					desireX = int(math.ceil((float(critterX) - float(x)) / self.radius))
					desireY = int(math.ceil((float(critterY) - float(y)) / self.radius))
					if desireX > 0:
						hornyList[2] += desireX
					else:
						hornyList[0] += abs(desireX)
					if desireY > 0:
						hornyList[1] += desireY
					else:
						hornyList[3] += abs(desireY)

		for coordinates in self.blockList:
			for radiusCords in blockRadiusList:
				if coordinates == radiusCords:
					_x, _y = coordinates
					xdirect = _x - x
					ydirect = _y - y
					if xdirect > 0:
						hornyList[2] += -1
					if xdirect < 0:
						hornyList[0] += -1
					if ydirect > 0:
						hornyList[1] += -1
					if ydirect < 0:
						hornyList[3] += -1
		return hornyList

	def printStuff(self):
		print 
		# print "fruits: ", len(self.fruitList)
		# print "critters: ", len(self.critterList)
		# print "total energy: ", self.totalEnergy
		# for critter in self.critterList:
		# 	x = critter[1]
		# 	y = critter[2]
		# 	print (x, y)

#if __name__ == "__main__":
# 	myFrame = MainFrame()
# 	myFrame.createMatrix(6, 6)
# 	myFrame.start()
# 	myFrame.printMatrix()
# 	print
# 	# # print
# 	myFrame.printStuff()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	myFrame.printStuff()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	myFrame.printStuff()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	myFrame.printStuff()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	myFrame.printStuff()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	myFrame.iterate()
# 	myFrame.printMatrix()
# 	# myFrame.iterate()
# 	# myFrame.printMatrix()
# 	# myFrame.iterate()
# 	# myFrame.printMatrix()
# 	# myFrame.iterate()
# 	# myFrame.printMatrix()
