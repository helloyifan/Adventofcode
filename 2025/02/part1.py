
import sys


class Solution():
    def solve(self):

        self.cache = {}

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
                ret = None
                # Sick caching layer
                if i in self.cache:
                    print('cache hit')
                    ret = self.cache[i]
                else:
                    ret = self.validId(i) 
                    self.cache[i] = ret

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
        stringNumber = str(num)

        if len(stringNumber) % 2 ==1:
            return True

        middle = len(stringNumber)//2
        for i in range(0, middle, 1):
            l = stringNumber[i]
            r = stringNumber[middle + i]

            # Valid bcuz theres a mismatch
            if l != r:
                return True

        return False    

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

sol.solve()

# 42395223499