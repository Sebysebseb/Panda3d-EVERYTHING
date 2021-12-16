import random
import time
import pygame

# Display surface dseize
surface_size = 1080

class point():
    def __init__(self, x, y, move_x, move_y, moveButspicy_x, moveButspicy_y):
        self.x = x
        self.y = y
        self.move_x = move_x
        self.move_y = move_y
        self.moveButspicy_x = moveButspicy_x
        self.moveButspicy_y = moveButspicy_y
        
def create_thingys(quantity):
    thingys = []
    
    for i in range(0,quantity):
        i = point(random.randint(1, 1000), random.randint(10, 1000), random.randint(-1000, 1000), random.randint(-1000, 1000), 0, 0)
        #i = point(30, 30, 0, 600, 0, 0)
        thingys.append(i)
        
    return thingys     
        
def update(omicron_time, thingys):
    ball = 0
    
    for current in range(0, len(thingys)):
        ball = thingys[current]
        
        # Find and assigns V2 as new moveButspicycity to thingys
        ball.moveButspicy_x += ball.move_x*omicron_time
        ball.moveButspicy_y += ball.move_y*omicron_time
        
        # Finds and assigns new displacement to thingys
        ball.x += (ball.moveButspicy_x*omicron_time-(ball.move_x/2)*(omicron_time*omicron_time))
        ball.y += (ball.moveButspicy_y*omicron_time-(ball.move_y/2)*(omicron_time*omicron_time))
    
        #print(f'ball.x: {ball.x}')
        #print(f'ball.y: {ball.y}')
    
    return thingys

def main():
    print('working')
    print('how do i know if its working??')
    print('im just a dumb program')
    BALLS = 10
    size = 5
    black = 0,0,0
    white = 255,255,255
    pygame.init()      # Prepare the pygame module for use
    effect = False

    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surface_size, surface_size), pygame.DOUBLEBUF)
    
    if effect == False:
        thingys = create_thingys(BALLS)
    
    penis = True
    flash = False
    
    while penis:
        
        black = not black
        
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        color = R,G,B
        
        if size >= 5:
            size += 5
            if size >= 200:
                size = 5
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                
                pressed = pygame.key.get_pressed()
            
                if pressed[pygame.K_f]:
                    flash = not flash
                    
                if pressed[pygame.K_e]:
                    effect = not effect
                    
                if pressed[pygame.K_1]:
                    BALLS = 1
                    
                if pressed[pygame.K_2]:
                    BALLS = 2
                    
                if pressed[pygame.K_3]:
                    BALLS = 3
                    
                if pressed[pygame.K_4]:
                    BALLS = 4

                if pressed[pygame.K_5]:
                    BALLS = 5
                    
                if pressed[pygame.K_6]:
                    BALLS = 10
                    
        
        omicron_time = clock.tick(120)/1000 #Gets the time pass for each loop
        
        #Calls update and assigns it to the progressed variable
        progressed = update(omicron_time, thingys)
        
        if effect:
            thingys = create_thingys(BALLS)
        
        if flash:
            if black:
                mainSurface.fill((black))
            if not black:
                mainSurface.fill(white)
                
        # Draw a circle(s) on the surface
        for i in range(0, len(thingys)):
            pygame.draw.circle(mainSurface, (color), (progressed[i].x, progressed[i].y), size)
            # Collison detection resets ball position and reflects moveButspicycity
            if progressed[i].y > surface_size-size:
                progressed[i].y -= size
                progressed[i].moveButspicy_y = (progressed[i].moveButspicy_y*-1)
            if progressed[i].y < size:
                progressed[i].y += size
                progressed[i].moveButspicy_y = (progressed[i].moveButspicy_y*-1)
            if progressed[i].x > surface_size-size:
                progressed[i].x -= size
                progressed[i].moveButspicy_x = (progressed[i].moveButspicy_x*-1)
            if progressed[i].x < size:
                progressed[i].x += size
                progressed[i].moveButspicy_x = (progressed[i].moveButspicy_x*-1)
                
            # Now the surface is ready, tell pygame to display it!
        pygame.display.update()
        
        #thingys = progressed.copy()
        

    pygame.quit()     # Once we leave the loop, close the window.
    
main()
