class button(object):
    
    def __init__(self, x, y,label, fontSize):
        self.x = x;
        self.y = y;
        self.Width = (width*0.25)*0.55
        self.Height = (height*0.08)*0.85
        self.fontSize = fontSize;
        self.font = createFont("Arial", self.fontSize);
        self.label = label

    def Draw(self):
        if self.isHover():
            fill(255);
            rect(self.x, self.y, self.Width, self.Height, 15, 15, 15, 15);
            textFont(self.font);
            fill(80,80,80)
        else:
            fill(34,100,150);
            rect(self.x, self.y, self.Width, self.Height, 15, 15, 15, 15);
            textFont(self.font);
            fill(255,255,255)
        
    def addText(self, x):
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
