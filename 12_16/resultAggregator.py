import re

class ResultAggregator():
    results = []
    flowRate = {}
    vertexNumRef = []

    def main(self):
        self.parseInput()
        self.parseResultInput()
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
            #print(totalVal)
            #maxVal = max(maxVal, totalVal)

            if (totalVal > maxVal):
                maxVal = totalVal
                maxRetLine = retline.copy()
        
        print('maxVal: ', maxVal)
        print('maxRetLine: ', maxRetLine)
        return None
    
    def calculateTotal(self, retline):
        runningSum = 0
        for ret in retline:
            runningSum += self.flowRate[ret[0]] * ret[1]
        return runningSum

ra  = ResultAggregator()
ra.main()