## Import packages and classes
import json
import pygame
import pygame.locals

from Screen import *
from Pacho import *
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

for i in range(0,len(levelfile[0])-1):    
    for j in range(0,len(levelfile)):
        position = (i,j)    # saves object position
        tile = levelfile[i][j]     # reads which object to show
        screen.shows(tile, position, background_color, steps_counter)   # shows objects on screen

        # Initializes pacho and list of cheeses and spots containing their position
        if tile == 'p':
            pacho = Pacho(tile, position)
        elif tile == 'c':
            list_of_cheeses.append(position) # No need to make an object for each cheese
        elif tile == 's':
            list_of_spots.append(position) # No need to make an object for each spot   

screen.shows('counter', (5,5), background_color, steps_counter)

## Event loop.
while True:
    for event in pygame.event.get():
        
        # If user presses keyboard touch
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:             
                x_move=0
                y_move=-1

            elif event.key == pygame.K_RIGHT:
                x_move=0
                y_move=1    

            elif event.key == pygame.K_UP:             
                x_move=-1
                y_move=0  

            elif event.key == pygame.K_DOWN:            
                x_move=1
                y_move=0     
                
            # calculate pacho's new position
            new_position = (pacho.position[0]+x_move, pacho.position[1]+y_move)
            # calculate position of object behind pacho
            next_new_position = (new_position[0]+x_move, new_position[1]+y_move)

            # if pacho's new position is inside screen, proceed
            if 0 <= new_position[0] <= len(levelfile)-1 and 0 <= new_position[1] <= len(levelfile[0])-1:   
                    
                # if there is a wall at new position: do nothing
                if levelfile[new_position[0]][new_position[1]] == 'w':
                    pass

                else: 
                    # if there is a cheese on the new position, the cheese moves as well 
                    if new_position in list_of_cheeses:

                        # if the next new position of the cheese is in the screen    
                        if 0 <= next_new_position[0] <= len(levelfile)-1 and 0 <= next_new_position[1] <= len(levelfile[0])-1:
                        
                            # cheese doesn't move if there is a wall on next new position
                            if levelfile[next_new_position[0]][next_new_position[1]] == 'w':
                                pass
                            # cheese doesn't move if there is another cheese on next new position
                            elif next_new_position in list_of_cheeses:
                                pass
                            # otherwise cheese moves
                            else:    
                                # if Pacho moves onto a spot position, draws background and spot tile on top of Pacho
                                if levelfile[pacho.position[0]][pacho.position[1]] == 's':
                                    screen.shows('b', pacho.position, background_color, steps_counter)
                                    screen.shows('s', pacho.position, background_color, steps_counter) 
                                else: # draws only background tile on top of pacho
                                    screen.shows('b', pacho.position, background_color, steps_counter) 
                                
                                pacho.modifyPosition(x_move, y_move)  # modifies pacho's position 
                                screen.shows('b', pacho.position, background_color, steps_counter) # draws background tile on top of cheese
                                screen.shows('p', pacho.position, background_color, steps_counter) # draws pacho at new position 

                                steps_counter += 1  # increments steps counter
                                screen.shows('counter', (5,5), background_color, steps_counter)

                                # modify cheese's position
                                cheese_position_in_list = list_of_cheeses.index(new_position)
                                list_of_cheeses[cheese_position_in_list] = next_new_position
                                
                                # if cheese moves onto a spot position, draws eaten cheese
                                if levelfile[next_new_position[0]][next_new_position[1]] == 's':
                                    screen.shows('e', next_new_position, background_color, steps_counter) 
                                else: # draws full cheese 
                                    screen.shows('c', next_new_position, background_color, steps_counter) # draws cheese behind
                        
                        # otherwise pass
                        else:
                            pass
                        
                    # otherwise only Pacho moves
                    else:
                        # if Pacho was on a spot, draws background and spot tile on top of Pacho
                        if levelfile[pacho.position[0]][pacho.position[1]] == 's':
                            screen.shows('b', pacho.position, background_color, steps_counter)
                            screen.shows('s', pacho.position, background_color, steps_counter) 
                        else: # draws only background tile on top of pacho
                            screen.shows('b', pacho.position, background_color, steps_counter) 

                        pacho.modifyPosition(x_move, y_move)  # modifies pacho's position  
                        screen.shows('p', pacho.position, background_color, steps_counter) # draws pacho at new position     
                        steps_counter += 1 
                        screen.shows('counter', (5,5), background_color, steps_counter)

            else:
                pass   
    
            if sorted(list_of_cheeses)==sorted(list_of_spots):  
                #print("You solved this level in {} steps".format(steps_counter))    
                screen.shows('victory', (0,0), background_color, steps_counter)
            else:
                pass    
            
        
        if event.type == QUIT:          # Keeps pygame window open unless asked otherwise
            pygame.quit()
            quit()


#pygame.display.quit()      # closes the display, automatically handled when user exits program