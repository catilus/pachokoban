def checkPosition(position, levelfile):
    '''Checks tile at position in levelfile'''
    return levelfile[position[0]][position[1]]

def positionInScreen(position, x_max, y_max):
    '''Checks if position is within the screen'''    
    if 0 <= position[0] <= x_max and 0 <= position[1] <= y_max:
        return True
    else:
        return False

def drawAtPosition(position, list_of_spots):
    if position in list_of_spots:
        return ["-", "s"]
    else: 
        return ["-"]

def drawAtNewPosition(position):   
    return ["-", "p"]

def drawBehindNewPosition(position, list_of_spots):     
    if position in list_of_spots:
        return ["-", "e"]
    else: 
        return ["-", "c"]

