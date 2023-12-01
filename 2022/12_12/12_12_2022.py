class Solution():
    def main(self):
        self.readInputToMatrix()
        # self.navigateMatrix(0,0)
        self.navigateMatrix(20,0)
        return None

    def navigateMatrix(self, startRow, startCol):
        # if (self.matrix[row, col] == 'S'):
        #     # Starting on S is kinda weird but its all good 
        
        self.visited = []

        ## Init the BFS stuff
        startingPos = {'row': startRow, 'col': startCol, 'count': 0}
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
                tU = { 'row': c['row'] + 1, 'col': c['col'], 'count': c['count']+1}
                q.append(tU)
            if (self.canWeVisit(c['row'] - 1, c['col'], preChar)):
                tD = { 'row': c['row'] - 1, 'col':c['col'], 'count': c['count']+1}
                q.append(tD)
            if (self.canWeVisit(c['row'], c['col'] + 1, preChar)):
                tR = { 'row': c['row'], 'col':c['col'] + 1, 'count': c['count']+1}
                q.append(tR)
            if (self.canWeVisit(c['row'], c['col'] -1, preChar)):
                tL = { 'row': c['row'],'col': c['col'] -1, 'count': c['count']+1} 
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

sol = Solution()
sol.main()


# Spent 55 mins in the morning
# Spent another 23 min debugging
# Spent another 10 min debugging

#  Your puzzle answer was 490.

