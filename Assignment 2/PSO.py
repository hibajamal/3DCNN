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

class Swarm:
	def __init__(self):
