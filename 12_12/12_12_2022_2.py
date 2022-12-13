from datetime import datetime

class Solution():
    def main(self):
        self.readInputToMatrix()
        #self.navigateMatrix(0,0)
        self.navigateMatrix(20,0)
        return None

    def navigateMatrix(self, startRow, startCol):
        # if (self.matrix[row, col] == 'S'):
        #     # Starting on S is kinda weird but its all good 
        
        self.visited = []

        ## Init the BFS stuff
        startingPos = {'row': startRow, 'col': startCol, 'count': 0, 'startingStep': 0, 'aCord': None}
        #print("debug:" , self.matrix[startRow][startCol])
        q = [startingPos]  #initalize it with starting pos
        
        while (len(q) > 0):
            # C (current) is the head of q
            c = q.pop(0)

            # make key for visited list
            vKey = str(c['row']) + '#' + str(c['col'])

            if (vKey in self.visited):
                continue

            self.visited.append(vKey)
            preChar = self.matrix[c['row']][c['col']]

            if (preChar == 'E'):
                # We are done
                print("we are done")
                print(c)
                break

            if (self.canWeVisit(c['row'] + 1, c['col'], preChar)):
                startingStep = c['startingStep'] + 1
                ac = c['aCord']
                if (self.matrix[c['row'] + 1][c['col']] == 'a'): 
                    startingStep = 0
                    ac = { 'row': c['row'] + 1, 'col': c['col']}
                
                tU = { 'row': c['row'] + 1, 'col': c['col'], 'count': c['count']+1, 'startingStep': startingStep, 'aCord': ac}
                q.append(tU)

            if (self.canWeVisit(c['row'] - 1, c['col'], preChar)):
                startingStep = c['startingStep'] + 1
                ac = c['aCord']
                if (self.matrix[c['row'] - 1][c['col']] == 'a'): 
                    startingStep = 0
                    ac = { 'row': c['row'] - 1, 'col': c['col']}

                tD = { 'row': c['row'] - 1, 'col':c['col'], 'count': c['count']+1, 'startingStep': startingStep, 'aCord': ac}
                q.append(tD)

            if (self.canWeVisit(c['row'], c['col'] + 1, preChar)):
                startingStep = c['startingStep'] + 1
                ac = c['aCord']
                if (self.matrix[c['row']][c['col']+1] == 'a'): 
                    startingStep = 0
                    ac = { 'row': c['row'], 'col': c['col'] + 1}

                tR = { 'row': c['row'], 'col':c['col'] + 1, 'count': c['count']+1, 'startingStep': startingStep, 'aCord': ac}
                q.append(tR)

            if (self.canWeVisit(c['row'], c['col'] -1, preChar)):
                startingStep = c['startingStep'] + 1
                ac = c['aCord']
                if (self.matrix[c['row']][c['col'] -1] == 'a'): 
                    startingStep = 0              
                    ac = { 'row': c['row'], 'col': c['col'] -1}

                tL = { 'row': c['row'],'col': c['col'] -1, 'count': c['count']+1, 'startingStep': startingStep, 'aCord': ac}
                q.append(tL)


        # print("Debug")
        # self.printVisited()

        return None

    def canWeVisit(self, row, col, prevChar):
        pos = {'row': row, 'col': col} # for some reason i recreated the object

        if (pos in self.visited):
            return False

        if(row < 0 or row >= self.rowLen):
            return False
        elif(col < 0 or col >= self.colLen):
            return False
        
        if (prevChar == 'S' ):
            if (self.matrix[row][col] == 'a'):
                return True
            else:
                return False

        if (self.matrix[row][col] == 'E'):
            if (prevChar == 'z'):
                return True
            else:
                return False

        # not too sure about this
        # 'a' + 1 >= 'b' (is good case)
        if(ord(prevChar) +1 >= ord(self.matrix[row][col])):
            return True
        
        return False

    def readInputToMatrix(self):
        #f = open('test_input.txt', 'r')
        f = open('input.txt', 'r')
        self.matrix = []

        for line in f:
            curRow = [*line.strip()]
            self.matrix.append(curRow)
    
        self.colLen = len(self.matrix[0])
        self.rowLen = len(self.matrix)
        # debug
        # self.printMatrix()
        return None

    
    def printMatrix(self):
        print("colLen: ", self.colLen, "rowLen: ", self.rowLen)
        for row in self.matrix:
            print(row)

    def printVisited(self):
        diagram = []
        for i in range(self.rowLen):
            row = []
            for j in range(self.colLen):
                row.append('.')
            diagram.append(row)

        for i in self.visited:
            diagram[i['row']][i['col']] = "#"

        print('--printVisited--')
        for row in diagram:
            print(row)

start = datetime.now()
sol = Solution()
sol.main()
end = datetime.now()
td = (end - start).total_seconds() * 10**3
print(f"The time of execution of above program is : {td:.03f}ms")


# Your puzzle answer was 488.
# I think there is a bug somewhere
# I think it took me 20-30 min of debugging
