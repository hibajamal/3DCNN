class Particle(object):
  def __init__(self, currPos, velocity, gbest, pbest):
    # all will be of type PosVector
    self.currPos = currPos 
    self.velocity = velocity
    self.gbest = gbest
    self.pbest = pbest
