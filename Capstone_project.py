#// SIMPLICITY IS KEY \\
#// KEEP TRYING EVERYTHING OUT \\
#// Do this one thing at time\\
#// Try to think things out first , then code \\\




def npc_movement_waiting(npc_rect_list):
    #If there is something in the list then run this
    if(len(npc_rect_list) > 0):
        i = 0
          #Sets the barrier at the line
        barrier = 100
          #If i less than the list length run through all the npcs list
        while(i < len(npc_rect_list)):
            #Checks if an npc’s x cord is less than or equal to the barriers
            if(npc_rect_list[i].x <= barrier):
            #Then make the npc’s x cord be the barriers. So it stops the npc from moving.
                npc_rect_list[i].x = barrier
            #Then the barrier changes to make it so the next npc doesn't collide with the other npc
                barrier = barrier + 90
            #Blit these changes
                screen.blit(npc_surface2,npc_rect_list[i])
            #and then go to the next npc rect
                i = i + 1
          #If an npcs x isnt near the barrier then do this
            else:
                # Move each rect x value to the left a bit
                npc_rect_list[i].x = npc_rect_list[i].x - 4
                screen.blit(npc_surface2,npc_rect_list[i])
                # Goes through all of the list
                i = i + 1
        return(npc_rect_list)
    else:
        return([])




def display_player_score(player_points):
    score_text = f"Player score: {player_points}"
    scrore_text_surface = score_text_font.render(score_text,anti_aliasing,text_color,texts_background_color)
    score_rect = scrore_text_surface.get_rect(center = (50,100))
    screen.blit(scrore_text_surface,score_rect)



def display_farmer_score(player_food_points):
    global selected_food
    if(selected_food == 0):
        color = 'Yellow'
    if(selected_food == 1):
        color = 'Orange'




    if(player_food_points <= 0):
        player_food_points = 0




    farmer_score_text = f"X {player_food_points}"
    farmer_score_text_surface = farmer_score_text_font.render(farmer_score_text,text_color,color)
    farmer_score_text_rect =  farmer_score_text_surface.get_rect(center = (600,25) )
    screen.blit(farmer_score_text_surface,farmer_score_text_rect)




def display_player_stacked_food(player_food_list):
    if(len(player_food_list) > 0):
        i = 0
        food_x_barrier = 400
        food_y_barrier = 260


        while(i < len(player_food_list)):
            if(food_x_barrier >= screen_width):
                food_y_barrier = food_y_barrier - 25
                food_x_barrier = 400
            player_food_list[i].x = food_x_barrier
            player_food_list[i].centery = food_y_barrier
            food_x_barrier = food_x_barrier + 30
            screen.blit(animal_food_surface,player_food_list[i])
            i = i + 1
        return(player_food_list)
    else:
        return([])


def update_produce(milk,carrot,wool):
    all_produce_text = f"X:{milk}     X:{carrot}     X:{wool}"
    produce_text_surface = produce_text_font.render(all_produce_text,anti_aliasing,'Yellow')
    produce_text_rect = produce_text_surface.get_rect(center = (90,50))
    screen.blit(produce_text_surface,produce_text_rect)

def update_player_money(player_money):
    player_money_text = f"Money:${float(player_money)}"
    player_money_surface = player_money_font.render(player_money_text,anti_aliasing,'Blue')
    player_money_rect = player_money_surface.get_rect(center = (80,80))
    screen.blit(player_money_surface,player_money_rect)
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








#Setup dusplay surface / window and clock
screen_width = 700
screen_height = 500




screen = pygame.display.set_mode((screen_width, screen_height))
#Title of the window
pygame.display.set_caption('Capstone Project')
#Controls framerate
clock = pygame.time.Clock()






# Text Surfaces






#universal text variables
font_type = None
anti_aliasing = False
text_color = 'Black'
texts_background_color = 'Yellow'
font_size = 18




#npc text
npc_text_surface = pygame.Surface((150,150))




npc_text_font = pygame.font.Font(font_type,font_size)
npc_text = "1. Welcome text. 2. Helpful guidance to the game. Go to the protal to continue. (arrow keys)"






npc_text_surface = npc_text_font.render(npc_text,anti_aliasing,text_color,texts_background_color)
npc_text_rect = npc_text_surface.get_rect(center = (350,100))




