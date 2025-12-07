# Solution wont work because 
# " 45" is different from "45 "
# 

import sys

class Solution():
    def solve(self):
        rawInput = read_file_get_input_string()

        signedRowFromInput = rawInput[-1]
        numberInput = rawInput[:-1]
        sizesOfEachSlot = self.figureOutGaps(signedRowFromInput)
        
        print(sizesOfEachSlot)
        print(numberInput)

        brokenDownMatrix = self.readInMatrixBySlow(sizesOfEachSlot, numberInput)
        self.datastructurePrinter(brokenDownMatrix)


        rollingSum = 0
        # Delete the below im confused


        numbersInMatrix = []
        for c in range(len(brokenDownMatrix[0])):
            print('wtf')
            # FinRet logic
            finalSumOrProduct = None
            currentSign = '*'
            signsInArray = signedRowFromInput.replace(" ", "")

            print('signsInArray[c]: ', signsInArray[c])

            if (signsInArray[c]) == '+':
                print("hey")
                currentSign = '+'

            # Lengths of words
            lengthOfNum = len(brokenDownMatrix[0][c])
            numbersInCol = []

            for numberIndex in range(lengthOfNum-1, -1, -1):
                curNum = ''
                for r in range(len(brokenDownMatrix)):
                    # Process list of letters
                    curNum = curNum + brokenDownMatrix[r][c][numberIndex]
                
                numbersInCol.append(curNum)

                intCurNum = int(curNum)

                # FinRet logic
                if finalSumOrProduct == None:
                    finalSumOrProduct = intCurNum
                else:
                    if currentSign == '*':
                        finalSumOrProduct *= intCurNum
                    elif currentSign == '+':
                        finalSumOrProduct += intCurNum
                    else:
                        raise Exception("you fucked up idiot")

      
        
            numbersInMatrix.append(numbersInCol)
            # FinRet logic
            print('finalSumOrProduct: ', finalSumOrProduct)
            rollingSum += finalSumOrProduct

        print(numbersInMatrix)
        print(rollingSum)
        
        return

    def readInMatrixBySlow(self, sizesOfEachSlot, numberInput):
        brokenDownMatrix = []
        for rawRow in numberInput:
            brokenDownRow = []
            startPoint = 0 
            for curSize in sizesOfEachSlot:
                currentSegment = rawRow[startPoint:startPoint+curSize]

                #Updating startinPoint to also account for the ' ' gap
                startPoint += curSize + 1

                brokenDownRow.append(list(currentSegment))

            brokenDownMatrix.append(brokenDownRow)

        return brokenDownMatrix


    def figureOutGaps(self, signedRow):
        print(signedRow)
        sizes = []
        curCounter = 0 
        for i, c in enumerate(signedRow):
            if c != ' ':
                if i > 0:
                    sizes.append(curCounter)
                curCounter = 0
            else:
                curCounter += 1
        sizes.append(curCounter + 1) # need to offset the last item by 1

        return sizes

    def datastructurePrinter(self, matrix):
        print('-------')

        for r in matrix:
            currentLine = []
            for c in r:
                currentLine.append(''.join(c))
            print(currentLine)
                
        print('-------')
            

def read_file():
    if len(sys.argv) != 2:
        print("Pass in a file name (and only the filename)")
        sys.exit(1)

    file_name = sys.argv[1]
    file = open(file_name, "r")
    return file

def read_file_get_input_string():
    return read_file().read().split('\n') # removed .strip() that we normally have



sol = Solution()
sol.solve()