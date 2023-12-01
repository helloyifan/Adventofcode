import sys

class Solution():
    def main(self):
        numList = self.parseInput()
        self.handlePart1(numList)        
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
            numList.append( {'val':int(line.strip()), 'moved': False})

            lineCounter += 1
        return numList

    def handlePart1(self, numList):

        index = 0

        while (index < len(numList)):
            if (numList[index]['moved'] == True):
                index +=1
                continue

            popped = numList.pop(index)            
            newIndex = index + popped['val'] #figure this out so its always a positive value

            # Normally insert will handle indexes that are in the edge case 
            # but we need to decide on whether or not to move index
            if (newIndex <= 0 or newIndex >= len(numList)):
                newIndex = newIndex % len(numList)
        
            numList.insert(newIndex, popped)
            popped['moved'] = True

            #print(newIndex, index)
            #self.printNumList(numList)

        return None

    def printNumList(self, numList):
        for i in numList:
            print(i['val'], end=', ')
        print('')
sol = Solution()
sol.main()


# You guessed 1470. too low. Typo bug
# You guessed -2910. That's not the right answer (i was not modding numlist on line 58 , i was adding and subtracting and that didnt work well for vals greater then len(numList))
# Correct answer Final Ret:  5498

# Took 1 hour