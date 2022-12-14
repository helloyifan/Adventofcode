from functools import cmp_to_key

class Solution():
    leftLst = []
    rightLst = []
    runningSum = 0

    def printPart2Input(self, lst):
        for i in lst:
            print(i)

    def main(self):
        self.parseInput()
        part2Input = []
        part2Input.extend(self.leftLst)
        part2Input.extend(self.rightLst)
        part2Input.append([2])
        part2Input.append([6])
        
        # Debug
        # self.printPart2Input(part2Input)
        # print('----')
        
        sortedLst = sorted(part2Input, key=cmp_to_key(lambda item1, item2: self.isIndexInRightOrder(item1, item2)))

        # Debug
        #self.printPart2Input(sortedLst)
        #self.printPart2Input(part2Input)

        # Final Ret
        rollingProduct = 1

        for i, e in enumerate(sortedLst):
            if (e == [2]):
                print("[2]", i+1)
                rollingProduct *= (i+1)
            elif(e == [6]):
                print("[6]", i+1)
                rollingProduct *= (i+1)

        print('rollingProduct: ', rollingProduct)
        return None


    def isIndexInRightOrder(self, lLst, rLst):
        c = 0
        # If the left list runs out of items first, the inputs are in the right order
        while (c < len(lLst) and c < len(rLst)):
            l, r = lLst[c], rLst[c]
            if (isinstance(l, list) and isinstance(r, list)):
                result = self.isIndexInRightOrder(l, r)
                if (result == 1):
                    return 1
                elif(result == -1):
                    return -1
                # if its 'None' We continue the loop fyi
            elif(isinstance(l, int) and isinstance(r, list)):
                result = self.isIndexInRightOrder([l], r)
                if (result == 1):
                    return 1
                elif(result == -1):
                    return -1

            elif(isinstance(l, list) and isinstance(r, int)):
                result = self.isIndexInRightOrder(l, [r])
                if (result == 1):
                    return 1
                elif(result == -1):
                    return -1

            else:
            # If the left integer is lower than the right integer, the inputs are in the right order.
                if l > r:
                    return 1
                elif l < r:                    
                    return -1
        
            c += 1
        
        # If the left list runs out of items first, the inputs are in the right order
        # If the right list runs out of items first, the inputs are not in the right order. 
        if (len(lLst) > len(rLst)):
            return 1
        elif (len(lLst) == len(rLst)):
            return 0

        return -1

        
    def parseInput(self):
        f = open('input.txt', 'r')
        while True:
            self.leftLst.append(eval(f.readline().strip()))
            self.rightLst.append(eval(f.readline().strip()))

            if(not f.readline()):
                break

        return None

sol = Solution()
sol.main()


# didn't time this was too obsesesd
# [2] 118
# [6] 205
# rollingProduct:  24190