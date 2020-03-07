import matplotlib
from matplotlib import pyplot as plt
import time
import random as rand

class PosVector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def updatePos(self, x, y):
		self.x = x
		self.y = y

	# if vector is to be scaled by a single constant
	def mulC(self, c):
		x = self.x*c 
		y = self.y*c
		return PosVector(x, y)

	# if vector is to be scaled differently in X and Y
	def mulXY(self, cx, cy):
		x = self.x*cx 
		y = self.y*cy
		return PosVector(x, y)

class Particle(PosVector):
	def __init__(self, currPos, gbest, pbest):
		# all will be of type PosVector
		self.currPos = currPos 
		self.gbest = gbest
		self.pbest = pbest

class Swarm:

	def __init__(self, pop_size, xlim, ylim, inertia, c1, c2):
		self.pop_size = pop_size
		self.particles = [0 for i in range(pop_size)]
		self.gbest = PosVector(0, 0)
		self.inertia = inertia
		self.c1 = c1
		self.c2 = c2
		# xlim and ylim are dimensions of the screen
		self.xlim = xlim
		self.ylim = ylim
		# random position where food source is
		self.foodSource = PosVector(rand.randrange(0, self.xlim), rand.randrange(0, self.ylim))
		print("Food Source placed at:", self.foodSource.x, ",", self.foodSource.y)

	def fitnessFunc(self, particle):
		return ((particle.x - self.foodSource.x)**2 +(particle.y - self.foodSource.y)**2)**(1/2)

	def addVectors(self, vectors):
		cx, cy = 0, 0
		for i in range(len(vectors)):
			cx += vectors[0].x
			cy += vectors[0].y
		return PosVector(cx, cy)

	def subtVectors(self, vec1, vec2):
		return PosVector(vec1.x - vec2.x, vec1.y - vec2.y)

	def init_population(self):
		for i in range(self.pop_size):
			# initialize a random position vector
			pos = PosVector(rand.randrange(0, self.xlim), rand.randrange(0, self.ylim))
			# calc if gbest is to be updated
			if self.fitnessFunc(self.gbest) < self.fitnessFunc(pos):
				self.gbest = pos
			# no movement yet so pbest = original position
			self.particles[i] = Particle(pos, pos , self.gbest)

	# main loop to run Particle Swarm Optimization
	def POS(self, iterations):
		fig = plt.figure()
		ax = fig.add_subplot(111)
		fig.show()
		for j in range(iterations):
			lst = []
			for i in range(pop_size):
				# calculate fitness of each particle
				c = self.fitnessFunc(self.particles[i].currPos) 
				lst.append(c)
				# compare and replace with pbest and gbest
				if c > self.fitnessFunc(self.particles[i].pbest):
					self.particles[i].pbest = self.particles[i].currPos
					if c > self.fitnessFunc(self.gbest):
						self.gbest = self.particles[i].pbest
						self.particles[i].gbest = self.gbest

				# Move all the particles now
				r1, r2 = rand.random(), rand.random()
				t1 = self.particles[i].currPos.mulC(self.inertia)
				t2 = self.subtVectors(self.particles[i].pbest, self.particles[i].currPos).mulC(self.c1*r1)
				t3 = self.subtVectors(self.gbest, self.particles[i].currPos).mulC(self.c2*r2)
				self.particles[i].currPos =  self.addVectors([t1, t2, t3])
			print(lst, "\nNext iteration:", j+1)
			ax.plot(lst, color='r')
			fig.canvas.draw()

# pop_size, xlim, ylim, inertia, c1, c2
pop_size = 20
xlim, ylim = 1000, 1000
inertia = 0.7
c1 = 0.5
c2 = 0.2

swarm = Swarm(pop_size, xlim, ylim, inertia, c1, c2)
print("Initializing population...")
swarm.init_population()
print("Particle Swarm Optimization starting...")
swarm.POS(50)
plt.show()