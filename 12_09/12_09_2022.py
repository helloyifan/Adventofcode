import copy

class Solution():
    hPos = {'row': 0, 'col':0}
    tPos = {'row': 0, 'col':0}
    tVisitedPos = []

    def main(self):
        self.tVisitedPos.append(str(self.tPos['row']) + '#' + str(self.tPos['col']))

        f = open("test_input.txt", "r")
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
            prevHPos = copy.deepcopy(self.hPos)
            self.hPos['row'] += 1
            self.moveTailUpdateCache(prevHPos) if self.needToMove() else None
        return None

    def moveDown(self, unit):
        for i in range(unit):
            prevHPos = copy.deepcopy(self.hPos)
            self.hPos['row'] -= 1
            self.moveTailUpdateCache(prevHPos) if self.needToMove() else None
        return None

    def moveLeft(self, unit):
        for i in range(unit):
            prevHPos = copy.deepcopy(self.hPos)
            self.hPos['col'] -= 1
            self.moveTailUpdateCache(prevHPos) if self.needToMove() else None
        return None

    def moveRight(self, unit):
        for i in range(unit):
            prevHPos = copy.deepcopy(self.hPos)
            self.hPos['col'] += 1
            self.moveTailUpdateCache(prevHPos) if self.needToMove() else None
        return None

    def needToMove(self):
        if (abs(self.hPos['row'] - self.tPos['row']) > 1 or 
            abs(self.hPos['col'] - self.tPos['col']) > 1):
            return True
        return False

    def moveTailUpdateCache(self, prevHPos):
        self.tPos = copy.deepcopy(prevHPos) #this is not good
        self.tVisitedPos.append(str(self.tPos['row']) + '#' + str(self.tPos['col']))

sol = Solution()
sol.main()

# Answer is 6503