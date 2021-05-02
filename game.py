## Import packages and classes
import json
import pygame
import pygame.locals

from Screen import *
from Pacho import *
from position import *
#from Cheese import *

pygame.init()       # Initializes the display as well as other things

## Loads level structure from .json file
levelfile = json.load(open("level_001.json"))

## Initialize objects
background_color=(255,228,182)
screen = Screen(350, 350, background_color)   # screen width and height are in px
list_of_cheeses = []    # list of cheeses' positions
list_of_spots = []      # list of spots' positions
steps_counter = 0

# Display first level

x_max = len(levelfile[0])-1
y_max = len(levelfile)-1


for x in range(0,x_max):    
    for y in range(0,y_max):
        position = (x,y)    # saves object position
        tile = levelfile[x][y]     # reads which object to show
        screen.shows(tile, position, background_color, steps_counter)   # draws objects on screen

        # Initializes pacho and list of cheeses and spots containing their position
        if tile == 'p':
            pacho = Pacho(tile, position)
        elif tile == 'c':
            list_of_cheeses.append(position) # No need to make an object for each cheese
        elif tile == 's':
            list_of_spots.append(position) # No need to make an object for each spot   

screen.shows('counter', (5,5), background_color, steps_counter) # can we do **kwargs? sometimes we don't need all the arguments to draw one thing

running = True

while running:  # Keeps pygame window opened unless asked otherwise
    
    # Event loop.
    for event in pygame.event.get():
        
        # If user presses keyboard touch
        if event.type == pygame.KEYDOWN:  

            position = pacho.position
            x_move=0 
            y_move=0          

            if event.key == pygame.K_LEFT:             
                y_move-=1

            elif event.key == pygame.K_RIGHT:
                y_move+=1    

            elif event.key == pygame.K_UP:             
                x_move-=1

            elif event.key == pygame.K_DOWN:            
                x_move+=1
                
            # calculate pacho's new position
            new_position = (position[0]+x_move, position[1]+y_move)

            # if pacho's new position is inside screen, proceed
            if positionInScreen(new_position, x_max, y_max):   

                if new_position in list_of_cheeses:   # if cheese at new position
                    
                    # calculate position of object behind cheese
                    behind_new_position = (new_position[0]+x_move, new_position[1]+y_move)

                    # check if the next new position of the cheese is in the screen    
                    if positionInScreen(behind_new_position, x_max, y_max):
                        
                        # if wall or cheese behind new position, do not move
                        if checkPosition(behind_new_position, levelfile) == 'w' or behind_new_position in list_of_cheeses:
                            pass

                        else:   
                            pacho.position = new_position
                            
                            # modify cheese's position
                            cheese_position_in_list = list_of_cheeses.index(new_position)
                            list_of_cheeses[cheese_position_in_list] = behind_new_position
                            
                            # increments steps counter
                            steps_counter += 1  
                            screen.shows('counter', (5,5), background_color, steps_counter)

                            tiles = drawAtPosition(position, list_of_spots) 
                            for tile in tiles:
                                screen.shows(tile, position, background_color, steps_counter)
                                
                            tiles = drawAtNewPosition(new_position)
                            for tile in tiles:
                                screen.shows(tile, new_position, background_color, steps_counter)  
        
                            tiles = drawBehindNewPosition(behind_new_position, list_of_spots)
                            for tile in tiles:
                                screen.shows(tile, behind_new_position, background_color, steps_counter)  
                    else:
                        pass

                elif  checkPosition(new_position, levelfile) == 'w': # if wall at new position
                    pass        
                
                else: 

                    pacho.position = new_position
                    
                    # increments steps counter
                    steps_counter += 1  
                    screen.shows('counter', (5,5), background_color, steps_counter)
                    
                    tiles = drawAtPosition(position, list_of_spots) 
                    for tile in tiles:
                        screen.shows(tile, position, background_color, steps_counter)
                    
                    tiles = drawAtNewPosition(new_position)
                    for tile in tiles:
                        screen.shows(tile, new_position, background_color, steps_counter)

            else:
                pass 

            # all the cheeses are on the spots, shows congratulations screen --> could be a while loop
            if sorted(list_of_cheeses)==sorted(list_of_spots):  
                screen.shows('victory', (0,0), background_color, steps_counter)
            
            else:
                pass    

            # if event.key == pygame.K_ESCAPE:    # Display options screen

            #     screen.shows('menu', (0,0), background_color, steps_counter)
                
            #     if event.type == pygame.KEYDOWN:
                    
            #         if event.key == pygame.K_q:     # Quit the game
            #             running is False
            #         #elif event.key == pygame.K_RETURN:  # Resume game
            #         #    pass
            #         #elif event.key == pygame.K_r:   # Restart game
            #         #    pass   
        
        if event.type == QUIT:          
            pygame.quit()
            quit()


pygame.display.quit()      # closes the display, automatically handled when user exits program