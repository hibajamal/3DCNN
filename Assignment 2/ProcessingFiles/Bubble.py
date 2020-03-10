
class bubble(object):
    def __init__(self, Width, Height):
        self.screenWidth = Width
        self.screenHeight = Height
        self.shadeBlue = [[67, 130, 255], [20, 150, 170], [50, 100, 174]]
        self.lightAngle = [[100, 200, 150], [100, 200, 200], [20, 100, 320], [30, 100, 300]]
        self.shade = [[100,100,255], [100, 100, 174]]
        self.strokeShade = [71, 130, 247, 24]
        self.radiusExt = int(random(10, 25))
        self.radiusInt = int(random(5, 10))
        self.x = 0
        self.y = 0
        
    
    def position(self):
        x = random(0, self.screenWidth)
        y = random(0, self.screenHeight)
        return([x, y])
    
    def shadePosition(self):
        pos = self.position()
        theta = random(0, 360)
        #theta = degrees(theta)
        x = pos[0]+self.radiusExt*cos(theta)
        y = pos[1]+self.radiusExt*sin(theta)
        theta = 225
        x = 120+120*cos(theta*PI/180)+55
        y = 120+120*sin(theta*PI/180)+55
        return([x, y])
                 
    def generateShade(self):
        pos = self.shadePosition()
        num = int(random(0, 1))
        col = self.shade[num]
        light = int(random(0, 3))
        angle = self.lightAngle[light]
        pointLight(col[0], col[1], col[2], angle[0], angle[1], angle[2]);
        fill(200,34,100)
        ellipse(pos[0], pos[1], self.radiusInt, self.radiusInt) 
    
    def colorBub(self):
        num = int(random(0, 2))
        col = self.shadeBlue[num]
        light = int(random(0, 3))
        angle = self.lightAngle[light]
        return([col, angle])
    
    def generateBubble(self):
        strokeShade = self.strokeShade
        pos = self.position()
        colour = self.colorBub()
        colBlue = colour[0]
        light = colour[1]
        strokeWeight(2)
        stroke(strokeShade[0], strokeShade[1], strokeShade[2], strokeShade[3])
        pointLight(colBlue[0], colBlue[1], colBlue[2], light[0], light[1], light[2]);
       
        #pointLight(0, 100, 255, 30, 200, 200);
        stroke(15, 60, 151)
        fill(83,183,249, 80)
        stroke(100,100,100)
        stroke(190,190,190)
        ellipse(pos[0], pos[1], self.radiusExt, self.radiusExt)
        self.x = pos[0]
        self.y = pos[1]
       
        
    def moveBubble(self):
        print("we're here")
        radius = self.radiusExt
        print(radius)
        newRad = radius + radius*0.2
        x = self.x
        y = self.y
        while (radius < newRad):
            ellipse(x, y+1, radius+1, radius+1)
