import re
import copy

class Solution():
    tunnelGraph = {}
    flowRate = {}
    dist = []
    vertexNumRef = []

    def main(self):
        self.parseInput() # Set True to run test input 
        self.floydWarshall()
        ret = self.dfs('AA', 26, [] , [])
        return None

    def dfs(self, curLoc, time, turnedOn, turnedOnAndWhen):

        if (time == 0 ):
            return 0
        
        maxScore = 0
        indexRow = self.vertexNumRef.index(curLoc)
        turnedOn.append(curLoc) #need to think about this, is this the right place
        turnedOnAndWhen.append([curLoc, time]) #need to think about this, is this the right place
        print(turnedOnAndWhen)
        for indexCol, element in enumerate(self.vertexNumRef):
            # No pressure
            if (self.flowRate[element] == 0 ):
                continue
            # Already been there
            if (element in turnedOn):
                continue
            # Already there
            if (curLoc == element):
                continue
            updatedTime = time - self.dist[indexRow][indexCol] - 1
            # Not enough time
            if (updatedTime < 0):
                continue

            curScore = self.dfs(element, updatedTime, turnedOn.copy(), turnedOnAndWhen.copy())
            maxScore = max(maxScore, curScore)
        

        
        return maxScore + time * self.flowRate[curLoc]


    def parseInput(self, test=False):
        f = open('input.txt', 'r')
        if (test):
            f = open('test_input.txt', 'r')
        
        for line in f:
            splitLine = line.split(';')
            curValve = re.findall('[A-Z][A-Z]', splitLine[0])[0]
            curFlowRate = re.findall('\d+', splitLine[0])[0]
            tunnelDest = re.findall('[A-Z][A-Z]', splitLine[1])

            self.tunnelGraph[curValve] = tunnelDest
            self.flowRate[curValve] = int(curFlowRate)
            self.vertexNumRef.append(curValve)

        return None

    def floydWarshall(self):
        for i, e in enumerate(self.vertexNumRef):
            row = []
            for j, ej in enumerate(self.vertexNumRef):
                row.append(float('inf'))
            self.dist.append(row)

        for i, e in enumerate(self.vertexNumRef):
            self.dist[i][i] = 0

        for curValve in self.tunnelGraph:
            row = self.vertexNumRef.index(curValve)
            for valve in self.tunnelGraph[curValve]:
                col = self.vertexNumRef.index(valve)
                self.dist[row][col] = 1

        for k in range(len(self.vertexNumRef)):
            for i in range(len(self.vertexNumRef)):
                for j in range(len(self.vertexNumRef)):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k] + self.dist[k][j])


        # for row in self.dist:
        #     for col in row:
        #         print(col, end=' ')
        #     print()

sol = Solution()
sol.main()  

