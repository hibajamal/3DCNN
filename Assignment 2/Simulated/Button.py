class button(object):
    
    def __init__(self, x, y,label, fontSize):
        self.x = x;
        self.y = y;
        self.Width = (width*0.25)*0.55
        self.Height = (height*0.08)*0.85
        self.fontSize = fontSize;
        self.font = createFont("Arial", self.fontSize);
        self.label = label

    def draw(self, Width, Height):
        pushStyle()
        self.Width = Width
        self.Height = Height
        self.fontSize =10
        self.font = createFont("Arial", self.fontSize);
        stroke(255,255,255)
    
        if self.isPressed():
            fill(255);
            rect(self.x, self.y, self.Width, self.Height, 15, 15, 15, 15);
            textFont(self.font);
            fill(100,100,100)
            popStyle()
            return 1
            
        elif self.isHover():
            fill(255, 100);
            rect(self.x, self.y, self.Width, self.Height, 15, 15, 15, 15);
            textFont(self.font);
            fill(20,80,100)
        else:
            fill(34,100,150);
            rect(self.x, self.y, self.Width, self.Height, 15, 15, 15, 15);
            textFont(self.font);
            fill(255,255,255)
        text(self.label, self.x +self.Width/2 - 2 , self.y + 14)
        popStyle()
  
            
    def Draw(self):
        pushStyle()
        stroke(255,255,255)
        fill(255,45,67)
        if self.isPressed():
            fill(255, 100);
            rect(self.x, self.y, self.Width, self.Height, 15, 15, 15, 15);
            textFont(self.font);
            fill(200,100,0)
            return True
            
        elif self.isHover():
            fill(255, 100);
            rect(self.x, self.y, self.Width, self.Height, 15, 15, 15, 15);
            textFont(self.font);
            fill(20,80,100)
        else:
            fill(34,10,150);
            rect(self.x, self.y, self.Width, self.Height, 15, 15, 15, 15);
            textFont(self.font);
            fill(255,255,255)
        popStyle()
    def addText(self, x):
        #fill(255, 255, 255)
        axis = self.x + x
        text(self.label, self.x + x, self.y+(self.Height-self.fontSize)+5)
        
    def isHover(self):
        if(mouseX >= self.x and mouseX <= self.x + self.Width):
            if(mouseY >= self.y and mouseY <= self.y + (self.Height)):
                    return True
        return False

    def isPressed(self):
        if (self.isHover()):
            if (mousePressed):
                    return True
        return False
