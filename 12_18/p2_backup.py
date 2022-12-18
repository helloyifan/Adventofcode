from collections import defaultdict

class Solution():
    #positions = {} #{x: {y: {z: True}}}
    positions = None
    inputList = []
    cubeBoundary = 25
    cubeMinBounday = 0
    dp = []
    def main(self):
        self.positions = self.multi_dict(3, bool)
        self.parseInput() # set True to debug

        runningSum = 0
        xKey = self.positions.keys()

        for i in self.inputList:
            freeSides = self.checkHowManyFreeFaces(i['x'], i['y'], i['z'])
            runningSum += freeSides

        print("sidesFree: ", runningSum)
        return None

    def parseInput(self, test=False):
        f = open('input.txt', 'r')
        if (test == True):
            f = open('test_input.txt', 'r')
        
        for line in f:
            xyz = line.strip().split(',')
            self.positions[int(xyz[0])][int(xyz[1])][int(xyz[2])] = True
            self.inputList.append({'x': int(xyz[0]) ,'y':  int(xyz[1]), 'z': int(xyz[2])})
        return None

    def printPositions(self):
        for kx in self.positions:
            for ky in self.positions[kx]:
                for kz in self.positions[kx][ky]:
                    print(kx, ky, kz)

    def checkHowManyFreeFaces(self, x, y, z):
        sidesFree = 0

        if(not self.positions[x + 1][y][z]):
            if (not self.checkAirBubble(x + 1, y, z, [])):
                sidesFree += 1

        if(not self.positions[x - 1][y][z]):
            if (not self.checkAirBubble(x - 1, y, z, [])):
                sidesFree += 1

        if(not self.positions[x][y + 1][z]):
            if (not self.checkAirBubble(x, y + 1, z, [])):
                sidesFree += 1

        if(not self.positions[x][y - 1][z]):
            if (not self.checkAirBubble(x, y - 1, z, [])):
                sidesFree += 1

        if(not self.positions[x][y][z + 1]):
            if (not self.checkAirBubble(x, y, z + 1, [])):
                sidesFree += 1

        if(not self.positions[x][y][z - 1]):
            if (not self.checkAirBubble(x, y, z - 1, [])):
                sidesFree += 1
        return sidesFree

    # an air bubble is if the block has a rock in all 6 directions (this is wrong)
    # we insead need to do dfs on all 6 directions to see if all 6 hits rock
    # if any of dfs hits air then its not rock
    def checkAirBubble(self, x, y, z, history):
        curPos = str(x) + '#' + str(y)+ '#' + str(z)

        if (curPos in self.dp):
            return True

        # Already have gone this way, dont bother
        if (curPos in history):
            return True

        if (x > self.cubeBoundary or x < self.cubeMinBounday or 
            y > self.cubeBoundary or y < self.cubeMinBounday or
            z > self.cubeBoundary or z < self.cubeMinBounday):
            return False
            
        if (self.positions[x][y][z] == True):
            self.dp.append(curPos)        
            return True

        curHistory = history.copy()
        curHistory.append(curPos)

        if (self.checkAirBubble(x + 1, y, z, curHistory) == False):
            return False

        if (self.checkAirBubble(x - 1, y, z, curHistory) == False):
            return False

        if (self.checkAirBubble(x, y + 1, z, curHistory) == False):
            return False

        if (self.checkAirBubble(x, y - 1, z, curHistory) == False):
            return False

        if (self.checkAirBubble(x, y, z + 1, curHistory) == False):
            return False

        if (self.checkAirBubble(x, y, z - 1, curHistory) == False):
            return False

        self.dp.append(curPos)        
        return True


    # Utility function to create dictionary
    # Solen from https://www.geeksforgeeks.org/python-creating-multidimensional-dictionary/
    def multi_dict(self, K, type):
        if K == 1:
            return defaultdict(type)
        else:
            return defaultdict(lambda: self.multi_dict(K-1, type))
    
sol = Solution()
sol.main()

# You guessed 4100, your answer is too high
# You guessed 2494, your answer is too low
# 2508 