import re

class ResultAggregator():
    results = []
    flowRate = {}
    vertexNumRef = []

    def main(self):
        self.parseInput()
        self.parseResultInput()

        self.results.sort(key=lambda a: a[0], reverse=True)
        #self.printSortedListOfTuple()
        self.findTwoNonOverLappingEntry(len(self.results))
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

            self.flowRate[curValve] = int(curFlowRate)
            self.vertexNumRef.append(curValve)

    def parseResultInput(self):
        f = open('output.txt', 'r')
        maxVal = 0 # it should be 1595
        maxRetLine = None
        for line in f:
            retline = eval(line)
            totalVal = self.calculateTotal(retline)

            # #print(totalVal)
            # #maxVal = max(maxVal, totalVal)
            # if (totalVal > maxVal):
            #     maxVal = totalVal
            #     maxRetLine = retline.copy()

            listOfValves = []
            for ret in retline:
                listOfValves.append(ret[0])

            self.results.append((totalVal, listOfValves))
        return None
    
    def calculateTotal(self, retline):
        runningSum = 0
        for ret in retline:
            runningSum += self.flowRate[ret[0]] * ret[1]
        return runningSum

    def printSortedListOfTuple(self):
        for i in self.results:
            print(i)

    def findTwoNonOverLappingEntry(self, coverage):
        maxFinResult = 0
        for i in range(coverage):
            line = self.results[i]
            for j in range(i + 1, coverage):
                curLine = self.results[j]
                if (not self.checkIfTwoSetsOfValveHaveDupliate(line[1], curLine[1])):
                    #print('finRet:', line[0] + curLine[0], line, curLine)
                    maxFinResult = max(maxFinResult, line[0] + curLine[0])
        print(maxFinResult)
        return None

    def checkIfTwoSetsOfValveHaveDupliate(self, valves1, valves2):
        for v in valves1:
            if (v != 'AA' and v in valves2):
                return True
        return False


ra  = ResultAggregator()
ra.main()


# to get the answer for 12_16 part 2, run 12_16_2022.2py which will create output.txt
# use output.txt and input.txt as input to this (i know)

