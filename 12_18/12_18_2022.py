from collections import defaultdict

class Solution():
    #positions = {} #{x: {y: {z: True}}}
    positions = None
    inputList = []

    def main(self):
        self.positions = self.multi_dict(3, bool)
        self.parseInput()

        runningSum = 0
        xKey = self.positions.keys()

        for i in self.inputList:
            freeSides = self.checkHowManyFreeFaces(i['x'], i['y'], i['z'])
            runningSum += freeSides
            print(i, freeSides)

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
            sidesFree += 1

        if(not self.positions[x - 1][y][z]):
            sidesFree += 1

        if(not self.positions[x][y + 1][z]):
            sidesFree += 1

        if(not self.positions[x][y - 1][z]):
            sidesFree += 1

        if(not self.positions[x][y][z + 1]):
            sidesFree += 1

        if(not self.positions[x][y][z - 1]):
            sidesFree += 1

        return sidesFree

    # Utility function to create dictionary
    # Solen from https://www.geeksforgeeks.org/python-creating-multidimensional-dictionary/
    def multi_dict(self, K, type):
        if K == 1:
            return defaultdict(type)
        else:
            return defaultdict(lambda: self.multi_dict(K-1, type))
    
sol = Solution()
sol.main()

# sidesFree:  4364