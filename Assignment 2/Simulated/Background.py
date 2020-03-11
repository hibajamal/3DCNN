from Bubble import bubble
from Button import button

class Background(object):
    def __init__(self, Red, Blue, Green, Height, Width, swarmCount, inertia, c1, c2, img, img1):
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
        self.inertia = inertia
        self.c1 = c1
        self.c2 = c2
        
    def generateShade(self):
        pushStyle()
        for i in range(0, self.Height):
            strokeWeight(3)
            stroke(self.r, i//3, self.b, 50)
            line(0, i, self.Width, i)
        popStyle()
        
    def generateBubbles(self):
        
        prob = int(random(0,30))
        bubbleList = []
        if prob < 2:
            bubbleCount = int(random(0,12))
            for i in range(0,bubbleCount):
                bubbleList.append(bubble(width,height))
                
        for object in bubbleList:
            object.generateBubble()
            if bubbleList<3:
                bubbleList.pop(0)
        
    def generateInterface(self, interfaceWidth, interfaceHeight):
        
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
        stroke(255,255,255)
        rect(0, 0, interfaceWidth, interfaceHeight)
        
        fill(250,250,250)
    
        text("Frame Count =  "+ str(frameCount), widthMargin, heightMargin)

        #line(40, interfaceWidth - 100, 40, heightMargin - 20)
        text("Swarm Count =  "+ str(self.swarmCount), widthMargin, heightMargin*2)
        but = button(interfaceWidth - 60, heightMargin*2 - 18, "I", 20)
        but.draw(20, 20)
        but1 = button(interfaceWidth - 30, heightMargin*2 - 18, "D", 20)
        but1.draw(20, 20)
        text("Inertia = "+ str(self.inertia), widthMargin, heightMargin*3)
        but2 = button(interfaceWidth - 60, heightMargin*3 - 18, "I", 20)
        but2.draw(20, 20)
        but3 = button(interfaceWidth - 30, heightMargin*3 - 18, "D", 20)
        but3.draw(20, 20)
        text("c1 = "+ str(self.c1), widthMargin, heightMargin*4)    
        but4 = button(interfaceWidth - 60, heightMargin*4 - 18, "I", 20) 
        but4.draw(20, 20)
        but5 = button(interfaceWidth - 30, heightMargin*4 - 18, "D", 20)
        but5.draw(20, 20)
        text("c2 = "+str(self.c2), widthMargin, heightMargin*5)   
        but6 = button(interfaceWidth - 60, heightMargin*5 - 18, "I", 20)
        but6.draw(20, 20)
        but7 = button(interfaceWidth - 30, heightMargin*5 - 18, "D", 20)
        but7.draw(20, 20)
             
        lst = [False, False, False, False]
        button1 = button(widthMargin,heightMargin*6,"Start", 23)
        button2 = button(widthMargin,heightMargin*7+20,"Pause", 23)
        button3 = button(widthMargin,heightMargin*8+40,"Restart", 23)
        a = button1.Draw()
        if a == 1:
            lst[0] = True
        button1.addText(widthMargin+15)
        b = button2.Draw()
        if b == 1:
            lst[1] = True
        button2.addText(widthMargin+8)
        c = button3.Draw()
        button3.addText(widthMargin+2)
        return lst