#npc question




#npc_question_surface = pygame.Surface((150,150))


npc_question_font = pygame.font.Font(font_type,font_size)
npc_question1 = "1. Where floor is the bathroom?"
npc_question2 = "2. Can i speak to your manager?"
npc_question3 = "3. Where is the job application form?"




npcs_question_list = [npc_question1,npc_question2,npc_question3]
npcs_answer_list = []
#Tile text




#title_text_surface = pygame.Surface((150,150))




title_text_font = pygame.font.Font(font_type,font_size)
title_text = "Here is title of game and helpful information. Click space bar to continue"
title_text_surface = title_text_font.render(title_text,anti_aliasing,text_color,texts_background_color)
title_text_rect = title_text_surface.get_rect(center = (350,100))




#Screen 2 text




#screen2_text_surface = pygame.Surface((150,150))




screen2_text_font = pygame.font.Font(font_type,font_size)
screen2_text = "1. Screen 2 text. 2. Here has three options of differnet caeers with different tasks."
screen2_text_surface = screen2_text_font.render(screen2_text,anti_aliasing,text_color,texts_background_color)
screen2_text_rect = screen2_text_surface.get_rect(center = (350,50))




#Screen 3 text




#screen3_text_surface = pygame.Surface((150,150))




screen3_text_font = pygame.font.Font(font_type,font_size)
screen3_text = "1. Screen 3 text. 2. Here has the first caeer task. Office job type, custormer service."
screen3_text_surface = screen3_text_font.render(screen3_text,anti_aliasing,text_color,texts_background_color)
screen3_text_rect = screen3_text_surface.get_rect(center = (350,100))




#Screen 4 text




# screen4_text_surface = pygame.Surface((150,150))


screen4_text_font = pygame.font.Font(font_type,font_size)
screen4_text = "1. Screen 4 text. 2. Here has second caeer task. Being a farmer, managing animals, hard labor, and buying food."
screen4_text_surface = screen4_text_font.render(screen4_text,anti_aliasing,text_color,texts_background_color)
screen4_text_rect = screen4_text_surface.get_rect(center = (350,100))




#Screen 5 text




# screen5_text_surface = pygame.Surface((150,150))




screen5_text_font = pygame.font.Font(font_type,font_size)
screen5_text = "1. Screen 5 text. 2. End screen text. Can restart the game or quit the game."
screen5_text_surface = screen5_text_font.render(screen5_text,anti_aliasing,text_color,texts_background_color)
screen5_text_rect = screen5_text_surface.get_rect(center = (350,100))


#Background Surfaces


# npc_screen
sky_surface = pygame.image.load('Pictures/backgrounds/background.png').convert()
ground_surface = pygame.image.load('Pictures/backgrounds/Ground3.png').convert()


sky_surface = pygame.transform.scale(sky_surface,(700,360))
ground_surface = pygame.transform.scale(ground_surface,(700,140))



#career_1_screen background


office_background_surface = pygame.image.load('Pictures/backgrounds/office_background.png').convert()
office_ground_surface = pygame.image.load('Pictures/backgrounds/office_floor.png').convert()



office_background_surface = pygame.transform.scale(office_background_surface,(700,400))
office_ground_surface = pygame.transform.scale(office_ground_surface,(700,100))


#Portal surface



#School
portal_surface = pygame.image.load("Pictures/portal/portal_0.png").convert_alpha()


portal_surface = pygame.transform.scale(portal_surface,(130,150))
portal_rect = portal_surface.get_rect(midbottom = (600,360))



#Player and Npc surfaces / Rects



# Career 1 player - helper player



