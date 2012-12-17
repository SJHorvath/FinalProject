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

	def createMatrix(self, width, height):
		'''Creates list of lists (matrix).'''
		self.width = width
		self.height = height
		for i in range(height):
			column = []
			self.rows.append(column)
		self.fillMatrix(width)

	def fillMatrix(self, width):
		'''Fills matrix with zeros'''
		for column in self.rows:
			for x in range(width):
				column.append(0)

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
		pass

	def matrixAddBlock(self, x, y):
		'''adds a block at a certain place on the grid.'''
		#adjusted for user-friendliness
		column = self.rows[x]
		column[y] = -1

	def matrixAddFruit(self, x, y):
		'''adds a fruit at a certain place on the grid.'''
		column = self.rows[x]
		column[y] = 2

	def matrixAddCritter(self, x, y):
		'''adds a critter at a certain place on the grid.'''
		column = self.rows[x]
		column[y] = 3

	def randomCoordinate(self):
		x = random.randrange(0, self.width)
		y = random.randrange(0, self.height)
		if self.isEmpty(x, y):
			return (x, y)
		else:
			return self.randomCoordinate()

	def isEmpty(self, x, y):
		'''Checks if a coordinate is filled.  If it is empty (0), returns True.'''
		column = self.rows[x]
		if column[y] == 0:
			return True
		else:
			return False

if __name__ == "__main__":
	myFrame = MainFrame()
	myFrame.createMatrix(2, 2)
	myFrame.matrixAddBlock(0, 0)
	myFrame.matrixAddFruit(0, 1)
	myFrame.matrixAddCritter(1, 1)
	myFrame.printMatrix()
