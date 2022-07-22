# python2 -u Tilegame_prototype2.py Level.txt

#----
def convertFileToList(): 
    # Converts file to list

    from sys import argv
    script, file = argv
    fileData = open(file)
    content = fileData.read() 
    fileData.close()
    
    lines = content.splitlines() # Divide string into list of lines
    yLen = len(lines) # How long vertically the map is
    len_x = lines[0].split() # Divide first line into a list of characters in it.
    xLen = len(len_x) # How long the map horisontaly is
    
    contentList = [[0 for i in range(xLen)] for j in range(yLen)]
    # This line generates the map with each tile having the value 0.
    # All changes to tiles are going to be made with the setCoordinate() function.

    for i in range(yLen):
        for j in range(xLen):
            fill = lines[i][j * 2] # *2 multiplier comes from having to skip whitespaces.
            setCoordinate(contentList, j, i, fill)
    # This for loop replaces each tile with corresponding value from the txt file.    
    
    #print yLen
    #print xLen
    
    return contentList

#----
def convertListToString(contentList):
    #Take the game board and turn it into a string for printing.
    
    yLen = len(contentList)
    xLen = len(contentList[0])
    # Width and lenght of board.
    
    string = "" 
    row = ""
    
    for i in range(yLen):
        for j in range(xLen):
            row = row + str(contentList[i][j]) + " "
        string = string + row + "\n"
        row = ""
    # This loop constructs a string using the list.
    # The inner loop creates a string containing one line of the contentList.
    # The outer loop takes the line-strings and combines them to one.
    
    
    return string

#----
def setCoordinate(contentList, x, y, change): 
    # takes one square on the board and changes the character in it to another.
    if change == " ":
        pass  # In case the level is typed wrong 0 will be typed on effected tiles.
    else:
        targetRow = contentList[y]
        targetCharacter = targetRow[x]
        targetRow[x] = change
        contentList[y] = targetRow
    
    return contentList  

#----
def findCoordinates(contentList, target):
    #Returns a list in which each element is the coordinate for one of the targets.
    #example coordinateList = [[1, 3] [2, 4]]
    
    coordinateList = []
    
    yLen = len(contentList)
    xLen = len(contentList[0])
    
    for i in range(yLen):
        for j in range(xLen):
            tile = contentList[i][j]
            if str(tile) == str(target):
                newCoordinate = [j, i]
                coordinateList.append(newCoordinate)
            else:
                pass
    # The double loop goes trough every value in the contentList. 
    # On each tile the if statement checks if the the tile contains a wanted value.
    # If it does, then the values [j, i] are appended to the coordinateList.
    # If it doesnt, then nothing is done.
    
    return coordinateList

#----
def lookUpCoordinates(contentList, targetCoordinates):
    # Returns list with the contents of coordinates in the given order.
    # Takes: (contentList, [[x, y], [x, y], [x, y]])
    # Returns: ['?', '?', '?']
    
    coordinateContentList = []
    
    listLenght = len(targetCoordinates)
    
    for i in range(listLenght):
        targetX = targetCoordinates[i][0]
        targetY = targetCoordinates[i][1]
        
        targetContent = contentList[targetY][targetX]
        
        coordinateContentList.append(targetContent)
        
    return coordinateContentList
    
#---- 
def playerTurn(contentList):
    #The playerTurn function takes input from player and updates the contentList accordingly.
    playerInput = raw_input("> ")    
    
    if playerInput == "exit":
        #save contentList to savefile
        exitGame(contentList)
    elif playerInput == "w":
        contentList = wAction(contentList)
    elif playerInput == "a":
        contentList = aAction(contentList)
    elif playerInput == "s":
        contentList = sAction(contentList)
    elif playerInput == "d":
        contentList = dAction(contentList)
    else:
        print "The valid controls are w, a, s, d for movement\nand exit for quiting the game."
        print convertListToString(contentList)
        playerTurn(contentList)
    
    return contentList
    
#----
def exitGame(contentList):
    # Whrites contentList to file and exits the game.
    
    string = convertListToString(contentList)
    
    #### bug after this
    
    from sys import argv
    script, file = argv

    fileData = open(file, 'w')
    
    #print fileData.read()
    
    fileData.truncate()
    
    #print fileData.read()
    
    fileData.write(string)
    
    #print fileData.read()
    
    fileData.close()
    
    #### bug before this
    
    print string
    
    
    exit()
    



