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

	def createCritter(self):
		pass

	def createFruit(self):
		x, y = self.randomCoordinate()
		pass

	def matrixAddBlock(self, x, y):
		'''adds a block at a certain place on the grid.'''
		#adjusted for user-friendliness
		row = self.rows[x]
		row[y] = -1

	def matrixAddFruit(self, x, y):
		'''adds a fruit at a certain place on the grid.'''
		row = self.rows[x]
		row[y] = 2

	def matrixAddCritter(self, x, y):
		'''adds a critter at a certain place on the grid.'''
		row = self.rows[x]
		row[y] = 3

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



if __name__ == "__main__":
	myFrame = MainFrame()
	myFrame.createMatrix(5, 8)
	myFrame.matrixAddBlock(0, 0)
	myFrame.matrixAddFruit(0, 1)
	myFrame.matrixAddCritter(1, 1)
	# print myFrame.createRadius(1, 1, 20)
	myFrame.printMatrix()
