from PosVector import PosVector;
from Particle import Particle;
from Fly import Fly;

class Swarm(object):
  def __init__(self, pop_size,lowerB, xlim, ylim, inertia, c1, c2):
    self.pop_size = pop_size
    self.particles = [0 for i in range(pop_size)]
    self.flies = [0 for i in range(pop_size)]
    self.gbest = PosVector(0, 0)
    self.inertia = inertia
    self.c1 = c1
    self.c2 = c2
    # xlim and ylim are dimensions of the screen
    self.xlim = xlim
    self.ylim = ylim
    self.lowerB = lowerB
    # random position where food source is
    self.foodSource = PosVector(random(self.lowerB, self.xlim), random(0, self.ylim))
    print("Food Source placed at:", self.foodSource.x, ",", self.foodSource.y)

  def fitnessFunc(self, particle):
    # fitness is inverse of distance
    import math
    f = (math.sqrt((particle.x - self.foodSource.x)**2 +(particle.y - self.foodSource.y)**2))
    return f

  def addVectors(self, vectors):
    cx, cy = 0, 0
    for i in range(len(vectors)):
      cx += vectors[i].x
      cy += vectors[i].y
    return PosVector(cx, cy)

  def subtVectors(self, vec1, vec2):
    return PosVector(vec1.x - vec2.x, vec1.y - vec2.y)

  def init_population(self):
    for i in range(self.pop_size):
      # initialize a random position vector
      pos = PosVector(random(0, self.xlim), random(0, self.ylim))
      # initialize random velocity
      vel = PosVector(random(-1, 1), random(-1, 1))
      # calc if gbest is to be updated
      if self.fitnessFunc(self.gbest) < self.fitnessFunc(pos):
        self.gbest = pos
      # no movement yet so pbest = original position
      self.particles[i] = Particle(pos, vel, self.gbest, pos)
      #print(i)
      self.flies[i] = Fly(pos.x, pos.y, vel.x, vel.y)

  # main loop to run Particle Swarm Optimization
  def PSO(self, iterations):
      #for j in range(iterations):
      lst = []
      for i in range(self.pop_size):
        # calculate fitness of each particle
        c = self.fitnessFunc(self.particles[i].currPos) 
        lst.append(c)
        # compare and replace with pbest and gbest
        if c < self.fitnessFunc(self.particles[i].pbest):
          self.particles[i].pbest = self.particles[i].currPos
        if c < self.fitnessFunc(self.gbest):
          self.gbest = self.particles[i].currPos
          self.particles[i].gbest = self.particles[i].currPos

        # Move all the particles now
        r1, r2 = random(0, 1.0), random(0, 1.0)
        # terms to attain new velocity
        t1 = self.particles[i].velocity.mulC(self.inertia)
        t2 = self.subtVectors(self.particles[i].pbest, self.particles[i].currPos).mulC(self.c1*r1)
        t3 = self.subtVectors(self.gbest, self.particles[i].currPos).mulC(self.c2*r2)
        # update velocity
        self.particles[i].velocity = self.addVectors([t1, t2, t3])
        # add velocity to current position
        self.particles[i].currPos =  self.addVectors([self.particles[i].currPos, self.particles[i].velocity])
        self.flies[i].draw(self.particles[i].currPos.x, self.particles[i].currPos.y)
      #print("avg:", sum(lst)/len(lst), "\nNext iteration:", j+1)
