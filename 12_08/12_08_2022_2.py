import copy

class Solution():
    gird = None
    def main(self):
        self.grid = self.readInputCreateGrid()
        self.printGrid()

        maxVal = 0 
        maxPos = None
        for rowIndex, gridRow in enumerate(self.grid):
            for colIndex, element in enumerate(gridRow):
                pos = {'row': rowIndex, 'col': colIndex}
                
                left = self.checkLeft(pos)
                right = self.checkFromRight(pos)
                top = self.checkFromTop(pos)
                bottom = self.checkFromBottom(pos)
                
                productVal = left * right * top * bottom
                # debug bullshit
                # if (pos['row']  == 3 and pos['col'] == 2):
                #     print(pos)
                #     print("left:", left, "right:", right, "top:", top, "bottom:", bottom)

            
                if (productVal > maxVal):
                    maxVal = productVal
                    maxPos = copy.deepcopy(pos)

        ## Final maxVal
        print("maxVal: ", maxVal)
        print("maxPos: ", maxPos)
        
        return None

    # def checkEdge(self, pos, debug=False):
    #     if (pos['row'] == 0 or 
    #         pos['row'] == len(self.grid) -1 or
    #         pos['col'] == 0 or
    #         pos['col'] == len(self.grid[0]) -1        
    #     ):
    #         # Print pos if debug mode is on
    #         if (debug):
    #             print(pos)
    #         return True
    #     return False

    def checkLeft(self, pos, debug=False):
        rollingSum = 0
        posVal = self.grid[pos['row']][pos['col']]
        for itratingCol in range(pos['col'] -1, -1, -1 ):
            if posVal <= self.grid[pos['row']][itratingCol]:
                return rollingSum + 1
            else:
                rollingSum += 1

        return rollingSum

    def checkFromRight(self, pos, debug=False):
        rollingSum = 0
        posVal = self.grid[pos['row']][pos['col']]
        # Remember first arg in range in inclusive
        for itratingCol in range(pos['col'] + 1, len(self.grid[0])):
            if posVal <= self.grid[pos['row']][itratingCol]:
                return rollingSum + 1
            else:
                rollingSum += 1

        return rollingSum

    def checkFromTop(self, pos, debug=False):
        rollingSum = 0
        posVal = self.grid[pos['row']][pos['col']]
        for itratingRow in range(pos['row'] -1 , -1 , -1 ):
            if posVal <= self.grid[itratingRow][pos['col']]:
                return rollingSum + 1
            else:
                rollingSum += 1
        return rollingSum

    def checkFromBottom(self, pos, debug=False):
        rollingSum = 0
        posVal = self.grid[pos['row']][pos['col']]
        for itratingRow in range(pos['row'] + 1, len(self.grid)):
            if posVal <= self.grid[itratingRow][pos['col']]:
                return rollingSum + 1
            else:
                rollingSum += 1
        return rollingSum

    def readInputCreateGrid(self):
        f = open("input.txt", "r")
        grid = []
        for row in f:
            gridRow = []
            for i, col in enumerate(row):
                if (not '\n' in col): # deal with the pesky \n
                    gridRow.append(int(col))
            grid.append(gridRow)
        return grid

    def printGrid(self):
        for gridRow in self.grid:
            print(gridRow)

sol = Solution()
sol.main()