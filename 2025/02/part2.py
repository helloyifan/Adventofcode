
import sys


class Solution():
    cache = {}

    def solve(self):
        input = read_file_get_input_string()
        splitInput = input[0].split(',')
        ## Process input
        processedInput = []
        for i in splitInput:
            l, r = i.split('-')
            processedInput.append({'l': int(l), 'r': int(r)})

        print(processedInput)

        invalidResults = []
        for pair in processedInput:
            l, r = pair['l'], pair['r']

            for i in range(l, r+1, 1):
                ret = self.validId(i) 
                if ret == False:
                    invalidResults.append(i)
        
        print(invalidResults)
        runningSum = 0
        for i in invalidResults:
            runningSum +=i

        print('RunningSum:', runningSum)
        print(self.cache)

    # note Valid ids are ids that DONT fit pattern
    def validId(self, num):
        stringNum = str(num)

        for i in range(1, len(stringNum)//2+1, 1):
            dividedStringList = self.getListOfNDividedString(stringNum, i )
            
            if dividedStringList != None:
                if self.listIsAllTheSame(dividedStringList):
                    return False
    
        return True
    

    def getListOfNDividedString(self, stringNum, splitBy):
        # Incompatiable split
        if len(stringNum) % splitBy != 0:
            #print('Incompatiable split')
            return None

        result = [stringNum[i:i+splitBy] for i in range(0, len(stringNum), splitBy)]
        return result
    

    def listIsAllTheSame(self, list):
        first = list[0]

        for unit in list[1:]:
            if first != unit:
                return False

        return True


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

#print(sol.validId(11))
#print(sol.validId(1188511887))
sol.solve()

# 42395223499