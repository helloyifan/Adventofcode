
import sys

class Solution():
    def solve(self):
        input = read_file_get_input_string()

        runningSum = 0
        for line in input:
            ret = self.processLine(line)

            print(ret)
            runningSum += ret

        print(runningSum)
        return runningSum
    
    def processLine(self, line):

        concatString = ''
        prevLargestValIndex = -1  # initalize to be out of scope 

        for i in range(12):
            nthVal = i + 1

            ret = self.findNthsLargestValueInProvidedSpan(line, nthVal, prevLargestValIndex + 1)
            
            concatString = concatString + str(ret['largestVal'])
            prevLargestValIndex = ret['largestValIndex']


        concatNum = int(concatString)
        print(concatNum)
        return concatNum
    
    def findNthsLargestValueInProvidedSpan(self, line, nthVal, startIndex):

        needAtLeastThisManyValuesAfter = 12 - nthVal

        largestVal = 0
        largestValIndex = 0 
        for i in range(startIndex, len(line)-needAtLeastThisManyValuesAfter, 1):

            e = int(line[i])
            if  e > largestVal:
                largestVal = e
                largestValIndex = i
        
        return {'largestVal': largestVal, 'largestValIndex': largestValIndex}

def read_file():
    if len(sys.argv) != 2:
        print("Pass in a file name (and only the filename)")
        sys.exit(1)

    file_name = sys.argv[1]
    file = open(file_name, "r")
    return file

def read_file_get_input_string():
    return read_file().read().strip().split('\n')


sol = Solution()
sol.solve()