def wAction(contentList):

    playerLocation = findCoordinates(contentList, "@") # Get player coordinates
    
    # @ [[playerx, playery]]
    
    playerX = playerLocation[0][0]
    playerY = playerLocation[0][1]
    
    # @ playerx playery
    
    wPlayerSurroundings = [[playerX, playerY - 1]]
    
    # @ playerx playery [[coordinate of tile above player]]
    
    wFromPlayerB = lookUpCoordinates(contentList, wPlayerSurroundings)
    wFromPlayer = wFromPlayerB[0]
    
    print wFromPlayer
    
    # @ playerx playery [[coordinate of tile above player]] ['content of tile above player']
    
    wXCoordinate = playerLocation[0][0]
    wYCoordinate = playerLocation[0][1] - 1
    
    # @ playerx playery [[coordinate of tile above player]] ['content of tile above player'] xCoordinate_of_target_tile y_Coordinate_of_target_tile 
    
    if wFromPlayer == "#":
        print "You can't walk trough walls"
    elif wFromPlayer == ".":
        contentList = setCoordinate(contentList, wXCoordinate, wYCoordinate, "@") # Add player character
        contentList = setCoordinate(contentList, playerX, playerY, ".") # Remove old character
    else:
        print "Something in the way. Uuhhhh..."
    
    return contentList
    
def aAction(contentList):

    playerLocation = findCoordinates(contentList, "@") # Get player coordinates
    
    print "a"
    
    playerX = playerLocation[0][0]
    playerY = playerLocation[0][1]
    # Take coordinate variables out of the lists
    
    aPlayerSurroundings = [[playerX - 1, playerY]]
    # List containing coordinates of tile left from player for lookUpCoordinates() to use.
    
    aFromPlayerB = lookUpCoordinates(contentList, aPlayerSurroundings)
    aFromPlayer = aFromPlayerB[0]
    # Tilecontent of tile left from player
    
    #print aFromPlayer
    
    aXCoordinate = playerLocation[0][0] - 1
    aYCoordinate = playerLocation[0][1]
    # Get coordinates of tile left from player. [x, y + 1] 
    
    if aFromPlayer == "#":
        print "You can't walk trough walls"
    elif aFromPlayer == ".":
        contentList = setCoordinate(contentList, aXCoordinate, aYCoordinate, "@") # Add player character
        contentList = setCoordinate(contentList, playerX, playerY, ".") # Remove old character
    else:
        print "Something in the way. Uuhhhh..."
    
    return contentList
    
def sAction(contentList):

    playerLocation = findCoordinates(contentList, "@") # Get player coordinates
    
    playerX = playerLocation[0][0]
    playerY = playerLocation[0][1]
    # Take coordinate variables out of the lists
    
    sPlayerSurroundings = [[playerX, playerY + 1]]
    # List containing coordinates of tile below player for lookUpCoordinates() to use.
    
    sFromPlayerB = lookUpCoordinates(contentList, sPlayerSurroundings)
    sFromPlayer = sFromPlayerB[0]
    # Tilecontent of tile below player
    
    #print sFromPlayer
    
    sXCoordinate = playerLocation[0][0]
    sYCoordinate = playerLocation[0][1] + 1
    # Get coordinates of tile below player. [x, y + 1] 
    
    if sFromPlayer == "#":
        print "You can't walk trough walls"
    elif sFromPlayer == ".":
        contentList = setCoordinate(contentList, sXCoordinate, sYCoordinate, "@") # Add player character
        contentList = setCoordinate(contentList, playerX, playerY, ".") # Remove old character
    else:
        print "Something in the way. Uuhhhh..."
    
    return contentList

def dAction(contentList):
    
    playerLocation = findCoordinates(contentList, "@") # Get player coordinates
    
    playerX = playerLocation[0][0]
    playerY = playerLocation[0][1]
    # Take coordinate variables out of the lists
    
    dPlayerSurroundings = [[playerX + 1, playerY]]
    # List containing coordinates of tile right of player for lookUpCoordinates() to use.
    
    dFromPlayerB = lookUpCoordinates(contentList, dPlayerSurroundings)
    dFromPlayer = dFromPlayerB[0]
    # Tilecontent of tile right from player
    
    #print dFromPlayer
    
    dXCoordinate = playerLocation[0][0] + 1
    dYCoordinate = playerLocation[0][1]
    # Get coordinates of tile right of player. [x + 1 , y]
    
    # @ playerx playery [[coordinate of tile above player]] ['content of tile above player'] xCoordinate_of_target_tile y_Coordinate_of_target_tile 
    
    if dFromPlayer == "#":
        print "You can't walk trough walls"
    elif dFromPlayer == ".":
        contentList = setCoordinate(contentList, dXCoordinate, dYCoordinate, "@") # Add player character
        contentList = setCoordinate(contentList, playerX, playerY, ".") # Remove old character
    else:
        print "Something in the way. Uuhhhh..."
    
    return contentList


# not done yet
def environmentTurn(contentList):
    #The environmentTurn function first generates a list of entities that have a turn.
    #It then generates a turn for each individual entity and updates contentlist accordingly.
    print "wip"
    
    
#alteredList = setCoordinate(contentList, 2, 3, "K")

# print convertListToString(alteredList)



# No functions after this.

contentList = convertFileToList()

temp = True

while temp == True:

    print convertListToString(contentList) # Draw contentList to screen.
    
    contentList = playerTurn(contentList) # Update contentList with player input.
    
    #contentList = environmentTurn(contentList) # Update contentList with NPC input.
    

# The marking #---- in the beginning of codeblocks means that bugs are yet to be encountered in said blocks.
