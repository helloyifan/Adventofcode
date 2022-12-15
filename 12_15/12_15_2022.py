import re

class Solution():
    sensorBeacon = []
    minXForBeacon = float('inf')
    maxXForBeacon = float('-inf')

    intervals = []
    mergedIntervals = []

    def main(self):

        i = 'input.txt'
        inputY = 2000000

        # i = 'test_input.txt'
        # inputY = 10


        self.parseInput(i)

        ## Debug
        #print(self.sensorBeacon)
        #print("minXForBeacon", self.minXForBeacon)
        #print("maxXForBeacon", self.maxXForBeacon)
    
        self.checkIfCoordInMatrix(inputY)
        self.mergeIntervals(self.intervals)

        runningSum = 0
        for i, e in enumerate(self.mergedIntervals):
            runningSum += abs(e[0] - e[1])
        
        print("runningSum: ", runningSum)
        return None


    def mergeIntervals(self, intervals):
        # Sort the array on the basis of start values of intervals.
        intervals.sort()
        stack = []
        # insert first interval into stack
        stack.append(intervals[0])
        for i in intervals[1:]:
            # Check for overlapping interval,
            # if interval overlap
            if stack[-1][0] <= i[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)
    
        for i in range(len(stack)):
            self.mergedIntervals.append(stack[i])
        return None

    def parseInput(self, i):
        f = open(i, 'r')

        for line in f:
            section = line.split(':')
            sensor, beacon = section[0], section[1]

            sensorCoord = re.findall('-?\d*\.{0,1}\d+', sensor)
            beaconCoord = re.findall('-?\d*\.{0,1}\d+', beacon)
            
            sensorCoordDict = {'x': int(sensorCoord[0]), 'y': int(sensorCoord[1])}
            beaconCoordDict = {'x': int(beaconCoord[0]), 'y': int(beaconCoord[1])}
            
            self.minXForBeacon = min(self.minXForBeacon, beaconCoordDict['x'])
            self.maxXForBeacon = max(self.maxXForBeacon, beaconCoordDict['x'])

            self.sensorBeacon.append({"sensor": sensorCoordDict, "beacon": beaconCoordDict})
        return None

    # Bad name
    def checkIfCoordInMatrix(self, y):
        for i, e in enumerate(self.sensorBeacon):
            sensor,beacon = e['sensor'], e['beacon']
            manhattenVal = self.calculateSensorToBeaconDistance(i)
            coverage = self.calculateRowCoverage(manhattenVal, y, sensor)

        return None
    
    def calculateSensorToBeaconDistance(self, i):
        sensor, beacon = self.sensorBeacon[i]['sensor'], self.sensorBeacon[i]['beacon'] 
        xDiff = abs(sensor['x'] - beacon['x'])
        yDiff = abs(sensor['y'] - beacon['y'])
        return xDiff + yDiff

    def calculateRowCoverage(self, manhattenVal, coordY, sensor):
        spanVal = manhattenVal -  abs(coordY - sensor['y'])
        if (spanVal < 0):
            return None

        #Its inclusive
        self.intervals.append([sensor['x'] - spanVal, sensor['x'] + spanVal])
        return None

    ## Maybe all of the above is a bad idea

    ## Maybe we just want to check if something is within the manhatten distance of somethign else

sol = Solution()
sol.main()

#You guessed 5181556 is too high

