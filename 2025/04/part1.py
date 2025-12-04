
import sys

class Solution():
    def solve(self):
        self.ret = 0
        self.matrix = read_file_get_input_string()
        self.maxR = len(self.matrix) -1
        self.maxC = len(self.matrix[0]) -1

        # twoDimensionPrinter(input)
        self.visited = {}
        self.dfs(0,0)
        
        print('FinRet:' , self.ret)

        return
    
    def dfs(self,  row, col):
        if (row, col) in self.visited:
            return

        if row < 0 or row > self.maxR:
            return
        
        if col < 0 or col > self.maxC:
            return

        #print(row, col)
        self.visited[(row, col)] = True

        if self.matrix[row][col] =='@':
            if self.check8Around(row, col) < 4:
                print(row, col)
                self.ret += 1

        self.dfs(row, col +1)
        self.dfs(row +1, col)

        return

    def check8Around(self, row, col):
        counter =0 

        dirs = [ (-1, -1), (-1, 0), (-1, 1), (1,-1),(1,0),(1,1), (0, 1), (0, -1)]

        for d in dirs:
            newRow = row + d[0]
            newCol = col + d[1]
            
            if 0 <= newRow and  newRow <= self.maxR:
                if 0 <= newCol and  newCol <= self.maxC:
                    if self.matrix[newRow][newCol] == '@':
                        counter +=1

        return counter

            


def read_file():
    if len(sys.argv) != 2:
        print("Pass in a file name (and only the filename)")
        sys.exit(1)

    file_name = sys.argv[1]
    file = open(file_name, "r")
    return file

def read_file_get_input_string():
    return read_file().read().strip().split('\n')


def twoDimensionPrinter(matrix):
    for i in matrix:
        print(i)


sol = Solution()

sol.solve()
