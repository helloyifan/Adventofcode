import sys

class Solution():
    sparceMatrix = {}
    directionInstructions = '?'
    def main(self):
        print("hello world")
        self.parseInput()

        return 0
    def parseInput(self):
        f = open(str(sys.argv[1]), 'r')
        numLines = sum(1 for line in f)
        f.seek(0) # Back to top of file
        print("numLines: ", numLines)

        puzzleMapFileEnd = numLines -1
        print("puzzleMapFileEnd: ", puzzleMapFileEnd)
        for rowNum in range(0, puzzleMapFileEnd):
            print(rowNum)
            row = f.readline()
            print(row)
            for colNum in range(0, len(row)):
                col = row[colNum]
                if (col != ' ' and col != '\n'):
                    self.sparceMatrix[(rowNum, colNum)] = col

        self.directionInstructions = f.read()
        print(self.sparceMatrix)
        print("nice it works:" , self.directionInstructions)

    def drawSparceMatrix():
        return None
sol = Solution()
sol.main()