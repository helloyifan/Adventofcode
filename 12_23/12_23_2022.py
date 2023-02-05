import sys

class Solution():
    sparceMatrix = {} # sparce matrix [(row, col): '#'] tuple where they are both numbers
    status = {}
    stepsToTake = 0

    stepCounter = 0
    def __init__(self):
        self.parseInput()
    
    def main(self):
        # Debug
        #print(self.sparceMatrix)

        print("Initial State")        
        self.printer()
        
        for i in range(self.stepsToTake):
            self.executeStep()
            self.printer()


        print("smallest rectangle: ", self.smallestRectangle())
        return None

    def tryMoving(self, direction,  elfRow, elfCol):
        if (direction == 0):
            return self.checkNorth(elfRow - 1, elfCol)
        elif(direction == 1):
            return self.checkSouth(elfRow + 1, elfCol)
        elif(direction == 2):
            return self.checkWest(elfRow, elfCol - 1)
        elif(direction == 3):
            return self.checkEast(elfRow, elfCol + 1)
        print("this is bad")
        return None


    def executeStep(self):
        plannedNextElfMove = {} # plannedNextElfMove: {location: currentElfLocation}

        for elfCoord in self.sparceMatrix:
            elfRow, elfCol = elfCoord[0], elfCoord[1]
            finalDirection = None

            if (self.checkAround(elfRow, elfCol)):
                self.setPlanNextElfMove((elfRow, elfCol), elfCoord, plannedNextElfMove)
            else:
                for i in range(4):
                    direction = (self.stepCounter  + i) % 4
                    print(direction)
                    if (self.tryMoving(direction, elfRow, elfCol)):
                        finalDirection = direction

            
            if(finalDirection == 0):
                self.setPlanNextElfMove((elfRow - 1, elfCol), elfCoord, plannedNextElfMove)

            elif(finalDirection == 1):
                self.setPlanNextElfMove((elfRow + 1, elfCol), elfCoord, plannedNextElfMove)

            elif(finalDirection == 2):
                self.setPlanNextElfMove((elfRow, elfCol - 1), elfCoord, plannedNextElfMove)

            elif(finalDirection == 3):
                self.setPlanNextElfMove((elfRow, elfCol + 1), elfCoord, plannedNextElfMove)


        #Execute changes
        # Not sure about logic here, but basically just taking all of the moves in plannedNextElfMove
        # (Even those who didnt move would be recorded there)
        updatedSparceMatrix = {}
        
        for key, val in plannedNextElfMove.items():
            # If only one elf wants to move to this slot
            if (len(val) == 1):
                updatedSparceMatrix[key] = '#'

            # Collision between elves, so they don't move
            # Could be collision between many elves
            elif(len(val) > 1):
                for preLocs in val:
                    updatedSparceMatrix[preLocs] = '#'
            else:
                print("not sure whats happening here")


        # Replace self.sparceMatrix with our newly created one 
        self.sparceMatrix = updatedSparceMatrix
        return None

    def handleNorth(self, elfRow, elfCol, elfCoord, plannedNextElfMove):
        if(self.checkNorth(elfRow, elfCol)):
                self.setPlanNextElfMove((elfRow - 1, elfCol), elfCoord, plannedNextElfMove)


    def setPlanNextElfMove(self, nextLoc, curLoc, plannedNextElfMove):
        if (nextLoc in plannedNextElfMove):
            plannedNextElfMove[nextLoc].append(curLoc)
        else:
            plannedNextElfMove[nextLoc] = [curLoc]


    def checkNorth(self, row, col):
        nobodyNorth = True
        if (
            self.checkRowCol(row - 1, col - 1) or 
            self.checkRowCol(row - 1, col) or 
            self.checkRowCol(row - 1, col + 1)):
            nobodyNorth = False
        return nobodyNorth

    def checkSouth(self, row, col):
        nobodySouth = True
        if (
            self.checkRowCol(row + 1, col - 1) or 
            self.checkRowCol(row + 1, col) or 
            self.checkRowCol(row + 1, col + 1)):
            nobodySouth = False
        return nobodySouth
    
    def checkEast(self, row, col):
        nobodyEast = True
        if (
            self.checkRowCol(row - 1, col + 1) or 
            self.checkRowCol(row, col + 1) or 
            self.checkRowCol(row + 1, col + 1)):
            nobodyEast = False
        return nobodyEast

    def checkWest(self, row, col):
        nobodyWest = True
        if (
            self.checkRowCol(row - 1, col - 1) or 
            self.checkRowCol(row, col - 1) or 
            self.checkRowCol(row + 1, col - 1)):
            nobodyWest = False
        return nobodyWest

    # During the first half of each round, each Elf considers the eight positions adjacent to themself. 
    # If no other Elves are in one of those eight positions, the Elf does not do anything during this round. 
    def checkAround(self, row, col):
        nobodyAround = True
        if (
            self.checkRowCol(row - 1, col - 1) or 
            self.checkRowCol(row - 1, col) or 
            self.checkRowCol(row - 1, col + 1) or 
            self.checkRowCol(row, col - 1) or 
            self.checkRowCol(row, col + 1) or 
            self.checkRowCol(row + 1, col - 1) or 
            self.checkRowCol(row + 1, col) or 
            self.checkRowCol(row + 1, col + 1)):
            nobodyAround = False
        return nobodyAround


    def parseInput(self):
        f = open(str(sys.argv[1]), 'r')
        self.stepsToTake = int(sys.argv[2])

        for rowCounter, row in enumerate(f):
            for colCounter, col in enumerate(row):
                if (col == '#'):
                    self.sparceMatrix[rowCounter, colCounter] = '#'

        return None
    
    def checkRowCol(self, row, col):
        keyTuple = (row, col)
        if (keyTuple in self.sparceMatrix):
            if (self.sparceMatrix[keyTuple] != '#'):
                print("Something is wrong at: ", keyTuple)
            return True
        
        return False


    def printer(self):
        maxRowVal, maxColVal = float('-inf'), float('-inf')
        minRowVal, minColVal = float('inf'), float('inf')

        for key in self.sparceMatrix:
            maxRowVal = max(maxRowVal, key[0] + 2) # Add 2 off set for better views
            maxColVal = max(maxColVal, key[1] + 2)

            minRowVal = min(minRowVal, key[0] - 2)
            minColVal = min(minColVal, key[1] - 2)


        for row in range(minRowVal, maxRowVal):
            line = ''
            for col in range(minColVal, maxColVal):
                keyTuple = (row, col)

                if (keyTuple in self.sparceMatrix and self.sparceMatrix[keyTuple] == '#'):
                    line += '#'
                else:
                    line +='.'
            print(line)
        print('>>>>>>>>>>>>>>>')
        return None
    
    def smallestRectangle(self):
        maxRowVal, maxColVal = float('-inf'), float('-inf')
        minRowVal, minColVal = float('inf'), float('inf')
        numberOfElves = len(self.sparceMatrix)

        for key in self.sparceMatrix:
            maxRowVal = max(maxRowVal, key[0]) # Add 2 off set for better views
            maxColVal = max(maxColVal, key[1])
            
            minRowVal = min(minRowVal, key[0] - 2)
            minColVal = min(minColVal, key[1] - 2)

        rowVal = maxRowVal - minRowVal
        colVal = maxColVal - minColVal
        

        return (rowVal * colVal) - numberOfElves

sol = Solution()
sol.main()