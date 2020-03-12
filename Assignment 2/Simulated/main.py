from Bubble import bubble
from Button import button
from Background import Background
from Fly import Fly
from Swarm import Swarm

global r, g, b;

r = 0
g = 0
b = 232
c = 0
def setup():    
    fullScreen()
    size(200, 200)
    global pop_size, interfaceHeight, interfaceWidth, inertia, c1, c2, lowerB, xlim, ylim;
    pop_size = 5

    inertia = 0.9
    c1 = 0.2
    c2 = 0.1
    interfaceHeight = height
    interfaceWidth = width*0.22
    xlim, lowerB, ylim = width, interfaceWidth, height
    
    global img
    global img1
    
    img = loadImage("grass.jpg")
    img1 = loadImage("grass1.jpg")

    global swarm;
    swarm = Swarm(pop_size, lowerB, xlim,  ylim, inertia, c1, c2)
    swarm.init_population()
    

def keyReleased():
    loop()
def keyPressed():
    noLoop()
#def mouseClicked():
 #   noLoop()
#def mouseReleased():
 #   redraw()
    #loop()

def draw():
    delay(100)
    global r,g,b, pop_size, swarm, interfaceHeight, interfaceWidth, c1, c2,inertia, lowerB, xlim, ylim;
    
    backgroundObj = Background(r,b,g, height, width+100, pop_size, inertia, c1, c2, img, img1)
    backgroundObj.generateShade()
    backgroundObj.generateBubbles()
    interface = backgroundObj.generateInterface(interfaceWidth, interfaceHeight)
    fill(255, 127, 0)
    ellipse(swarm.foodSource.x, swarm.foodSource.y, 30,30)
    #Code starts after u press 32. to hault the simulation press the mouse. to redraw press a key. to continue release the mouse
    for i in range(len(interface)):
        if interface[i] == True:
            if i == 0:
                pop_size += 1
                interface[i] = False
            if i == 1:
                if pop_size > 3:
                    pop_size -= 1
                interface[i] = False
            if i == 2:
                print('helloo')
                x = inertia + 0.1
                if x < 1:
                    inertia+=0.1
                interface[i] = False
            if i == 3:
                print('kekek')
                x = inertia - 0.1
                if x >= 0.1:
                    inertia -= 0.1
                    
                interface[i] = False            
            if i == 4:
                x = c1 + 0.1
                if x < 1:
                    c1+=0.1
                interface[i] = False 
            if i == 5:
                x = c1 - 0.1
                if x >= 0.1:
                    #swarm.inertia+=1
                    c1 -= 0.1
                interface[i] = False 
            if i == 6:
                x = c2 + 0.1
                if x < 1:
                    #swarm.inertia+=1
                    c2 += 0.1
                interface[i] = False 
            if i == 7:
                x = c2 - 0.1
                if x >=0.1:
                    #swarm.inertia+=1
                    c2 -= 0.1
                interface[i] = False 
            if i == 8:
                swarm = Swarm(pop_size, lowerB, xlim,  ylim, inertia, c1, c2)
                swarm.init_population()
                interface[i] = False
                
            if i == 9:
                interface[i] = False
                print('l')
                noLoop()

            
    if keyCode == 32:
        swarm.PSO(100)
    if keyCode == ENTER:
        noLoop()
