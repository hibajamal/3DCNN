class PosVector(object):
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
