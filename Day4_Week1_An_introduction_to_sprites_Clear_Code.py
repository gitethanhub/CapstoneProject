import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
# Sprites in Pygame
# A class that combines a surface, a rect and many addtinoal features like anmations or sounds

# Drawing in pygame
# Display surface object is the only thing displayed
# Addtional surfaces can be added, but they need to be attacted to the display surface
# Surfaces cannot be moved!
# You need to put a 'rect' around them first
# And that 'rect' can be moved


# A SPRITE CLASS -- Object Oriented Programming
# This combines a surface and a Rect
# But can contain more (sounds , animations, behaviors etc)
# You can target mulitple sprites via groups 

# Inorder to create a blank surface write---pygame.Surface([width,height])
# To fill a surface with a color type on a object---object.fill([R,G,B])
# Inorder to add a rectangle to a surface you write---object.get_rect(). 

class Crosshair(pygame.sprite.Sprite):
    def __init__(self,width,height,x_pos,y_pos,color):
        #Inherit all the attributes/funcitons for sprites from pygame
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos,y_pos]

# The object, 
crosshair = Crosshair(50,50,350,350,[255,0,0])


# Cant draw sprites individualy you have to draw them inside a group
# 1. Create a group for the sprites. Variable = pygame.sprite.Group()
# 2. Put the crosshair oject into the group. var_group.add(object)
# 3. Tell the group to draw all the sprites.

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)


# General Setup

#start pygame
pygame.init()
#start a clock
clock = pygame.time.Clock()
#Game Screen

screen_width = 1000
screen_height = 850
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.mouse.set_visible(True)
# When you hover over the window you can see the mouse


#This is how you load an image, pygame.image.load("filename.png")
# Wont be shown now. When pygame load a new image it puts the image on its own surface.
# Inorder to put a surface on a another surface write--(surface you want to put the image on).blit('the second surface','cordinates for the surface')
# So we are putting the background surface onto the screen surface.

# Example-- background = pygame.image.load("background.png")
# Example--'screen'.blit('background',(0,0))-- 
#(0,0) is the same cords as the first surface

#Varaible to keep the game loop running
running = True
while(running):
    for event in pygame.event.get():
        if(event.type == QUIT):
            running = False
        elif(event.type == KEYDOWN):
            if(event.key == K_ESCAPE):
                running = False
    #Fills the color of the screen surface
    screen.fill((100,180,100)) 

    #Draws the sprites inside the group 'crosshair_group'onto the surface ('screen')
    crosshair_group.draw(screen)

    #Puts the background surface on the screen surface
    # Example--'screen'.blit('background',(0,0))-- 

    #updates the screen
    pygame.display.flip()
    
    #Mangaaing game speed / framerate
    clock.tick(30)



#Stops the program
pygame.quit()
