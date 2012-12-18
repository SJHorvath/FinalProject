import random  

class critter(Object):

	def __init__(self, startingEnergy, startingSmell, smellRadius, location, hungryLimit, hornyLimit):
		self.energy = startingEnergy
		self.smellStrength = startingSmell
		self.smellRadius = smellRadius
		self.metabolism = 1
		self.location = location
		self.hungryLimit = hungryLimit		
		self.hornyLimit = hornyLimit
		self.hungry == true
 
'''takes in two tuples containing the smell values for critters and fruits, tailored to this critters smellingradius'''	
	def decide(self, critter, fruit):
		'''chooses the highest fruit value if it is hungry, and returns 0-3 as a direction decision'''		
		if self.hungry:			
			i = 0			
			for number in fruit:
				if number > i
					i = number
			#get the slot number for the value i
			return slotnumber			 			
			self.energy -= self.metabolism			
		'''chooses the highest critter value if it is horny, and returns 0-3 as a direction decision'''		
		else:
			i = 0	
			j = 0			
			for number in critter:
				if number > i
					i = number
			#get the slot number for the value i
			return slotnumber
			self.energy -= self.metabolism

	def iterate(self, passed):		
		'''	'''
		if passed = critter:		
			if self.hungry != true:
				if self.energy < self.hungryLimit:
					self.hungry == true
			if self.hungry:				
				if self.energy > self.hornyLimit:
					self.hungry == false
				
			if self.hungry == false: 	
				smelly, smelling, hungry, horny = critter #this will be a list
				newEnergy = self.energy/2
				newSmelly = 0				
				if smelly > self.smellStrength:
					newSmelly = random.random((self.smellStrength-1), (smelly+1))
				else:
					newSmelly = random.random((smelly-1), (self.smellStrength+1))
				newSmelling = 0
				if smelling > self.smellRadius:
					newSmelling = random.random((self.smellRadius-1), (smelling+1))
				else:
					newSmelling = random.random((smelling-1), (self.smellRadius+1))
				newHungry = 0 
				if hungry > self.hornyLimit:
					newHorny = random.random((self.hornyLimit-1), (horny+1))
				else:
					newHorny = random.random((horny-1), (self.hornyLimit+1))
				newHorny = 0
				if horny > self.hornyLimit:
					newHorny = random.random((self.hornyLimit-1), (horny+1))
				else:
					newHorny = random.random((horny-1), (self.hornyLimit+1))
				return (newSmelly, newSmelling, newHungry, newHorny)
				self.energy = self.energy/2
			else:
				self.energy -= self.metabolism
		if passed = fruit:
			self.energy += 10
			if self.hungry != true:
				if self.energy < self.hungryLimit:
					self.hungry == true
			if self.hungry:				
				if self.energy > self.hornyLimit:
					self.hungry == false
		else:
			pass	
		
class fruit(Object):

	def __init__(self, location):
		self.energy = 10
		self.location = location
