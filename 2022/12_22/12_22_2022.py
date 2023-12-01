import sys
import re

class Solution():
    sparceMatrix = {}
    walkedPath = {}
    directionInstructions = None
    
    numOfRowsInput = 0
    numOfColsInput = 0 

    direction = 'R'
    cPos = None

    def main(self):
        self.parseInput()
        
        ## Setup
        #self.drawSparceMatrix()
        #print(self.directionInstructions)
        # print(self.sparceMatrix)
   
        # print('numOfRowsInput: ', self.numOfRowsInput)
        # print('numOfColsInput: ', self.numOfColsInput)

        # Doest work
        # self.executeAInstruction(self.directionInstructions[0])
        # self.executeAInstruction(self.directionInstructions[1])
        # self.executeAInstruction(self.directionInstructions[2]) #fails here 

        # Doesnt work yet
        for i in self.directionInstructions:
            self.executeAInstruction(i)
        
        self.drawSparceMatrix()

        ret = self.computeResult()
        print("The key combination ret value is: ", ret)
        return 0
    
    def computeResult(self):
        # Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^). 
        # The final password is the sum of 1000 times the row, 4 times the column, and the facing
        rowVal = 1000* (self.cPos[0] + 1)
        colVal = 4* (self.cPos[1] + 1)
        dirVal = None

        if (self.direction == 'R'):
            dirVal = 0
        elif(self.direction == 'L'):
            dirVal = 2
        elif(self.direction == 'U'):
            dirVal = 3
        elif(self.direction == 'D'):
            dirVal = 1
        return rowVal + colVal + dirVal

    def parseInput(self):
        f = open(str(sys.argv[1]), 'r')
        numLines = sum(1 for line in f)
        f.seek(0) # Back to top of file
        self.numOfRowsInput = numLines - 3 # -3 bcuz theres a new line at the end of file (idk i should fix this)
        puzzleMapFileEnd = numLines -1
        for rowNum in range(0, puzzleMapFileEnd):
            row = f.readline()
            self.numOfColsInput = max(self.numOfColsInput, len(row))
            for colNum in range(0, len(row)):
                col = row[colNum]
                if (col != ' ' and col != '\n'):
                    self.sparceMatrix[(rowNum, colNum)] = col
                    ### Lasy but should work
                    if self.cPos == None:
                        self.cPos = (rowNum, colNum)

        directionInput = f.read()
        regex = '(?P<steps>[0-9]+)(?P<direction>[A-Z]+)'
        matches = re.findall(regex, directionInput) # a bit of magic that i dont quite understand here
        self.directionInstructions = [(int(m[0]), m[1]) for m in matches]

        ## So i fked up this part, the directionInput ends with a steps val
        finalStepVal = re.match('.*?([0-9]+)$', directionInput).group(1)

        self.directionInstructions.append(( int(finalStepVal), None)) #R is just a random direction it doesnt matter
        return 0


    def executeAInstruction(self, instruction):
        steps = instruction[0]
        turnDirection = instruction[1]

        # handle steps
        self.handleSteps(steps)

        # handle turns
        self.handleTurning(turnDirection)

        return None
    
    def handleSteps(self, steps):
        for i in range(0, steps):
            self.walkedPath[self.cPos[0], self.cPos[1]] = self.symbolTranslation(self.direction) # There is some overwriting here
            canTakeStep = self.canTakeStepWithStep(self.direction, self.cPos)
            if (canTakeStep[0]):
                self.cPos = canTakeStep[1]

    def handleTurning(self, turnDirection):
        if (turnDirection == None):
            return # used for the last step bcuz i fked up input parsing
        if turnDirection == 'R':
            if (self.direction == 'R'):
                self.direction = 'D'
            elif (self.direction == 'D'):
                self.direction = 'L'
            elif (self.direction == 'L'):
               self.direction = 'U'
            elif (self.direction == 'U'):
                self.direction = 'R'

        elif turnDirection == 'L':
            if (self.direction == 'R'):
                self.direction = 'U'
            elif (self.direction == 'U'):
                self.direction = 'L'
            elif (self.direction == 'L'):
               self.direction = 'D'
            elif (self.direction == 'D'):
                self.direction = 'R'

    # Returns a bool on whether or not we can take the step
    # also resturns the newPos if we can take the step
    def canTakeStepWithStep(self, dir, curPos):
        newPos = self.findNextSpot(dir, curPos)
        if (newPos in self.sparceMatrix):
            if (self.sparceMatrix[newPos] == '#'):
                return (False, None)
            elif(self.sparceMatrix[newPos] == '.'):
                return (True, newPos)
        else:
            print("im not sure why this is happening", newPos)

    def findNextSpot(self, dir, curPos):
        newPos = self.newPosGen(dir, curPos)
        while (not newPos in self.sparceMatrix):
            newPos = self.newPosGen(dir, newPos)
        return newPos
    
    def newPosGen(self, dir, curPos):
        if (not(dir == 'L' or dir == 'R' or dir == 'U' or dir == 'D')):
            print ("ur a fking idiot")
            return None
        ## Wrap around logic:
        if (dir == 'L'):
            newPos = (curPos[0], 
                      curPos[1] - 1 if curPos[1] - 1 >= 0 else self.numOfColsInput)
        elif (dir == 'R'):
            newPos = (curPos[0], 
                      curPos[1] + 1 if curPos[1] + 1 <= self.numOfColsInput else 0)
        elif (dir == 'D'):
            newPos = (curPos[0] + 1 if curPos[0] + 1  <= self.numOfRowsInput else 0, 
                      curPos[1])
        elif (dir == 'U'):
            newPos = (curPos[0] - 1 if curPos[0] - 1  >= 0 else self.numOfRowsInput, 
                      curPos[1])
        return newPos
    
    def drawSparceMatrix(self):
        for col in range (0, self.numOfRowsInput + 1):
            printRow = ''
            for row in range(0, self.numOfColsInput + 1):
                if ((col, row) in self.walkedPath):
                    printRow += self.walkedPath[(col, row)]
                elif ((col,row) in self.sparceMatrix):
                    printRow += self.sparceMatrix[(col, row)]
                else:
                    printRow += ' '
            print(printRow)
        return None
    
    def symbolTranslation(self, sym):
        if (sym == 'R'):
            return '>'
        elif(sym == 'L'):
            return '<'
        elif(sym == 'U'):
            return '^'
        elif(sym == 'D'):
            return 'v'
        return None
sol = Solution()
sol.main()


# print('Print Validiate R:', sol.newPosGen('R', (3, 16)))
# print('Print Validiate R:', sol.newPosGen('R', (3, 17)))

# print('Print Validiate L:', sol.newPosGen('L', (4, 1)))
# print('Print Validiate L:', sol.newPosGen('L', (4, 0)))

# print('Print Validiate D:', sol.newPosGen('D', (10, 5)))
# print('Print Validiate D:', sol.newPosGen('D', (14, 5)))

# print('Print Validiate U:', sol.newPosGen('U', (1, 6)))
# print('Print Validiate U:', sol.newPosGen('U', (0, 6)))


#You guessed 27464 (it is too low)