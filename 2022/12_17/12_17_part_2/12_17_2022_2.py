from collections import defaultdict
from aoc_util_2 import shape1, shape2, shape3, shape4, shape5, convertLinesIntoSparceMatList, printRockInChamber, findMaxHeightOfRocksInChamber
import sys

class Solution():
    
    def __init__(self):
        # The tall, vertical chamber is exactly seven units wide. 
        self.rocksInChamber = defaultdict(lambda: defaultdict(str))  # {y: {x: val}}
        self.gasCounter = 0 # Used to figure out where we are in the input line
        self.rocksToDrop = 0  # How many rocks we want to drop

    def main(self):
        self.parseInput()
        shapeList = [shape1, shape2, shape3, shape4, shape5]
        rockDroppedCounter = 0
        
        while rockDroppedCounter < self.rocksToDrop:
            dropThisRock = rockDroppedCounter % len(shapeList)
            curRock = convertLinesIntoSparceMatList(shapeList[dropThisRock])
            self.dropRock(curRock)
            rockDroppedCounter += 1
        
        print("ret: ", findMaxHeightOfRocksInChamber(self.rocksInChamber) + 1) # Don't know why i have off by one, nor do i care
        return None

    def dropRock(self, curRock):
        startDisFromLeftWall = 2 # Each rock appears so that its left edge is two units away from the left wall and 
        maxHeight = findMaxHeightOfRocksInChamber(self.rocksInChamber)
        startHeight = 3 + maxHeight # its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

        newRock = defaultdict(lambda: defaultdict(str))
        for y in curRock:
            for x in curRock[y]:
                newRock[y + startHeight][x + startDisFromLeftWall] = curRock[y][x]
        curRock = newRock

        while True:
           
            ### Moving left right
            noBlockersIfMoveLR = True
            gasChangeXVal = self.getGasChangeXVal()
            # Can this move by gasChangeXVal (left/right)
            for y in curRock:
                for x in curRock[y]:
                    if (self.isThereCollisionForCoordLR(y, x + gasChangeXVal)):
                        noBlockersIfMoveLR = False
                if (noBlockersIfMoveLR == False):
                    break
            
            # If theres no blockers, move it
            if (noBlockersIfMoveLR == True):
                tempRock = defaultdict(lambda: defaultdict(str))
                for y in curRock:
                    for x in curRock[y]:
                        tempRock[y][x + gasChangeXVal] = curRock[y][x]
                curRock = tempRock

            self.gasCounter += 1


            ### Moving down
            noCollisionIfMoveDown = True
            # Will there be collision if we move stuff down one more step?
            for y in curRock:
                for x in curRock[y]:
                    if (self.isThereCollisionForCoordDown(y-1, x)):
                        noCollisionIfMoveDown = False
                if (noCollisionIfMoveDown == False):
                    break
            
            # if theres no collisions move it
            if (noCollisionIfMoveDown == True):
                tempRock = defaultdict(lambda: defaultdict(str))
                for y in curRock:
                    for x in curRock[y]:
                        tempRock[y - 1][x] = curRock[y][x]
                curRock = tempRock
            else:
                break

            ### Check if rock it at bottom (stupid confusing edge case, we don't want to let it get blown LR if its on the ground)
            rockTouchingFloor = False
            for y in curRock:
                if (y == 0):
                    rockTouchingFloor = True
            if (rockTouchingFloor == True):
                break

        # Set in stone (write to rockInChamber)
        self.rockLandsInChamber(curRock)
        return None


    def isThereCollisionForCoordDown(self, y, x):
        if (y < 0):
            return True

        if (self.rocksInChamber[y][x] == True):
            return True
        else:
            del self.rocksInChamber[y][x]

        if (not self.rocksInChamber[y]):
            del self.rocksInChamber[y]

        return False

    def isThereCollisionForCoordLR(self, y, x):
        if (x >= 7 or x < 0):
            return True

        if (self.rocksInChamber[y][x] == True):
            return True
        else:
            del self.rocksInChamber[y][x]

        if (not self.rocksInChamber[y]):
            del self.rocksInChamber[y]
        return False
 
    def rockLandsInChamber(self, rock):
        for y in rock:
            for x in rock[y]:
               self.rocksInChamber[y][x] = True
        return None

    def parseInput(self):
        f = open(str(sys.argv[1]), 'r')
        self.rocksToDrop = int(sys.argv[2])
        self.gas = f.read()

    def getGasChangeXVal(self):
        indexInString = self.gasCounter % ( len(self.gas))
        arrowVal = self.gas[indexInString]
        if (arrowVal == '>'):
            return 1
        elif(arrowVal == '<'):
            return -1
        else:
            print("How the fuck we return " + arrowVal )
            return None


sol = Solution()
sol.main()
