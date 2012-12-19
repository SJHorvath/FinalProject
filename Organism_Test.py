import Organism
import unittest

class Organism_Test(unittest.TestCase):

	def setUp(self):
		self.test_organism=Organism.Organism(1,1,1)

	def test_getEnergy(self):
		energy = self.test_organism.getEnergy()
		self.assertEquals(energy,1)

	def test_getSmellRadius(self):
		#problems with this one, see comment in organism.py
		smell = self.test_organism.getSmellRadius()
		self.assertEquals(smell,1)

	def test_loseEnergy(self):
		metabolism = self.test_organism.loseEnergy()
		self.assertEquals(metabolism,1)

if __name__ == '__main__':
    unittest.main()