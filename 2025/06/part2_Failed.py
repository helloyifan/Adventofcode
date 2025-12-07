# Solution wont work because 
# " 45" is different from "45 "
# 

import sys

class Solution():
    def solve(self):
        rawInput = read_file_get_input_string()
        processedInput = self.preProcess1SplitInput(rawInput)

        signs = processedInput[-1]
        processedInput2 = self.preProcess2DoubleSplitInput(processedInput)
        processedInput3 = self.preProcess3CollectValsInSameCol(processedInput2)

        readyToUseMatrix = self.preProcess4BuildNumberMatrix(processedInput3)

        print('readyToUseMatrix: ', readyToUseMatrix)        


        # Build Ret:

        runningSum = 0
        
        # for rowIndex, rowVal in enumerate(processedInput3):
        #     print(rowVal)
        #     # Find longest array


        # print("runningSum: ", runningSum)
        return
    
    def preProcess4BuildNumberMatrix(self ,processedInput3):

        readyToUseMatrix = []
        for index, input in enumerate(processedInput3):
            readyToUseRow = self.preProcess4HelperBuildNumberForRow(input)
            readyToUseMatrix.append(readyToUseRow)
        return readyToUseMatrix
            

    def preProcess4HelperBuildNumberForRow(self, row):

        readyToUseRow = []
        # Find Max Len of Row

        maxRowLen = 0
        for numberInListForm in row:
            maxRowLen = max(maxRowLen, len(numberInListForm))
        

        for i in range(maxRowLen):
            curNumberAsString = ''
            for number in row:
                if len(number) > i:
                    lastDigitIndex = len(number)-1 -i 
                    curNumberAsString += str(number[lastDigitIndex])
            
            #print(curNumberAsString)
            readyToUseRow.append(int(curNumberAsString))

        return readyToUseRow



    Collapse Navigation
    
    
    
    # Collect same values that exists in same col into same row instead
    def preProcess3CollectValsInSameCol(self, input):
        retVal = []

        for c in range(len(input[0])):
            newRow = []
            for r in range(len(input)):
                newRow.append(input[r][c]) #not sure if we need to do deep copy
            retVal.append(newRow)
        return retVal



    def preProcess2DoubleSplitInput(self, input):
        retVal = []
        for r in range(len(input)-1):
            rowVal = []
            for c in range(len(input[0])):
                colVal = [int(e) for i, e in enumerate(input[r][c])]
                rowVal.append(colVal)
            retVal.append(rowVal)

        return  retVal

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