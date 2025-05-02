
# Ultimate introduction
def display_score():
    #Gives us time in milliseconds when we FIRST called pygame.init()
    # TICKS IS UNIVERSAL
    # We subtract the ticks from itself to go back to zero. Ticks stays the same but the score goes back to zero.
    current_time = pygame.time.get_ticks() - starting_time 
    screen_score = current_time // 1000
    score_surface = score_font.render(f'Score:{screen_score}',anti_aliasing,(64,64,64))
    score_rect = score_surface.get_rect(center = (250,30))
    screen.blit(score_surface,score_rect)
    return(screen_score)


def obstacle_movement(obstacle_list):
    # IF there is something in the list do this function
    if(len(obstacle_list) > 0):
        i = 0
        # obstacle_rect is like , i , just a differnet name
        while i < len(obstacle_list):
            if(obstacle_list[i].x < -100 ):
                del(obstacle_list[i])
                print("||| Deleted An Enemy |||")


            # Move each rect x value to the left a bit
            obstacle_list[i].x = obstacle_list[i].x - 5.5


            # If the rect in the list has a bottome val of 185 then draw a snail, else draw a fly
            if(obstacle_list[i].bottom == 185):
                screen.blit(snail_surface,obstacle_list[i])
                # then blit each one
            else:
                screen.blit(fly_surface,obstacle_list[i])
           
            i = i + 1
       
        # Then return this new list with the new moved snail rects
        return(obstacle_list)
    else:
        return([])


def collisions(player,obstacles):
    if(len(obstacles) > 0):
        i = 0
        while(i < len(obstacles)):
            if( player.colliderect(obstacles[i]) == 1):
                return(1)
            i = i + 1
    else:
        return(0)


def player_animation():
    # Turns these two varaibles into global varaibles(variabels you can access anywhere)
    global player_surface , player_index
    # play walking animation if player is on floor
    # or display jump surface when player is not on floor
    if(player_rect.bottom < 180):
        #the player surface now is the player jump surface
        player_surface = player_jump
    else:
        #Slowly increase the index when the player walks, then if the index is greater than 2 then index goes back to zero.
        player_index = player_index + 0.1
        if(player_index >= len(player_walk_list)):
            player_index = 0
        player_surface = player_walk_list[int(player_index)]
# 1st. Import and initialize(start) the pygame libary
import pygame
from random import randint


pygame.init()


# 2nd. Set up a window. Or a display surface
# The window is like a cordinate system.
# The origon point is always (0,0)(x,y)
# But in pygame the origon point is in the top left.
# So if you want to go to the right you have to increase x.
# If you want to go downwards you have to increase y.
# (Different from what you learn from school) (its like backwards or like upside down)


screen_width = 500
screen_height = 250


screen = pygame.display.set_mode((screen_width,screen_height))
# Title of the window
pygame.display.set_caption('Ultimate Introduction')


# Helps control Framerate
clock = pygame.time.Clock()


#Score Text Surface
#Deafult font in pygame
font_type = None
font_size = 35
score_font = pygame.font.Font(font_type,font_size)


#Try again Text Surface
#Deafult font in pygame
font_type2 = None
font_size2 = 30
try_again_font = pygame.font.Font(font_type2,font_size2)


#End score text Font styling
#Deafult font in pygame
font_type3 = None
font_size3 = 35
end_score_font = pygame.font.Font(font_type3,font_size3)


#Start Screen text Font styling
#Deafult font in pygame
font_type4 = None
font_size4 = 30
start_text_font = pygame.font.Font(font_type4,font_size4)


#Start Screen text Font styling
#Deafult font in pygame
font_type5 = None
font_size5 = 30
start_text2_font = pygame.font.Font(font_type5,font_size5)


# #Pause screen text Font styling
# #Deafult font in pygame
# font_type6 = None
# font_size6 = 30
# pause_text_font = pygame.font.Font(font_type6,font_size6)


# You can create a surface with a Plain color, a Image, or Text
# Recall that a Surface is a rectangular object on which you can draw, like a blank sheet of paper.
# The screen object is a Surface, and you can create your own Surface objects separate from the display screen.
# .convert() converts the image to something pygame can work with easily. Helps our game run faster.


