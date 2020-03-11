
class Fly(object):
    def __init__(self, x, y, vx, vy):
        print("Fly Object generated")
        self.charge = 0.0; # amount of deposit
        self.x = x;
        self.y = y;
        self.vx = vx
        self.vy = vy
        self.r = int(random(0,255))
        self.b =  int(random(0,255))
        self.g = int(random(0, 255));
        
    def draw(self, x, y):        
        self.x = x
        self.y = y
        
        self.x = constrain(self.x, 0, width-1);
        self.y = constrain(self.y, 0, height-1);
        # Trajectory
        noStroke()
        fill(self.r, self.g, self.b)
        
        ellipseMode(CENTER);
        ellipse(self.x, self.y, 15, 13);
        fill(32,45,67)
        fill(255,255,255)
        radius = 13
        ellipse(self.x-radius + radius*0.7, self.y-radius+radius*0.7+2, 6,6)
        #ellipse(self.x+radius - radius*0.7,  self.y-radius+radius*0.7+2, 6,6)
        #ellipse()