player_surface = pygame.image.load('Pictures/player/sprite_pumkin0.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (400,360))
player_points = 0
player_wrong_choice = 0




#player Score text
score_text_font = pygame.font.Font(font_type,font_size)








#Npcs








#Home Computer
npc_surface1 = pygame.image.load('Pictures/enemy/NPC.png').convert_alpha()
npc_surface2 = pygame.image.load('Pictures/enemy/NPC(2).png').convert_alpha()








#School Computer
# npc_surface1 = pygame.image.load('Pictures/enemy/NPC.png').convert_alpha()
# npc_surface2 = pygame.image.load('Pictures/enemy/NPC(2).png').convert_alpha()
















npc_surface1 = pygame.transform.scale(npc_surface1,(96,96))
npc_surface2 = pygame.transform.scale(npc_surface2,(96,96))
















npc1_rect = npc_surface1.get_rect(midbottom = (80,360))
npc2_rect = npc_surface2.get_rect(midbottom = (250,360))
















npc_obstacle_rect_list = []
npc_mood = 0
npc_mood_checker = False








#npc timer
npc_timer_font = pygame.font.Font(font_type,font_size)








#caeer select screen buttons
#Customer select and farmer




customer_select_button_surface = pygame.image.load('Pictures/buttonimg/Customer_select_button(84x81).png')
customer_select_button_surface = pygame.transform.scale(customer_select_button_surface, (200,200))
customer_select_button_rect = customer_select_button_surface.get_rect(center = (150,200))








farmer_select_button_surface = pygame.image.load('Pictures/buttonimg/Farmer_select_button(84x81).png')
farmer_select_button_surface = pygame.transform.scale(farmer_select_button_surface, (200,200))
farmer_select_button_rect = farmer_select_button_surface.get_rect(center = (500,200))
















# --------------- /// Caeer 2 stuff //// ---------------
















# |||| Career_2_screen backgrounds ||||








farmer_background_surface = pygame.image.load('Pictures/farmer_game_imgs/farm_ground.png').convert()
farmer_background_surface = pygame.transform.scale(farmer_background_surface,(700,500))








farmer_fence_surface_cow = pygame.image.load('Pictures/farmer_game_imgs/fence.png').convert_alpha()
farmer_fence_surface_pig = pygame.image.load('Pictures/farmer_game_imgs/fence.png').convert_alpha()
farmer_fence_surface_sheep = pygame.image.load('Pictures/farmer_game_imgs/fence.png').convert_alpha()








farmer_fence_surface_cow = pygame.transform.scale(farmer_fence_surface_cow,(310,150))
farmer_fence_surface_pig = pygame.transform.scale(farmer_fence_surface_pig,(310,150))
farmer_fence_surface_sheep = pygame.transform.scale(farmer_fence_surface_sheep,(310,150))



# ||| farm animals |||


cow_surface = pygame.image.load('Pictures/farmer_game_imgs/cow.png').convert_alpha()
cow_rect = cow_surface.get_rect(center = (450,60))
# Maximum of three cows
# Next cow x-val = 500 , y = 50
# Next cow x-val = 470 , y = 100


pig_surface = pygame.image.load('Pictures/farmer_game_imgs/pig.png').convert_alpha()
pig_rect = pig_surface.get_rect(center = (450,210))
# Maximum of five pigs
# add 25 to x
# when three pigs on y = 150 change y to 200
# Next pig x-val = 475 , y = 150
# Next pig x-val = 500 , y = 150


sheep_white_surface = pygame.image.load('Pictures/farmer_game_imgs/sheep_white.png').convert_alpha()
sheep_white_surface = pygame.transform.scale(sheep_white_surface,(90,70))
sheep_white_rect = sheep_white_surface.get_rect(center = (460,370))
# Maximum of three sheep
# Next sheep x-val = 500 , y = 370
# Next sheep x-val = 480 , y = 400
# Chance to add rainbow sheep



# career 2 player ---- farmer player

player_farmer_surface = pygame.image.load('Pictures/player/pumpkin_farmer.png').convert_alpha()
player_farmer_surface = pygame.transform.scale(player_farmer_surface,(125,150))
pf_x_cord = 350
pf_y_cord = 220
player_farmer_rect = player_farmer_surface.get_rect(center = (pf_x_cord,pf_y_cord) )
player_left_or_right = 0
# left = 0
# right = 1
# player_farmer_surface = pygame.transform.flip(player_farmer_surface,True,False)


# player_money_text
player_money = 0
player_money_font = pygame.font.Font(font_type,25)


# Player a and d keys (for player labor)


a_key_white_surface = pygame.image.load('Pictures/buttonimg/a_key_0.png')
a_key_blue_surface = pygame.image.load('Pictures/buttonimg/a_key_1.png')




d_key_white_surface = pygame.image.load('Pictures/buttonimg/d_key_0.png')
d_key_blue_surface = pygame.image.load('Pictures/buttonimg/d_key_1.png')


# When i click a or d this becomes 1
# If this is one then switch the surfaces being blitted, while a or d is clicked
a_key_detection_index = 0
d_key_detection_index = 0


# Surface list
a_key_surface_list = [a_key_white_surface,a_key_blue_surface]
d_key_surface_list = [d_key_white_surface,d_key_blue_surface]


a_key_surface = a_key_surface_list[a_key_detection_index]
d_key_surface = d_key_surface_list[d_key_detection_index]



# animal food
# player interacts
animal_food_surface = pygame.image.load('Pictures/farmer_game_imgs/farmer_food.png').convert_alpha()
animal_food_surface = pygame.transform.scale(animal_food_surface,(60,60))
af_x_cord = pf_x_cord - 100
af_y_cord = pf_y_cord + 40
animal_food_rect = animal_food_surface.get_rect( center = (af_x_cord,af_y_cord) )


#player gets
player_animal_food_list_rects = []


# animal food score
animal_food_score_surface = pygame.image.load('Pictures/farmer_game_imgs/farmer_food.png').convert_alpha()
animal_food_score_rect = animal_food_score_surface.get_rect( center = (550,25) )
farmer_score_text_font = pygame.font.Font(font_type,30)
farmer_food_points = 0
selected_food = 0
feed_cow = False
feed_pig = False
feed_sheep = False




# animal produce
milk_surface = pygame.image.load('Pictures/farmer_game_imgs/milk.png').convert_alpha()
carrot_surface =  pygame.image.load('Pictures/farmer_game_imgs/carrot.png').convert_alpha()
wool_surface =  pygame.image.load('Pictures/farmer_game_imgs/wool.png').convert_alpha()


milk_surface = pygame.transform.scale(milk_surface,(30,30))
carrot_surface = pygame.transform.scale(carrot_surface,(30,30))
wool_surface = pygame.transform.scale(wool_surface,(30,30))




# produce text - HAS A FUNCTION


produce_text_font = pygame.font.Font(font_type,25)
# player produce
milk_count = 0
carrot_count = 0
wool_count = 0



# Selling and buying screen


# Shop sign image
shop_sign_surface = pygame.image.load('Pictures/farmer_game_imgs/shop_sign_text.png').convert()
shop_sign_surface = pygame.transform.scale(shop_sign_surface,(150,150))
shop_sign_rect = shop_sign_surface.get_rect(center  = (screen_width/2,100))


#Shop background
# shop_background_rect = pygame.Rect(200,140,300,300)

# sell buttons
sell_milk_button_surface = pygame.image.load('Pictures/buttonimg/sell_button.png').convert()
sell_milk_button_rect = sell_milk_button_surface.get_rect(center = (50,250))
milk_button_press = False

sell_carrot_button_surface = pygame.image.load('Pictures/buttonimg/sell_button.png').convert()
sell_carrot_button_rect = sell_carrot_button_surface.get_rect(center = (50,320))
carrot_button_press = False

sell_wool_button_surface = pygame.image.load('Pictures/buttonimg/sell_button.png').convert()
sell_wool_button_rect = sell_wool_button_surface.get_rect(center = (50,390))
wool_button_press = False


# buy buttons 
buy_cow_button_surface = pygame.image.load('Pictures/buttonimg/buy_button.png').convert()
buy_cow_button_rect = buy_cow_button_surface.get_rect(center = (550,250))
buy_cow_button_press = False

buy_pig_button_surface = pygame.image.load('Pictures/buttonimg/buy_button.png').convert()
buy_pig_button_rect = buy_pig_button_surface.get_rect(center = (550,320))
buy_pig_button_press = False

buy_sheep_button_surface = pygame.image.load('Pictures/buttonimg/buy_button.png').convert()
buy_sheep_button_rect = buy_sheep_button_surface.get_rect(center = (550,390))
buy_sheep_button_press = False




# Home Screen




# true
start_screen = True


# Npc talking screen



#False
npc_screen = False
#False
talking = False




# Customer service screen varaibles


#False
select_screen = False
#False
career_1_gamescreen = False
#False
career_1_gameoverscreen = False



#Npc variables
npc_spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(npc_spawn_timer,(1800))



starting_time = 0
npc_mood_timer = 0
delete_npc = False
player_question_answer = False
npc_checker = True



# Farmer screen varabiles



#False
player_labor_screen = False
#False
animal_screen = False
#False
selling_and_buying_screen = False




# End screen
#False
end_screen = False



running = True
while(running):
    for event in(pygame.event.get()):
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    running = False
        if(start_screen == True):
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    npc_screen = True
                    start_screen = False
        elif(npc_screen == True):
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(npc1_rect.collidepoint(event.pos) == True or npc2_rect.collidepoint(event.pos) == True):
                    print("Talking to NPC. Show text")
                    talking = True
                else:
                    talking = False
        elif(select_screen == True):
            # if(event.type == pygame.KEYDOWN):
            #     if(event.key == pygame.K_SPACE):
            #         career_1_gamescreen = True
            #         select_screen = False
            #         starting_time = pygame.time.get_ticks()
            #         print("player is on career 1 screen")  
            #     elif(event.key == pygame.K_LSHIFT):
            #         career_2_screen = True
            #         select_screen = False
            #         print("Player is on caeer 2 screen")
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(customer_select_button_rect.collidepoint(event.pos) == True):
                    print("Player picked customer service")
                    career_1_gamescreen = True
                    select_screen = False
                    starting_time = pygame.time.get_ticks()
                    print("player is on career 1 screen")
                elif(farmer_select_button_rect.collidepoint(event.pos) == True):
                    print("player picked farmer")
                    player_labor_screen = True
                    select_screen = False
                    print("Player is on caeer 2 screen")
        elif(career_1_gamescreen == True):
            if(player_question_answer == True):
               
                if(event.type == pygame.KEYDOWN):
                        # if(event.key == pygame.K_SPACE):
                        #     end_screen = True
                        #     career_1_screen = False
                        #     print("player is on end screen")
                        # if(event.key == pygame.K_l):
                        #     delete_npc = True
                        #     npc_checker = True
                        #     player_question_answer = False
                        #     print("Deleted an NPC and question")
                    if(event.key == pygame.K_a and random_question == 0):
                        delete_npc = True
                        npc_checker = True
                        player_question_answer = False
                        print("Thank you for telling me where the bathroom is.")
                        player_points = (player_points + 10) - npc_mood
                        # print("Deleted an NPC and question")
                    elif(event.key == pygame.K_b and random_question == 1):
                        delete_npc = True
                        npc_checker = True
                        player_question_answer = False
                        print("Yes you can speak to my manager. ")
                        player_points = (player_points + 10) - npc_mood
                        # print("Deleted an NPC and question")
                    elif(event.key == pygame.K_c and random_question == 2):
                        delete_npc = True
                        npc_checker = True
                        player_question_answer = False
                        print("Its on the counter here.")
                        player_points = (player_points + 10) - npc_mood
                        # print("Deleted an NPC and question")
                    else:
                        print("Sorry wrong thing")
                        player_wrong_choice = player_wrong_choice + 1
                        if(player_wrong_choice >= 5):
                            npc_mood = npc_mood + 1
                            player_wrong_choice = 0
                if(player_points >= 150):
                    print("Player completed level. Go to gameover screen. ")
                    career_1_gameoverscreen = True
                    career_1_gamescreen = False
            if(event.type == npc_spawn_timer):
                if(len(npc_obstacle_rect_list) == 7):
                    print("list is full!")
                else:
                    npc_obstacle_rect_list.append(npc_surface2.get_rect(midbottom = (650,400)))
                    print("New npc is appended")
            # if(event.type == npc_mood_timer):
            #     npc_mood_maker = True
        elif(career_1_gameoverscreen == True):
            pass
















        elif(player_labor_screen == True):
            # if(event.type == pygame.KEYDOWN):
            #         if(event.key == pygame.K_SPACE):
            #             end_screen = True
            #             player_labor_screen = False
            #             print("player is on end screen")
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_a and player_left_or_right == 0):
                    # flip the player looking to the left
                    player_farmer_surface = pygame.transform.flip(player_farmer_surface,True,False)
                    player_left_or_right = 1
                   
                if(event.key == pygame.K_d and player_left_or_right == 1):
                    # flip the player looking to the right
                    player_farmer_surface = pygame.transform.flip(player_farmer_surface,True,False)
                    player_left_or_right = 0


                    # # This checks if the farmer points is a multiple of 10
                    # farmer_check = farmer_food_points / 10
                    # # If farmer_food_points divided by 10 is not the integer of farmer_check.
                    # # Yes Ex. 10/10 = 1 == int(1) -> 1 equal to 1
                    # # No Ex. 5/10 = 0.5 /= int(0.5) = 0 -> 0.5 not equal to 0
                    # if(farmer_check == int(farmer_check)):
                    if(len(player_animal_food_list_rects) >= 20):
                        print("Sorry ran out of food.")
                    else:
                        player_animal_food_list_rects.append(animal_food_surface.get_rect(center = (400,260)))
                        farmer_food_points = farmer_food_points + 1
                if(event.key == pygame.K_SPACE):
                    player_labor_screen = False
                    animal_screen = True








        elif(animal_screen == True):
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(animal_food_score_rect.collidepoint(event.pos) == True):
                    selected_food = 1
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(selected_food == 1 and cow_rect.collidepoint(event.pos) == True):
                    feed_cow = True
                    selected_food = 0
                elif(selected_food == 1 and pig_rect.collidepoint(event.pos) == True):
                    feed_pig = True
                    selected_food = 0
                elif(selected_food == 1 and sheep_white_rect.collidepoint(event.pos) == True):
                    feed_sheep = True
                    selected_food = 0
                else:
                    feed_cow = False
                    feed_pig = False
                    feed_sheep = False
            if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_SPACE):
                        animal_screen = False
                        selling_and_buying_screen = True
                   
       
        elif(selling_and_buying_screen == True):
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(sell_milk_button_rect.collidepoint(event.pos) == True):
                    milk_button_press = True
                elif(sell_carrot_button_rect.collidepoint(event.pos) == True):
                    carrot_button_press = True 
                elif(sell_wool_button_rect.collidepoint(event.pos) == True):
                    wool_button_press = True
                else:
                    milk_button_press = False
                    carrot_button_press = False
                    wool_button_press = False
            
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(buy_cow_button_rect.collidepoint(event.pos) == True):
                    buy_cow_button_press = True
                elif(buy_pig_button_rect.collidepoint(event.pos) == True):
                    buy_pig_button_press = True 
                elif(buy_sheep_button_rect.collidepoint(event.pos) == True):
                    buy_sheep_button_press = True
                else:
                    buy_cow_button_press = False
                    buy_pig_button_press = False
                    buy_sheep_button_press = False
        




        elif(end_screen == True):
            if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_SPACE):
                        end_screen = False
                        start_screen = True
                        player_rect.midbottom = (400,360)
                        print("player is back on start_screen")



    if(start_screen == True):
        screen.fill((200,100,0))
        screen.blit(title_text_surface,title_text_rect)
    elif(npc_screen == True):
        # Background
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,360))
        screen.blit(portal_surface,portal_rect)

        # Npcs
        screen.blit(npc_surface1,npc1_rect)
        screen.blit(npc_surface2,npc2_rect)


        # Player
        # Get pressed is a dictionary, each key is either True or false
        pressed_keys = pygame.key.get_pressed()
        if(pressed_keys[pygame.K_LEFT]):
            player_rect.x = player_rect.x - 5
        if(pressed_keys[pygame.K_RIGHT]):
            player_rect.x = player_rect.x + 5



        if(player_rect.right > screen_width):
            player_rect.right = screen_width
        if(player_rect.left < 0):
            player_rect.left = 0


        screen.blit(player_surface,player_rect)
        #Player talking with NPC
        if(talking == True):
            screen.blit(npc_text_surface,npc_text_rect)




        #Player collide with portal
        if(player_rect.colliderect(portal_rect) == 1):
            print("Player is on screen 2")
            select_screen = True
            npc_screen = False




    elif(select_screen == True):
        screen.fill((100,100,100))
        screen.blit(screen2_text_surface, screen2_text_rect)    
        screen.blit(customer_select_button_surface,customer_select_button_rect)
        screen.blit(farmer_select_button_surface,farmer_select_button_rect)






    elif(career_1_gamescreen == True):
        screen.blit(office_background_surface,(0,0))
        screen.blit(office_ground_surface,(0,400))
        player_rect.midbottom = (50,400)
        screen.blit(player_surface,player_rect)
        pygame.draw.line(screen,'Black',(100,400),(100,350),5)




        #Checks if a npc rect is at or below the barrier
        if(delete_npc == True):
            if(len(npc_obstacle_rect_list) > 0):
                del(npc_obstacle_rect_list[0])
                starting_time = pygame.time.get_ticks()
                npc_mood = 0
                delete_npc = False
            else:
                delete_npc = False  
       
        if(npc_checker == True):
            if(len(npc_obstacle_rect_list) > 0):
                if(npc_obstacle_rect_list[0].x <= 100):
                    random_question = randint(0,2)
                    print('Random question generated')
                    player_question_answer = True
                    npc_checker = False
                    npc_mood_checker = True
                    # npc_mood = npc_mood + 5
                    # print("NPC mood worsened")
                else:
                    npc_mood_checker = False
                    starting_time = pygame.time.get_ticks()
                   
        if(npc_mood_checker == True):
            current_time = pygame.time.get_ticks() - starting_time
            npc_mood_timer = current_time // 1000
            if(npc_mood_timer > 5):
                npc_mood = npc_mood + 2
                # print(npc_mood)
                starting_time = pygame.time.get_ticks()
            #Make you comment the npc_timer when you are done.
            npc_timer_surface = npc_timer_font.render(f'Mood Timer:{npc_mood_timer}',anti_aliasing,(64,64,64))
            npc_timer_rect = npc_timer_surface.get_rect(center = (150,100))
            screen.blit(npc_timer_surface,npc_timer_rect)
       


        if(player_question_answer == True):
            npc_question_text_surface = npc_question_font.render(npcs_question_list[random_question],anti_aliasing,text_color,texts_background_color)
            npc_question_text_rect = npc_question_text_surface.get_rect(center = (350,100))
            screen.blit(npc_question_text_surface,npc_question_text_rect)
            #If it is then it is going to display a random question
            #If it isnt then it is not going to display a random question




        # The function (npc_movement_waiting) returns the new list with all the moved surface rects.
        # So inorder to move all the surface rects. The list has to keep on changing inorder to update everything
        # It gets that orginal list, then makes the new one the orginal one, and repeats this process
        if(len(npc_obstacle_rect_list) <= 7):
            npc_obstacle_rect_list = npc_movement_waiting(npc_obstacle_rect_list)    
        display_player_score(player_points)




    # WORK ON THIS
    elif(career_1_gameoverscreen == True):
        screen.blit(office_background_surface,(0,0))
        screen.blit(office_ground_surface,(0,400))
        pygame.draw.line(screen,'Black',(100,400),(100,350),5)




    elif(player_labor_screen == True):
        #Background
        screen.blit(farmer_background_surface,(0,0))
        #Animal food score
        screen.blit(animal_food_score_surface,animal_food_score_rect)






        # key animation
        # A and D key controls to change color
        pressed_keys = pygame.key.get_pressed()
        # Switch the white a key surface to the blue a key surface
        if(pressed_keys[pygame.K_a]):
            a_key_detection_index = 1
            a_key_surface = a_key_surface_list[a_key_detection_index]
        else:
            # Else, change both key surface back to the white key surfaces
            a_key_detection_index = 0
            a_key_surface = a_key_surface_list[a_key_detection_index]
        # Switch the white d key surface to the blue d key surface
        if(pressed_keys[pygame.K_d]):
            d_key_detection_index = 1
            d_key_surface = d_key_surface_list[d_key_detection_index]
        else:
            # Else, change both key surface back to the white key surfaces
            d_key_detection_index = 0
            d_key_surface = d_key_surface_list[d_key_detection_index]
       
        #If both keys are pressed down dont get food
        # if(a_key_detection_index and d_key_detection_index == 1):
        #     print("Cant do that")



        # Blit the A and D keys
        screen.blit(a_key_surface,(220,300))
        screen.blit(d_key_surface,(400,300))
        # player
        screen.blit(player_farmer_surface,player_farmer_rect)
        # Truck food/still food
        screen.blit(animal_food_surface,animal_food_rect)



        # display player food points
        display_farmer_score(farmer_food_points)


        # Display stacked food
        player_animal_food_list_rects = display_player_stacked_food(player_animal_food_list_rects)
               
    elif(animal_screen == True):
        # screen.fill((100,100,100))
        # screen.blit(sky_surface,(0,0))
        # screen.blit(ground_surface,(0,360))


        #Background and fences
        screen.blit(farmer_background_surface,(0,0))
        screen.blit(farmer_fence_surface_cow,(380,10))
        screen.blit(farmer_fence_surface_pig,(380,170))
        screen.blit(farmer_fence_surface_sheep,(380,330))



        # animals
        screen.blit(cow_surface,cow_rect)
        screen.blit(pig_surface,pig_rect)
        screen.blit(sheep_white_surface,sheep_white_rect)


        # Text
        # screen.blit(screen4_text_surface, screen4_text_rect)



        #player food / produce
        screen.blit(animal_food_score_surface,animal_food_score_rect)
        screen.blit(milk_surface,(20,10))
        screen.blit(carrot_surface,(60,10))
        screen.blit(wool_surface,(100,10))


        if(feed_cow == True):
            if(farmer_food_points < 4):
                feed_cow = False
                print("Sorry need more food")
            else:
                farmer_food_points = farmer_food_points - 4
                milk_count = milk_count + 1
                feed_cow = False
                print("Feed cow")
        if(feed_pig == True):
            if(farmer_food_points < 1):
                feed_pig = False
                print("Sorry need more food")
            else:
                farmer_food_points = farmer_food_points - 1
                carrot_count = carrot_count + 1
                feed_pig = False
                print("Feed pig")
        if(feed_sheep == True):
            if(farmer_food_points < 2):
                feed_sheep = False
                print("Sorry need more food")
            else:
                farmer_food_points = farmer_food_points - 2
                wool_count = wool_count + 1
                feed_sheep = False
                print("Feed sheep")
       
        display_farmer_score(farmer_food_points)


        update_produce(milk_count,carrot_count,wool_count)


    elif(selling_and_buying_screen == True):
        #Background
        screen.blit(farmer_background_surface,(0,0))


        #Shop board
        # pygame.draw.rect(screen,(146,101,56),shop_background_rect)
        screen.blit(shop_sign_surface,shop_sign_rect)

        #sell / buy produce buttons / images 
        screen.blit(sell_milk_button_surface,sell_milk_button_rect)
        screen.blit(sell_carrot_button_surface,sell_carrot_button_rect)
        screen.blit(sell_wool_button_surface,sell_wool_button_rect)

        screen.blit(milk_surface,(20,10))
        screen.blit(carrot_surface,(60,10))
        screen.blit(wool_surface,(100,10))

        screen.blit(buy_cow_button_surface,buy_cow_button_rect)
        screen.blit(buy_pig_button_surface,buy_pig_button_rect)
        screen.blit(buy_sheep_button_surface,buy_sheep_button_rect)

        screen.blit(cow_surface,(600,200))
        screen.blit(pig_surface,(600,280))
        screen.blit(sheep_white_surface,(600,350))

        # player food Images
        screen.blit(milk_surface,(90,240))
        screen.blit(carrot_surface,(90,310))
        screen.blit(wool_surface,(90,380))


        if(milk_button_press):
            if(milk_count <= 0):
                print("Sorry you have no mroe produce.")
                milk_button_press = False
            else:
                player_money = player_money + 5
                milk_button_press = False
                milk_count = milk_count - 1
                print("Sell milk")
    
        if(carrot_button_press):
            if(carrot_count <= 0):
                print("Sorry you have no mroe produce.")
                carrot_button_press = False
            else:
                player_money = player_money + 2
                carrot_button_press = False
                carrot_count = carrot_count - 1
                print("Sell carrot")
        if(wool_button_press):
            if(wool_count <= 0):
                print("Sorry you have no mroe produce.")
                wool_button_press = False
            else:
                player_money = player_money + 4
                wool_button_press = False
                wool_count = wool_count - 1
                print("Sell wool")

        # Money Text
        update_player_money(player_money)

        # Produce Text
        update_produce(milk_count,carrot_count,wool_count)


    elif(end_screen == True):
        screen.fill((0,100,200))
        screen.blit(screen5_text_surface, screen5_text_rect)





    pygame.display.flip()




    clock.tick(60)
pygame.quit()