sky_surface = pygame.image.load('Pictures/backgrounds/Sky.png').convert()
ground_surface = pygame.image.load('Pictures/backgrounds/Ground3.png').convert()


#Score text
#Any text
text = "Ethan's Game"
# Smooth the edges of the text. But we dont want that because we are working with pixel art. Any text that not pixel art you turn it True.
anti_aliasing = False
# Color
color = 'Black'
# # score_surface = score_font.render(text,anti_aliasing,(64,64,64))
# # score_rect = score_surface.get_rect(center = (250,30))


#Try again text
#Any text
text2 = "Press Shift to try again. Space bar = Jump"
# Smooth the edges of the text. But we dont want that because we are working with pixel art. Any text that not pixel art you turn it True.
anti_aliasing2 = False
# Color
color2 = 'Black'
try_again_surface = try_again_font.render(text2,anti_aliasing2,color2)
try_again_rect = try_again_surface.get_rect(center = (250,50))


#End Score text
#Any text
# Smooth the edges of the text. But we dont want that because we are working with pixel art. Any text that not pixel art you turn it True.
anti_aliasing3 = False
#Color
color3 = 'Black'
end_score_x_cord = 400
end_score_y_cord = 80




#Starting Screen text
#Any text
text4 = "Press Shift to start. Jump = space bar."
# Smooth the edges of the text. But we dont want that because we are working with pixel art. Any text that not pixel art you turn it True.
anti_aliasing4 = False
# Color
color4 = 'Black'
start_text_surface = start_text_font.render(text4,anti_aliasing4,color4)
start_text_rect = start_text_surface.get_rect(center = (250,50))


#Starting Screen text
#Any text
text5 = "Pumpkin Runner"
# Smooth the edges of the text. But we dont want that because we are working with pixel art. Any text that not pixel art you turn it True.
anti_aliasing5 = False
# Color
color5 = 'Black'
start_text2_surface = start_text2_font.render(text5,anti_aliasing5,color5)
start_text2_rect = start_text2_surface.get_rect(center = (250,25))


#Pause Screen text
#Any text
# text6 = "Pause Screen"
# # Smooth the edges of the text. But we dont want that because we are working with pixel art. Any text that not pixel art you turn it True.
# anti_aliasing6 = False
# # Color
# color6 = 'Black'
# pause_text_surface = pause_text_font.render(text6,anti_aliasing6,color6)
# pause_text_rect = pause_text_surface.get_rect(center = (250,25))




# Obstacles


#Snail Surface
#_alpha removes the blank spots on the image.
# Anamation stuff
snail_surface_sltiher1 = pygame.image.load('Pictures/enemy/Snail7.png').convert_alpha()
snail_surface_sltiher1 = pygame.transform.scale(snail_surface_sltiher1,(65,50))
snail_surface_sltiher2 = pygame.image.load('Pictures/enemy/sprite_1.png').convert_alpha()
snail_surface_sltiher2 = pygame.transform.scale(snail_surface_sltiher2,(65,50))
snail_index = 0
# Create a list of different surfaces of the two snail images.
# So when we change indexs we are changing the images being drawn, so, anmation happens bewteen two images
snail_list = [snail_surface_sltiher1,snail_surface_sltiher2]
snail_surface = snail_list[snail_index]


# snail_rect = snail_surface.get_rect(midbottom = (700,180))


fly_surface_flap1 = pygame.image.load('Pictures/enemy/flying_pumpkin0.png').convert_alpha()
fly_surface_flap1 = pygame.transform.scale(fly_surface_flap1,(70,50))
fly_surface_flap2 = pygame.image.load('Pictures/enemy/flying_pumpkin1.png').convert_alpha()
fly_surface_flap2 = pygame.transform.scale(fly_surface_flap2,(70,50))
# Create a list of different surfaces of the two snail images.
# So when we change indexs we are changing the images being drawn, so, anmation happens bewteen two images
fly_index = 0
fly_list = [fly_surface_flap1,fly_surface_flap2]
fly_surface = fly_list[fly_index]


