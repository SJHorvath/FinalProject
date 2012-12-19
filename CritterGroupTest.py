import unittest
import Critter

class test_class(unittest.TestCase):

		def setUp(self):
			self.test_critter = Critter.critter(1,1,1,1,1,1,-1)

		def test_decide(self):
			slotnumber = self.test_critter.decide()
			self.assertEquals(slotnumber,range(0-3))

if __name__ == '__main__':
    unittest.main()
		# def test_iterate(self):

		# 	passed = critter
