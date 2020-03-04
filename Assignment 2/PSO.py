import math
import numpy as np
import random as rand

class PosVector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def updatePos(self, x, y):
		self.x = x
		self.y = y

class Particle(PosVector):
	def __init__(self, currPos, gbest, pbest):
		self.currPos = currPos # will be of type PosVector
		self.gbest = gbest
		self.pbest = pbest

	def fitnessFunc(self):
		cost = 0
		return cost

class Swarm:

	def __init__(self, pop_size, xlim, ylim, inertia, c1, c2):
		self.pop_size = pop_size
		self.particles = np.zeros(pop_size)
		self.gbest = PosVector(0, 0)
		self.inertia = inertia
		# xlim and ylim are dimensions of the screen
		self.xlim = xlim
		self.ylim = ylim

	def init_population(self):
		for i in range(self.pop_size):
			# initialize a random position vector
			pos = PosVector(rand.randrange(0, self.xlim), rand.randrange(0, self.ylim))
			# no movement yet so pbest = gbest
			self.particles[i] = Particle(pos, self.gbest , self.gbest)

	# main loop to run Particle Swarm Optimization
	def POS(self, iterations):
		# make it a do while loop
		while iterations:
			for i in range(pop_size):
				# calculate fitness of each particle
				c = self.particles[i].fitnessFunc() 
				# comp and replace w pbest and gbest
				if c > particles[i].pbest:
					particles[i].pbest = particles[i].currPos
					if particles[i].pbest > self.gbest:
						self.gbest = particles[i].pbest
						particles[i].gbest = self.gbest

				# Move all the particles now
				r1, r2 = rand.random(), rand.random()
				particles[i].currPos = inertia*particles[i].currPos + self.c1*r1*(particles[i].pbest - particles[i].currPos) + self.c2*r2(self.gbest - particles[i].currPos)
				