# List thats gonna contain all the obstacles / enemys / snails and flying pumpkins
obstacle_rect_list = []


# PLAYER


#Player surface
player_surface_walk1 = pygame.image.load('Pictures/player/sprite_pumkin0.png').convert_alpha()
player_surface_walk2 = pygame.image.load('Pictures/player/sprite_pumkin1.png').convert_alpha()
player_surface_walk1 = pygame.transform.scale(player_surface_walk1,(85,85))
player_surface_walk2 = pygame.transform.scale(player_surface_walk2,(85,85))


# Create a list of different surfaces of the two snail images.
# So when we change indexs we are changing the images being drawn, so, anmation happens bewteen two images
player_walk_list = [player_surface_walk1,player_surface_walk2]
player_index = 0
player_jump = pygame.image.load('Pictures/player/pumkin_jump.png').convert_alpha()
player_jump = pygame.transform.scale(player_jump,(85,85))
#Player Rectangle
# Takes a surface and draws a rectangle around it. Puts the midbottom of the rect at the cordinates, (70,180).
#
player_surface = player_walk_list[player_index]
player_rect = player_surface.get_rect(midbottom = (70,180))
player_gravity = 0


# Pumkin player on Start screen
player_stand_surface = pygame.image.load('Pictures/player/sprite_pumkin0.png').convert_alpha()
# Scaled the pumpkin player, then changes the surface again
player_stand_surface = pygame.transform.scale(player_stand_surface,(150,150))
player_stand_rect = player_stand_surface.get_rect(center = (250,130))


# Timers
# Look at notes for more info and documentaion.
# (milli seconds)
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,(1200))


# Creating new events to animate enemys
# A timer will go off and when that timer goes off the obstacle swtiches the image to another. This loops until the program stops.
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,300)


# Run until the user asks to quit
running = True
# Var mangaing game
game_active = False
# Var manaing game over screen
game_over_screen = False
# pause_screen = False
# var managing score
starting_time = 0


