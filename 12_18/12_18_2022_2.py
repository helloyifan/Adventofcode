from collections import defaultdict

class Solution():
    #positions = {} #{x: {y: {z: True}}}
    positions = None
    inputList = []
    cubeBoundary = 22 
    cubeMinBoundary = 0
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
            if (not self.checkAirBubble(x + 1, y, z)):
                sidesFree += 1

        if(not self.positions[x - 1][y][z]):
            if (not self.checkAirBubble(x - 1, y, z)):
                sidesFree += 1

        if(not self.positions[x][y + 1][z]):
            if (not self.checkAirBubble(x, y + 1, z)):
                sidesFree += 1

        if(not self.positions[x][y - 1][z]):
            if (not self.checkAirBubble(x, y - 1, z)):
                sidesFree += 1

        if(not self.positions[x][y][z + 1]):
            if (not self.checkAirBubble(x, y, z + 1)):
                sidesFree += 1

        if(not self.positions[x][y][z - 1]):
            if (not self.checkAirBubble(x, y, z - 1)):
                sidesFree += 1
        return sidesFree

    # an air bubble is if the block has a rock in all 6 directions (this is wrong)
    # we insead need to do dfs on all 6 directions to see if all 6 hits rock
    # if any of dfs hits air then its not rock
    def checkAirBubble(self, x, y, z):
        curPos = {'x': x, 'y': y, 'z': z}
        
        if (curPos in self.dp):
            return True

        q = []
        history = []

        q.append(curPos)

        while len(q) > 0:
            pos = q.pop(0)

            if (pos in history):
                continue


            history.append(pos)

            if (pos['x'] < self.cubeMinBoundary or  pos['x'] > self.cubeBoundary):
                return False
            if (pos['y'] < self.cubeMinBoundary or  pos['y'] > self.cubeBoundary):
                return False
            if (pos['z'] < self.cubeMinBoundary or  pos['z'] > self.cubeBoundary):
                return False
            
            if (not self.positions[pos['x']][pos['y']][pos['z']]):
                q.append( {'x': pos['x'] + 1, 'y': pos['y'], 'z':pos['z']})
                q.append( {'x': pos['x'] - 1, 'y': pos['y'], 'z':pos['z']})
                q.append( {'x': pos['x'], 'y': pos['y'] + 1, 'z':pos['z']})
                q.append( {'x': pos['x'], 'y': pos['y'] - 1, 'z':pos['z']})
                q.append( {'x': pos['x'], 'y': pos['y'], 'z':pos['z'] + 1})
                q.append( {'x': pos['x'], 'y': pos['y'], 'z':pos['z'] - 1})
        
        # Return true if q is empty

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