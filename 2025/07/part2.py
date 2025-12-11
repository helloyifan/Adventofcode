# Bad coding standsards but worked in 15mins
import sys

class Solution():
    def solve(self):

        input = read_file_get_input_string()
        matrix = convert_input_to_2d_martix(input)
        print2DArray(matrix)

        activatedManufolds = {}
        counterMatrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        

        # Initalize S to be 1
        middleIndex = len(counterMatrix[0]) //2
        print('middleIndex: ', middleIndex)

        counterMatrix[0][middleIndex] = 1
        print2DArray(counterMatrix)


        for ri in range(len(matrix)-1): #-1 because we dont wanna evaluate the last row since theres no row after
            self.helperProcessLineFillNextLine(ri, matrix, activatedManufolds, counterMatrix)
            #print2DArray(matrix)

        print2DArray(counterMatrix)

        
        finRet = 0

        for c in counterMatrix[-1]:
            finRet += c
        print('Sum of last row: ', finRet)
        return finRet
    

    def helperProcessLineFillNextLine(self, rowIndex, matrix, activatedManufolds, counterMatrix):
        for ci in range(len(matrix[rowIndex])):
            if matrix[rowIndex][ci] == 'S' or matrix[rowIndex][ci] == '|':
                
                if matrix[rowIndex+1][ci] == '^':
                    activatedManufolds[(rowIndex+1,ci)] = True
                else:
                    matrix[rowIndex+1][ci] = '|'

                    counterMatrix[rowIndex+1][ci] += counterMatrix[rowIndex][ci]


            elif matrix[rowIndex][ci] == '^': 
                if (rowIndex,ci) in activatedManufolds:

                    if ci-1 >= 0:
                        if matrix[rowIndex+1][ci-1] == '^':
                            activatedManufolds[(rowIndex+1,ci-1)] = True
                        else:
                            matrix[rowIndex+1][ci-1] = '|'
                            counterMatrix[rowIndex+1][ci-1] += counterMatrix[rowIndex-1][ci]

                    if ci+1 < len(matrix[rowIndex]):
                        if matrix[rowIndex+1][ci+1] == '^':
                            activatedManufolds[(rowIndex+1,ci+1)] = True
                        else:
                            matrix[rowIndex+1][ci+1] = '|'

                            counterMatrix[rowIndex+1][ci+1] += counterMatrix[rowIndex-1][ci]

                else:
                    print('dealing with non activated manufold: ', (rowIndex+1,ci))

        return



def print2DArray(list):
    print('==================')
    for l in list:
        print(",".join(str(x) for x in l))

def read_file():
    if len(sys.argv) != 2:
        print("Pass in a file name (and only the filename)")
        sys.exit(1)

    file_name = sys.argv[1]
    file = open(file_name, "r")
    return file

def read_file_get_input_string():
    return read_file().read().strip().split('\n')


def convert_input_to_2d_martix(listOfString):
    matrix = []
    for r in listOfString:
        row = []
        for c in r:
            row.append(c)
        print(row)
        matrix.append(row)
    return matrix

sol = Solution()
sol.solve()