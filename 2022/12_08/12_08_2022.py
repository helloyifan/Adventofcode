class Solution():
    gird = None
    def main(self):
        self.grid = self.readInputCreateGrid()
        self.printGrid()

        ret = 0
        for rowIndex, gridRow in enumerate(self.grid):
            for colIndex, element in enumerate(gridRow):
                pos = {'row': rowIndex, 'col': colIndex}
                if (self.checkEdge(pos) or 
                    self.checkLeft(pos) or
                    self.checkFromRight(pos) or
                    self.checkFromTop(pos) or
                    self.checkFromBottom(pos)
                ):
                    ret += 1

        ## Final Ret
        print("Ret: ", ret)
        return None

    def checkEdge(self, pos, debug=False):
        if (pos['row'] == 0 or 
            pos['row'] == len(self.grid) -1 or
            pos['col'] == 0 or
            pos['col'] == len(self.grid[0]) -1        
        ):
            # Print pos if debug mode is on
            if (debug):
                print(pos)
            return True
        return False

    def checkLeft(self, pos, debug=False):
        posVal = self.grid[pos['row']][pos['col']]
        for itratingCol in range(0, pos['col']):
            if posVal <= self.grid[pos['row']][itratingCol]:
                return False
        # Print pos if debug mode is on
        if (debug):
            print(pos)
        return True

    def checkFromRight(self, pos, debug=False):
        posVal = self.grid[pos['row']][pos['col']]
        # Remember first arg in range in inclusive
        for itratingCol in range(pos['col'] + 1, len(self.grid[0])):
            if posVal <= self.grid[pos['row']][itratingCol]:
                return False
        # Print pos if debug mode is on
        if (debug):
            print(pos)
        return True

    def checkFromTop(self, pos, debug=False):
        posVal = self.grid[pos['row']][pos['col']]
        for itratingRow in range(0, pos['row']):
            if posVal <= self.grid[itratingRow][pos['col']]:
                return False
        # Print pos if debug mode is on
        if (debug):
            print(pos)
        return True

    def checkFromBottom(self, pos, debug=False):
        posVal = self.grid[pos['row']][pos['col']]
        for itratingRow in range(pos['row'] + 1, len(self.grid)):
            if posVal <= self.grid[itratingRow][pos['col']]:
                return False
        # Print pos if debug mode is on
        if (debug):
            print(pos)
        return True

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