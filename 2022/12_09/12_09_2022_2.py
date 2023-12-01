import copy

class Solution():
    pos = []
    tVisitedPos = []

    def main(self):

        for i in range(10):
            self.pos.append({'row':0, 'col':0})
        self.tVisitedPos.append(str(self.pos[9]['row']) + '#' + str(self.pos[9]['col']))

        f = open("input.txt", "r")
        for line in f:
            move = line.strip().split(' ')
            move[1] = int(move[1])
            if (move[0] == 'U'):
                self.moveUp(move[1])
            elif (move[0] == 'D'):
                self.moveDown(move[1])
            elif (move[0] == 'L'):
                self.moveLeft(move[1])
            elif (move[0] == 'R'):
                self.moveRight(move[1])

        print('tVisitedPos:', self.tVisitedPos)
        print(len(set(self.tVisitedPos)))
        return None

    def moveUp(self, unit):
        for i in range(unit):
            self.pos[0]['row'] += 1
            self.movementHelper()
        return None

    def moveDown(self, unit):
        for i in range(unit):
            self.pos[0]['row'] -= 1
            self.movementHelper()
        return None

    def moveLeft(self, unit):
        for i in range(unit):
            self.pos[0]['col'] -= 1
            self.movementHelper()
        return None

    def moveRight(self, unit):
        for i in range(unit):
            self.pos[0]['col'] += 1
            self.movementHelper()
        return None
    
    def movementHelper(self):
        for i in range(1, 10):
            curH, curT = i-1, i
            self.moveTailUpdateCache(curH, curT) if self.needToMove(curH, curT) else None
            
            if (i == 9):
                self.tVisitedPos.append(str(self.pos[9]['row']) + '#' + str(self.pos[9]['col']))

        return None

    def needToMove(self, curH, curT):
        if (abs(self.pos[curH]['row'] - self.pos[curT]['row']) > 1 or 
            abs(self.pos[curH]['col'] - self.pos[curT]['col']) > 1):
            return True
        return False

    def moveTailUpdateCache(self, curH, curT):
        # Same Row
        if (self.pos[curH]['row'] == self.pos[curT]['row']):
            self.colDiffBy2(curH, curT)
        # Same Col
        elif (self.pos[curH]['col'] == self.pos[curT]['col']):
            self.rowDiffBy2(curH, curT)

        # Row diff by 1 (col diff by 2)
        elif (abs(self.pos[curH]['row'] - self.pos[curT]['row']) == 1 and
            abs(self.pos[curH]['col'] - self.pos[curT]['col']) == 2):
            # set row to be the same
            self.pos[curT]['row'] = int(self.pos[curH]['row'])
            self.colDiffBy2(curH, curT)

        # col diff by 1 (row diff by 2)
        elif (abs(self.pos[curH]['col'] - self.pos[curT]['col']) == 1 and
            abs(self.pos[curH]['row'] - self.pos[curT]['row']) == 2):
            # set col to be the same
            self.pos[curT]['col'] = int(self.pos[curH]['col'])
            self.rowDiffBy2(curH, curT)
        
        # col diff by 1 (row diff by 2)
        elif (abs(self.pos[curH]['col'] - self.pos[curT]['col']) == 2 and
            abs(self.pos[curH]['row'] - self.pos[curT]['row']) == 2):
            # set col to be the same
            self.colDiffBy2(curH, curT)
            self.rowDiffBy2(curH, curT)
        

        else:
            print('--------------------')
            print("Shouldn't see this: ", curH, curT)
            print(self.pos[curH], self.pos[curT])

        return None

    def colDiffBy2(self, curH, curT):
        if (self.pos[curH]['col']  > self.pos[curT]['col'] + 1):
            self.pos[curT]['col']  += 1
        elif (self.pos[curH]['col'] < self.pos[curT]['col'] - 1):
            self.pos[curT]['col']  -= 1
        return None

    def rowDiffBy2(self, curH, curT):
        if (self.pos[curH]['row']  > self.pos[curT]['row'] + 1):
            self.pos[curT]['row']  += 1
        elif (self.pos[curH]['row'] < self.pos[curT]['row'] - 1):
            self.pos[curT]['row']  -= 1
        return None


sol = Solution()
sol.main()

## Result is 2724
## After thought, i didnt understand the question well enough
## or consider the edge cases 

## I considered all of the cases except this below, which i thought was impossible, turns out its possible
##        elif (abs(self.pos[curH]['col'] - self.pos[curT]['col']) == 2 and
##            abs(self.pos[curH]['row'] - self.pos[curT]['row']) == 2):