import sys
import re

class Solution():
    sparceMatrix = {}
    directionInstructions = None
    numOfRowsInput = 0
    numOfColsInput = 0 

    direction = 'R'
    cPos = None

    def main(self):
        self.parseInput()
        
        ## Setup
        # self.drawSparceMatrix()
        # print(self.directionInstructions)
        # print(self.sparceMatrix)
   
        # print('numOfRowsInput: ', self.numOfRowsInput)
        # print('numOfColsInput: ', self.numOfColsInput)

        self.executeAInstruction(self.directionInstructions[0])
        self.drawSparceMatrix()

        return 0
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


    def executeAInstruction(self, instruction):
        steps = instruction[0]
        turnDirection = instruction[1]

        for i in range(0, steps):
            canTakeStep = self.canTakeStepWithStep(self.direction, self.cPos)
            if (canTakeStep[0]):
                self.cPos = canTakeStep[1]
        return None

    # Returns a bool on whether or not we can take the step
    # also resturns the newPos if we can take the step
    def canTakeStepWithStep(self, dir, curPos):
        newPos = self.newPosGen(dir, curPos)
        if (newPos in self.sparceMatrix):
            if (self.sparceMatrix[newPos] == '#'):
                return (False, None)
            elif(self.sparceMatrix[newPos] == '.'):
                return (True, newPos)
        else:
            print("im not sure why this is happening")

    
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
                if ((col, row) == self.cPos):
                    printRow += 'J'
                elif ((col,row) in self.sparceMatrix):
                    printRow += self.sparceMatrix[(col, row)]
                else:
                    printRow += '@'
            print(printRow)
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
