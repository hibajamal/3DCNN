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
    global pop_size, interfaceHeight, interfaceWidth;
    pop_size = 100

    inertia = 0.9
    c1 = 0.2
    c2 = 0.1
    interfaceHeight = height
    interfaceWidth = width*0.22
    xlim, lowerB, ylim = width, interfaceWidth, interfaceHeight
    
    global img
    global img1
    
    img = loadImage("grass.jpg")
    img1 = loadImage("grass1.jpg")

    global swarm;
    swarm = Swarm(pop_size, lowerB, xlim,  ylim, inertia, c1, c2)
    swarm.init_population()
    

    
def keyPressed():
    if (key == CODED):
        if (keyCode == UP):
            print("Hi")
        if (keyCode == DOWN):
            print("DOWM")
        if (keyCode == LEFT):
            print("LEFT")
        if (keyCode == RIGHT):
            print("Right")

    if keyCode == 32 and keyCode == 86:
        print(";")
    if keyCode == ENTER:
            print("ENTER")
def draw():
    delay(100)
    global r,g,b, pop_size, xpos, fish, swarm, interfaceHeight, interfaceWidth, c;
    
    backgroundObj = Background(r,b,g, height, width+100, pop_size, swarm.inertia, swarm.c1, swarm.c2, img, img1)
    backgroundObj.generateShade()
    backgroundObj.generateBubbles()
    interface = backgroundObj.generateInterface(interfaceWidth, interfaceHeight)
    fill(255, 127, 0)
    ellipse(swarm.foodSource.x, swarm.foodSource.y, 30,30)
    swarm.PSO(100)

    
