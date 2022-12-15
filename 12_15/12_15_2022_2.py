import re

class Solution():
    sensorBeacon = []
    xValRange = None
    yValRange = None


    def main(self):

        i = 'input.txt'
        inputY = 2000000
        self.xValRange = [0, 4000000]
        self.yValRange = [0, 4000000]

        # i = 'test_input.txt'
        # inputY = 10
        # self.xValRange = [0, 20]
        # self.yValRange = [0, 20]

        self.parseInput(i)


        for y in range(self.yValRange[0], self.yValRange[1] + 1):
            intervals = self.checkIfCoordInMatrix(y)
            mergedIntervals = self.mergeIntervals(intervals)

            if (len(mergedIntervals) > 1):
                print(y, mergedIntervals)

        return None

    def mergeIntervals(self, intervals):
        # Sort the array on the basis of start values of intervals.
        intervals.sort()
        stack = []
        mergedIntervals = []
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
            mergedIntervals.append(stack[i])
        return mergedIntervals

    def parseInput(self, i):
        f = open(i, 'r')

        for line in f:
            section = line.split(':')
            sensor, beacon = section[0], section[1]

            sensorCoord = re.findall('-?\d*\.{0,1}\d+', sensor)
            beaconCoord = re.findall('-?\d*\.{0,1}\d+', beacon)
            
            sensorCoordDict = {'x': int(sensorCoord[0]), 'y': int(sensorCoord[1])}
            beaconCoordDict = {'x': int(beaconCoord[0]), 'y': int(beaconCoord[1])}

            self.sensorBeacon.append({"sensor": sensorCoordDict, "beacon": beaconCoordDict})
        return None

    # Bad name
    def checkIfCoordInMatrix(self, y):
        intervals = []
        for i, e in enumerate(self.sensorBeacon):
            sensor,beacon = e['sensor'], e['beacon']
            manhattenVal = self.calculateSensorToBeaconDistance(i)
            interval = self.calculateRowCoverage(manhattenVal, y, sensor)
            if (interval): #make sure its not none
                intervals.append(interval)

        return intervals
    
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
        return [sensor['x'] - spanVal, sensor['x'] + spanVal]

    ## Maybe all of the above is a bad idea

    ## Maybe we just want to check if something is within the manhatten distance of somethign else

sol = Solution()
sol.main()

# y = 3219131 x = [[-1006499, 3204399], [3204401, 4255799]]
# y = 3219131 , x = 320440

'''
>>> 4000000 * 3204400 
12817600000000
>>> 12817600000000 + 3219131
12817603219131
'''