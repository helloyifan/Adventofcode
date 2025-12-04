
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

        largestVal = 0
        largestValIndex = 0 
        for i in range(len(line)-1):
            e = int(line[i])
            if  e > largestVal:
                largestVal = e
                largestValIndex = i

        secondLargestVal = 0
        secondLargestValIndex = 0

        for i in range(largestValIndex+1, len(line), 1):
            e = int(line[i])
            if  e > secondLargestVal:
                secondLargestVal = e
                secondLargestValIndex = i

        concatString = str(largestVal) + str(secondLargestVal)
        concatNum = int(concatString)
        return concatNum
    

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