while(running):
    # THE EVENT LOOP / USER INTERACTION LOOP
    # Did the user click the window close button?
    for event in(pygame.event.get()):
        if(event.type == pygame.QUIT):
            running = False
        # If game is on. Check these events
        if(game_active == True):
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(player_rect.collidepoint(event.pos) == 1 and player_rect.bottom == 180 ):
                    print("||| mouse clicked player. Jump.|||")
                    player_gravity = -20
            if(event.type == pygame.KEYDOWN and player_rect.bottom == 180 ):
                if(event.key == pygame.K_SPACE):
                    player_gravity = -20                    
                    print("||| Jump! |||")
            # New obstacle spawners
            # If the obstacle timer is on
            if(event.type == obstacle_timer):
                #Generate a random number from 0 - 1. Either 0 and 1
                if(randint(0,1) == 1):
                    #Create a snail rectangle with a random x cord and append it to a list of other rects
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(600,750),185)))
                else:
                    #Create a fly rectangle with a random x cord and append it to a list of other rects
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(550,700),70)))
                print("||| Appened new obstacle |||")
            # if(event.type == pygame.KEYDOWN):
            #     if(event.key == pygame.K_p):
            #         print("Pause GAME.")
            #         pause_screen = True
            if(event.type == snail_animation_timer):
                if(snail_index == 0):
                    # If the index(i.e. the image) is snail 1 then change the index to snail 2
                    snail_index = 1
                else:
                    # Else(i.e if the index IS 1, then change the index back to snail 1)
                    snail_index = 0
                # Use that index to change the image into the previous or up and coming image surface
                snail_surface = snail_list[snail_index]


            if(event.type == fly_animation_timer):
                    # If the index(i.e. the image) is snail 1 then change the index to snail 2
                if(fly_index == 0):
                    fly_index = 1
                else:
                    # Else(i.e if the index IS 1, then change the index back to snail 1)
                    fly_index = 0
                # Use that index to change the image into the previous or up and coming image surface
                fly_surface = fly_list[fly_index]


        # Game over screen Event Loop
        elif(game_active == False and game_over_screen == True):
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
                    print("||| Game Restart |||")
                    # snail_rect.left = 500
                    game_active = True
                    game_over_screen = False
                    starting_time = pygame.time.get_ticks()
                    #Clear the obstacle rect list
                    obstacle_rect_list.clear()
                    player_rect.midbottom = (70,180)
                    player_gravity = 0
        # Start screen event loop
        else:
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
                    print(" ||| Game START!!! ||| ")
                    starting_time = pygame.time.get_ticks()
                    game_active = True




    #If True, Start and Draw everthing for the game.
    if(game_active == True):
        # Here’s how you drawing surfaces on the screen:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,180))
        #adding a background to our score text
        # pygame.draw.rect(screen,'Yellow',score_rect)
        # pygame.draw.rect(screen,'Black',score_rect,2)
        # screen.blit(score_surface,score_rect)
        display_score()


        ## SNAIL


        # If we move one point on the rect, all the other points move.
        # # Gets the origion point(x) of the rect.
       
        # GOOD BYE SIMPLE SNAIL
        # snail_rect.x = snail_rect.x - 6
        # if(snail_rect.right <= -100):
        #     print("Snail out of bounds.")
        #     snail_rect.left = 650
        #     print("Snail back in bounds.")
        # screen.blit(snail_surface,snail_rect)
       
        ## PLAYER


        # We are taking the player surface and placing it in the postion of the rectangle. Then we are putting it on the display surface.
        # player_rect.left = 22 px
        # (0,0) is the origon point. The top left.
        # Player gravity increases every loop by 1
        # Player y rect postion is getting added by player gravity every time




        player_gravity = player_gravity + 1
        player_rect.y = player_rect.y + player_gravity
       
        if(player_rect.bottom >= 180):
            player_rect.bottom = 180
        player_animation()
        screen.blit(player_surface,player_rect)
   
        ## New obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)


        #This is where a framework like pygame comes in handy!
        # Writing collision detection code is tedious, but pygame has a LOT of collision detection methods available for you to use.
        # This method would return a 0 or a 1. 0 is no collide. 1 is a collide.


        collision_check = collisions(player_rect,obstacle_rect_list)
        # Its returns a 1 or a 0
        if(collision_check == 1):
            print("||| Player collided with snail. |||")
            print("||| GAME ENDED |||")
            print("||| Your Score:",display_score(),"|||")
           
            #Has to create the score here because the end score will always change.
            # And you cant get a return if you dont call it before you want to get it
            # Also you cant get the current time when you made the game active false. Which also makes the display_score() function not on.
            # You got to get everything before that.


            #This has to change with the code
            end_score = f"Score:{display_score()}"
            #Creating a new surface everytime. Because you get a different score everytime. Like the display score function.
            end_score_surface = end_score_font.render(end_score,anti_aliasing3,color3)
            #Creaing a new rect everytime. Because you get a new score everytime.
            end_score_rect = end_score_surface.get_rect(center = (end_score_x_cord,end_score_y_cord))


            #Game turns off.
            game_active = False
            game_over_screen = True


    #fills the screen with yellow. And blit two text surfaces. # Game over screen
    elif(game_over_screen == True):
        screen.fill("Orange")
        screen.blit(try_again_surface,try_again_rect)
        screen.blit(end_score_surface,end_score_rect)
        screen.blit(start_text2_surface,start_text2_rect)
        screen.blit(player_stand_surface,player_stand_rect)
    # elif(pause_screen == True):
    #     screen.fill((230,150,25))
    #     screen.blit(pause_text_surface,pause_text_rect)
    #     screen.blit(start_text_surface,start_text_rect)
    #     screen.blit(player_stand_surface,player_stand_rect)
    #Start screeen
    else:
        screen.fill((230,150,25))
        screen.blit(start_text_surface,start_text_rect)
        screen.blit(start_text2_surface,start_text2_rect)
        screen.blit(player_stand_surface,player_stand_rect)
   
    # Notice the call to pygame.display.flip() after the call to blit().
    # This updates the entire screen with everything that’s been drawn since the last flip.
    # Without the call to .flip(), nothing is shown.
    pygame.display.flip()
   


    #Framerate 60fps
    clock.tick(60)
pygame.quit()


