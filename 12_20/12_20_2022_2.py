import sys

class Solution():
    decryptKey = 811589153

    def main(self):
        numList = self.parseInput()
        
        # Part 1
        #self.handlePart1(numList)

        # Part 2
        self.applyDecryptKey(numList)
        for i in range(0,10):
            self.handlePart1(numList)
            print("After round:", i+1)    
            # self.printNumList(numList)

        indexOf0 = self.find0Index(numList)
        print ("Final index of 0: ", indexOf0)
        print(numList[indexOf0])

        index1k = (indexOf0 + 1000) % len(numList)
        index2k = (indexOf0 + 2000) % len(numList)
        index3k = (indexOf0 + 3000) % len(numList)

        print("1000th", numList[index1k], 'index1k', index1k)
        print("2000th", numList[index2k], 'index2k', index2k)
        print("3000th", numList[index3k], 'index3k', index3k)

        print("Final Ret: ", numList[index1k]['val'] + numList[index2k]['val'] + numList[index3k]['val'])

        return None


    def find0Index(self, numList):
        for i, e in enumerate(numList):
            if (e['val'] == 0):
                return i
        print("cant find 0")
        return None

    def parseInput(self):
        numList = []
        f = open(str(sys.argv[1]), 'r')

        lineCounter = 0 
        for line in f:
            #numList.append(int(line.strip()))
            item =  {'val':int(line.strip()), 'startPos': lineCounter}
            numList.append(item)

            lineCounter += 1
        return numList

    def applyDecryptKey(self, numList):
        for i in range(len(numList)):
            numList[i]['val'] *= self.decryptKey
        return None

    def handlePart1(self, numList):
        pos = 0
        while (pos < len(numList)):
            index = self.findItemInList(numList, pos)

            popped = numList.pop(index)            
            newIndex = index + popped['val'] #figure this out so its always a positive value

            # Normally insert will handle indexes that are in the edge case 
            # but we need to decide on whether or not to move index
            if (newIndex <= 0 or newIndex >= len(numList)):
                newIndex = newIndex % len(numList)
        
            numList.insert(newIndex, popped)
            pos += 1

            #print(newIndex, index)
            #self.printNumList(numList)
        return None

    def findItemInList(self, numList, curPos):
        for i, e in enumerate(numList):
            if (e['startPos'] == curPos):
                return i
        print("Cant find from findItemInList ")
        return None

    def printNumList(self, numList):
        for i in numList:
            print(i['val'], end=', ')
        print('')

sol = Solution()
sol.main()

# Took 15mins
# I didn't do it the smart way, but i also dont care atm
# Final Ret:  3390007892081