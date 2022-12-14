from collections import defaultdict

class Solution():
    sparceMatrix = defaultdict(lambda: defaultdict(str))  # {x: {y: val}}
    def main(self):
        self.parseInputBuildMatrix()
        return None
    
    def parseInputBuildMatrix(self):
        f = open('sample_input.txt', 'r')

        for line in f:
            oldCoord = None # Reset these for every new line of inptu
            newCoord = None

            line = line.strip()
            steps = line.split('->')
        
            for step in steps:
                step = step.split(',')
                newCoord = {'x':int(step[0]), 'y': int(step[1])}
                
                if (oldCoord != None):
                    self.fillMatrix(oldCoord, newCoord)    
                
                oldCoord = newCoord

        #self.simplePrintSparceMatrix()
        self.printVisualSparceMatrix(494, 503+1, 0, 9+1)
        return None

    # After the first point of each path, each point indicates the end of a straight horizontal or vertical
    def fillMatrix(self, oldCoord, newCoord):
        # Fill Vertically
        if (oldCoord['x'] == newCoord['x'] and  oldCoord['y'] != newCoord['y']):
            x = oldCoord['x']
            oldY, newY = oldCoord['y'], newCoord['y']
            step = 1 if oldCoord['y'] < newCoord['y'] else -1
            newYOffSet = newY + step #Because range end_val us exclusive, this is to offset that

            for y in range(oldY, newYOffSet, step):
                self.sparceMatrix[x][y] = '#' # not sure if there is something better we can fill with

        # Fill Horizontally
        elif (oldCoord['x'] != newCoord['x'] and  oldCoord['y'] == newCoord['y']):
            y = oldCoord['y']
            oldX, newX = oldCoord['x'], newCoord['x']
            step = 1 if oldCoord['x'] < newCoord['x'] else -1
            newXOffSet = newX + step

            for x in range(oldX, newXOffSet, step):
                self.sparceMatrix[x][y] = '#' 


        elif (oldCoord['x'] == newCoord['x'] and  oldCoord['y'] == newCoord['y']):
            raise Exception("Fucking try to call fillMatrix with same oldCoord and oldCoord")

        elif (oldCoord['x'] != newCoord['x'] and  oldCoord['y'] != newCoord['y']):
            raise Exception("Both the X and Y don't line up. Is it suppose to be diagonal?")

    def simplePrintSparceMatrix(self):
        for xk, xv in self.sparceMatrix.items():
            for yk, yv in xv.items():
                print("x:", xk, "y:", yk, 'v:', yv)
        return None


    def printVisualSparceMatrix(self, startX, endX, startY, endY):
        for y in range(startY, endY):
            outPutLine = ''
            for x in range(startX, endX):
                char = '# ' if (self.sparceMatrix[x][y] == '#') else '. '
                outPutLine += char
            print(outPutLine)

sol = Solution()
sol.main()


# sand always falls down one step if possible

# If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. 

# If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right.
