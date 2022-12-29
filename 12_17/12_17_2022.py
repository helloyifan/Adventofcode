from collections import defaultdict
from aoc_util import shape1, shape2, shape3, shape4, shape5, convertLinesIntoSparceMatList, printRockInChamber, findMaxHeightOfRocksInChamber
import sys

class Solution():
    
    def __init__(self):
        # The tall, vertical chamber is exactly seven units wide. 
        self.rocksInChamber = defaultdict(lambda: defaultdict(str))  # {y: {x: val}}
        self.maxHeight = 0
        self.gasCounter = 0 


    def main(self):
        self.parseInput()
        # self.figureOutPositionBeforeDrop(shape2)
        curRock = convertLinesIntoSparceMatList(shape2)
        self.dropRock(curRock)
        
        printRockInChamber(self.rocksInChamber)
        return None

    def dropRock(self, curRock):
        startDisFromLeftWall = 2 # Each rock appears so that its left edge is two units away from the left wall and 
        maxHeight = findMaxHeightOfRocksInChamber(self.rocksInChamber)
        startHeight = 3 + maxHeight # its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

        print(startHeight)

        newRock = defaultdict(lambda: defaultdict(str))
        for y in curRock:
            for x in curRock[y]:
                newRock[y + startHeight][x + startDisFromLeftWall] = curRock[y][x]
        curRock = newRock

        while True:
            noCollisionIfMove = True
            gasChangeXVal = self.getGasChangeXVal()
            # Will there be collision if we move stuff down one more step?
            for y in curRock:
                for x in curRock[y]:
                    if (self.isThereCollisionForCoord(y-1, x + gasChangeXVal)):
                        noCollisionIfMove = False
                if (noCollisionIfMove == False):
                    break

            
            # if not move it
            if (noCollisionIfMove == True):
                tempRock = defaultdict(lambda: defaultdict(str))
                for y in curRock:
                    for x in curRock[y]:
                        tempRock[y - 1][x + gasChangeXVal] = curRock[y][x]
                curRock = tempRock
                
                # Only count up when we commit to the move
                self.gasCounter += 1
            else:
                break

        # Set in stone (write to rockInChamber)
        self.rockLandsInChamber(curRock)
        return None


    def isThereCollisionForCoord(self, y, x):
        if (y < 0):
            return True
        
        if (x >= 7 or x < 0):
            return True

        if (self.rocksInChamber[y][x] == True):
            return True

        return False
 
    def rockLandsInChamber(self, rock):
        for y in rock:
            for x in rock[y]:
               self.rocksInChamber[y][x] = True
        return None

    def parseInput(self):
        f = open(str(sys.argv[1]), 'r')
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