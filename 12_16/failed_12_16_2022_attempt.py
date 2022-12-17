import re
import copy


class Solution():
    tunnelGraph = {}
    flowRate = {}

    def main(self):
        self.parseInput(True) # Set true to run test input 
        print(self.tunnelGraph)
        print(self.flowRate)

        maxPressureFromTunnelList = self.dfs('AA', 30)
        print("maxPressureFromTunnelList: ", maxPressureFromTunnelList)
        return None

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
        return None

    # Return contract: {valve: timeItGotOpened}
    def dfs(self, curValve, timeRemain):
        if (timeRemain <= 0):
            return {}        
        # For the move
        timeRemain -= 1
        
        maxScore = 0
        maxScoreTrackingObj = {}

        # If we decided to turn on this valve
        if (self.flowRate[curValve] > 0):
            for valve in self.tunnelGraph[curValve]:
                # timeRemain -= 1
                scoreTrackingObj = self.dfs(valve, timeRemain)

                # We only consider possibilities with current valve if its not in the result
                if (not curValve in scoreTrackingObj):
                    timeRemain -= 1 #not sure if it goes here or above
                    scoreTrackingObj[curValve] = timeRemain

                    curScore = self.calcScoreFromTrackingObj(scoreTrackingObj)            
                    if (curScore > maxScore):
                        maxScore = curScore
                        maxScoreTrackingObj = scoreTrackingObj.copy() #hopefully this copy doesnt fuck shit up
                

        # for valve in self.tunnelGraph[curValve]:
        #     scoreTrackingObj = self.dfs(valve, timeRemain)
        #     curScore = self.calcScoreFromTrackingObj(scoreTrackingObj)            
        #     if (curScore > maxScore):
        #         maxScore = curScore
        #         maxScoreTrackingObj = scoreTrackingObj.copy() 
        return maxScoreTrackingObj            
    
    # Dict format
    #  {valve: timeItGotOpened}
    def calcScoreFromTrackingObj(self, scoreTrackingObj):
        runningSumScore = 0
        for key in scoreTrackingObj:
            runningSumScore += scoreTrackingObj[key] * self.flowRate[key]        
        return runningSumScore


sol = Solution()

# sol.main()  


#Debug calcScoreFromTrackingObj
testScoreObject = {'CC': 26, 'DD': 27, 'AA': 28}
sol.parseInput(True)
print(sol.calcScoreFromTrackingObj(testScoreObject))


