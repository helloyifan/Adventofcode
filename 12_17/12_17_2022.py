from collections import defaultdict
from aoc_util import shape1, shape2, shape3, shape4, shape5, convertLinesIntoSparceMatList

class Solution():
    
    def __init__(self):
        # The tall, vertical chamber is exactly seven units wide. 
        self.rocksInChamber = defaultdict(lambda: defaultdict(str))  # {y: {x: val}}
        self.maxHeight = 0


    def main(self):
        # self.figureOutPositionBeforeDrop(shape2)
        curRock = convertLinesIntoSparceMatList(shape2)
        self.rockLandsInChamber(curRock)
        self.printRockInChamber()
        return None

    # Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).
    def figureOutPositionBeforeDrop(self, shape):
        print(shape[0][1])
        return None
    
    def rockLandsInChamber(self, rock):
        for y in rock:
            for x in rock[y]:
               self.rocksInChamber[y][x] = True
        return None


    def printRockInChamber(self):
        maxHeight = float('-inf')
        for y in self.rocksInChamber:
            maxHeight = max(maxHeight, y)

        print('+-------+')
        for y in range(maxHeight, -1, -1):
            line = ['.'] * 7

            for x in self.rocksInChamber[y]:
                line[x] = '#'
            
            printLine = ''
            for i in line:
                printLine += i
            
            print('|' + printLine + '|:' + str(y))
        print('+-------+')



sol = Solution()
sol.main()