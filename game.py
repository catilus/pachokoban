## Import packages and classes
import json
import pygame
import pygame.locals

from Screen import *
from Pacho import *
from Cheese import *

pygame.init()       # Initializes the display as well as other things

## Loads level structure from .json file
levelfile = json.load(open("level_001.json"))

## Initialize objects
background_color=(255,228,182)
screen = Screen(350, 350, background_color)   # screen width and height are in px

# Display first level
for i in range(0,len(levelfile[0])-1):    # customize this so we don't use integers
    for j in range(0,len(levelfile)):
        position = (i,j)    # save object position
        tile = levelfile[i][j]     # read object to draw
        screen.shows(tile, position, background_color)   # show objects on screen

        # Initializes pacho and cheese objects with their position
        if tile == 'p':
            pacho = Pacho(tile, position)
        elif tile == 'c':
            cheese = Cheese(tile, position)


## Event loop.
while True:
    for event in pygame.event.get():
        
        # If user presses keyboard touch
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
                x_move=0
                y_move=-1
                # calculate pacho's new position
                new_position = (pacho.position[0]+x_move, pacho.position[1]+y_move)

                if 0 <= new_position[1]:   # so that pacho cannot get out of the screen
                    
                    # if there is a wall at new position: do nothing
                    if levelfile[new_position[0]][new_position[1]] == 'w':
                        pass

                    else: 

                        # if there is a cheese on the new position, the cheese moves as well 
                        if levelfile[new_position[0]][new_position[1]] == 'c':
                            # unless there is a wall or other cheese behind
                            if levelfile[new_position[0]+x_move][new_position[1]+y_move] in ['w', 'c']:
                                pass
                            # pacho and cheese move
                            else:
                                screen.shows('b', pacho.position, background_color) # draws background tile on top of pacho
                                pacho.modifyPosition(x_move, y_move)  # modifies pacho's position 
                                screen.shows('b', cheese.position, background_color) # draws background tile on top of cheese
                                cheese.modifyPosition(x_move, y_move)  # modifies cheese's position
                                screen.shows('p', pacho.position, background_color) # draws pacho at new position 
                                screen.shows('c', cheese.position, background_color) # draws cheese behind
                        
                        # otherwise only Pacho moves
                        else:
                            screen.shows('b', pacho.position, background_color) # draws background tile on top of pacho
                            pacho.modifyPosition(x_move, y_move)  # modifies pacho's position  
                            screen.shows('p', pacho.position, background_color) # draws pacho at new position      
                
                else:
                    pass        
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:

                x_move=0
                y_move=1
                # calculate pacho's new position
                new_position = (pacho.position[0]+x_move, pacho.position[1]+y_move)
                
                if new_position[1] <= len(levelfile)-1: 
                    if levelfile[new_position[0]][new_position[1]] == 'w':
                        pass

                    else: 
                        screen.shows('b', pacho.position, background_color) # draws background tile on top of pacho
                        pacho.modifyPosition(x_move, y_move)  # modifies pacho's position 
                        screen.shows('p', pacho.position, background_color) # draws pacho at new position
                
                else:
                    pass   


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                
                x_move=-1
                y_move=0
                # calculate pacho's new position
                new_position = (pacho.position[0]+x_move, pacho.position[1]+y_move)

                if 0 <= new_position[0]:
                    if levelfile[new_position[0]][new_position[1]] == 'w':
                        pass

                    else: 
                        screen.shows('b', pacho.position, background_color) # draws background tile on top of pacho
                        pacho.modifyPosition(x_move, y_move)  # modifies pacho's position 
                        screen.shows('p', pacho.position, background_color) # draws pacho at new position
                
                else:
                    pass   
                 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                
                x_move=1
                y_move=0
                # calculate pacho's new position
                new_position = (pacho.position[0]+x_move, pacho.position[1]+y_move)

                if new_position[0] <= len(levelfile[0])-1:
                    if levelfile[new_position[0]][new_position[1]] == 'w':
                        pass

                    else: 
                        screen.shows('b', pacho.position, background_color) # draws background tile on top of pacho
                        pacho.modifyPosition(x_move, y_move)  # modifies pacho's position 
                        screen.shows('p', pacho.position, background_color) # draws pacho at new position
                
                else:
                    pass            
        
        
        if event.type == QUIT:          # Keeps pygame window open unless asked otherwise
            pygame.quit()
            quit()


#pygame.display.quit()      # closes the display, automatically handled when user exits program