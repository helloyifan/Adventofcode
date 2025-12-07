# Bad coding standsards but worked in 15mins
import sys

class Solution():
    def solve(self):
        rawInput = read_file_get_input_string()
        processedInput = self.preProcess1SplitInput(rawInput)

        # Build Ret:
        cols = len(processedInput[0])
        rows = len(processedInput)

        runningSum = 0
        
        for i in range(cols):
            curTotal = None
            curMode = '*'
            if processedInput[-1][i] == '+': # -1 because its the last
                curMode = '+'

            for j in range(rows-1): # Because last row is the sign

                if curTotal ==None:
                    curTotal = int(processedInput[j][i])
                else:
                    if curMode == '*':
                        curTotal *=  int(processedInput[j][i])
                    elif curMode == '+':
                        curTotal +=  int(processedInput[j][i])
                    else:
                        raise Exception("You fucked up")


            runningSum += curTotal

        print("runningSum: ", runningSum)
        return

    def preProcess1SplitInput(self, input):
        retVal = []
        for i in input:
            retVal.append(i.split())
        return retVal
        

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