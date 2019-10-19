import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)#colours use the RGB system
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

car_width = 170

gameDisplay = pygame.display.set_mode((800,600))#this determines the screen size
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')#this only loads the image

def things_dodged(count):#to display score
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: "+str(count),True,blue)
    gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):#here we have our obstacle function
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):#to show that you crashed basically
    textSurface = font.render(text,True,red)
    return textSurface, textSurface.get_rect()
 
def message_display(text):#in which font to show you crashed
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    
    pygame.display.update()
    
    time.sleep(2)
    
    game_loop()
   
def crash():
    message_display('You crashed!')

def game_loop():#this entire function is the game basically
   
    x = (display_width * 0.4)
    y = (display_height * 0.7)
    
    x_change = 0#variable used for movement
    
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0,display_width - thing_width)
    
    dodged = 0
    
    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:#this is how we move an object
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = +5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        x += x_change
        
        gameDisplay.fill(white) 
        
        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx,thing_starty,thing_width,thing_height,green)
        thing_starty += thing_speed
               
        car(x,y)
        things_dodged(dodged)
        
        if x > display_width - car_width or x < 0:
            crash()
        
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1#to increase speed
            thing_width += (dodged*1.2)#to increase size
        
        #this checks to see if the car image crosses over with the obstacles
        if y < thing_starty+thing_height:            
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x+car_width < thing_startx + thing_width:
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_loop()    
pygame.quit()
quit()