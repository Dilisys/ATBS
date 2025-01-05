# Conway's game of life
import random, time, copy
WIDTH = 60
HEIGHT = 20

#Create a list of lists for the cells

nextCells = []

#Randomly add living or dead cells
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)

#main loop
while True:
    print('\n\n\n\n\n') #seperate steps
    currentCells = copy.deepcopy(nextCells)

    #print current step to screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print() #prints new line
    
    #calculating next step
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #get neighboring coords:
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            #count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 #topleft neighbor
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 #top neighbor
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 #top-right neighbor
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 #left neighbor
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 #right neighbor
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 #bottom left neighbor
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 #bottom neighbor
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 #bottom right neighbor
            
            #apply game of life rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #if a living cell has 2-3 neighbors it stays alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                #dead cells with 3 neighbors live
                nextCells[x][y] = '#'
            else:
                #die
                nextCells[x][y] = ' '
            
    time.sleep(0.5)    