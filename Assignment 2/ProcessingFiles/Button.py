class button(object):
    
    def __init__(self, x, y, Width, Height, label, fontSize):
        self.x = x;
        self.y = y;
        self.Width = (width*0.25)*0.55
        self.Height = (height*0.08)*0.85
        self.fontSize = fontSize;
        self.font = createFont("Arial", self.fontSize);
        self.label = label

    def Draw(self):
        fill(255);
        rect(self.x, self.y, self.Width, self.Height, 15, 15, 15, 15);
        textFont(self.font);
        #noStroke();
        fill(80,80,80);
        text(self.label, self.x + 5, self.Height-self.fontSize//2 + (self.Height - self.fontSize) / 2 + (self.Height / 2))
        #text(self.label, 20,20)
  
    def IsPressed(self):
        if not mousePressed:
            return false
        
        if(mouseX >= self.x and mouseX <= self.x + self.width):
            if(mouseY >= self.y and mouseY <= self.y + (self.height)):
                if(self.framesPassed == self.delay):
                    self.framesPassed = 0
                    return true
        return false
