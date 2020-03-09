from Bubble import bubble
from Button import button

class Background(object):
    def __init__(self, Red, Blue, Green, Height, Width, swarmCount, img, img1):
        self.r = Red
        self.b = Blue
        self.g = Green
        self.Height = Height
        self.Width = Width
        self.swarmCount = swarmCount
        self.imgWidth = Width*0.4
        self.imgHeight = Height*0.22
        self.img = img
        self.img1 = img1
        
    def generateShade(self):
        pushStyle()
        for i in range(0, self.Height):
            strokeWeight(3)
            stroke(self.r, i//3, self.b)
            line(0, i, self.Width, i)
        popStyle()
        
    def generateBubbles(self):
        
        prob = int(random(0,20))
        bubbleList = []
        if prob < 4:
            bubbleCount = int(random(0,12))
            for i in range(0,bubbleCount):
                bubbleList.append(bubble(width,height))
                
            for object in bubbleList:
                object.generateBubble()
                if bubbleList<3:
                    bubbleList.pop(0)
        
    def generateInterface(self):
        
        interfaceHeight = self.Height
        interfaceWidth = self.Width*0.22
        lineMargin = 10
        interfaceText = interfaceWidth*0.06
        heightMargin = self.Height*0.08
        widthMargin = self.Width*0.04
        image(self.img, self.Width - self.imgWidth - 200, self.Height - self.imgHeight)
        image(self.img1, interfaceWidth - 50, self.Height - self.imgHeight + 7)
        font = createFont("Georgia", interfaceText)
        textFont(font)
        textAlign(LEFT)
        
        fill(0,0,0)
        
        rect(0, 0, interfaceWidth, interfaceHeight)
        
        fill(250,250,250)
    
        text("Frame Count =  "+ str(frameCount), widthMargin, heightMargin)
        text("Swarm Count =  "+ str(self.swarmCount), widthMargin, heightMargin*2)
        text("Food Location = ", widthMargin, heightMargin*3)
        
        button1 = button(widthMargin,heightMargin*4,"Start", 23)
        button2 = button(widthMargin,heightMargin*5+20,"Pause", 23)
        button3 = button(widthMargin,heightMargin*6+40,"Restart", 23)
        button1.Draw()
        button1.addText(widthMargin+15)
        button2.Draw()
        button2.addText(widthMargin+8)
        button3.Draw()
        button3.addText(widthMargin+2)
        
