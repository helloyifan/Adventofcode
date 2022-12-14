class Solution():
    leftLst = []
    rightLst = []
    runningSum = 0

    def printInput(self):
        for i in range(len(self.leftLst)):
            print(self.leftLst[i])
            print(self.rightLst[i])
            print()

    def main(self):
        self.parseInput()
        #self.printInput()
        # Technically both left and right have same length
        for i in range(len(self.leftLst)):
            self.isIndexInRightOrder(self.leftLst[i], self.rightLst[i], i+1)
        
        print("runningSum: ", self.runningSum)
        return None

    

    def isIndexInRightOrder(self, lLst, rLst, pairNum=None):
        c = 0
        # If the left list runs out of items first, the inputs are in the right order
        while (c < len(lLst) and c < len(rLst)):
            l, r = lLst[c], rLst[c]
            if (isinstance(l, list) and isinstance(r, list)):
                result = self.isIndexInRightOrder(l, r)
                if (result == False):
                    return False
                elif(result == True):
                    if (pairNum != None):
                        print("pairNum: ", pairNum)
                        self.runningSum += pairNum
                    return True
                # if its 'None' We continue the loop fyi
            elif(isinstance(l, int) and isinstance(r, list)):
                result = self.isIndexInRightOrder([l], r)

                if (result == False):
                    return False
                elif(result == True):
                    if (pairNum != None):
                        print("pairNum: ", pairNum)
                        self.runningSum += pairNum
                    return True

            elif(isinstance(l, list) and isinstance(r, int)):
                result = self.isIndexInRightOrder(l, [r])
                
                if (result == False):
                    return False
                elif(result == True):
                    if (pairNum != None):
                        print("pairNum: ", pairNum)
                        self.runningSum += pairNum
                    return True

            else:
            # If the left integer is lower than the right integer, the inputs are in the right order.
                if l > r:
                    return False
                elif l < r:                    
                    if (pairNum != None):
                        print("pairNum: ", pairNum)
                        self.runningSum += pairNum
                    return True
        
            c += 1
        
        # If the left list runs out of items first, the inputs are in the right order
        # If the right list runs out of items first, the inputs are not in the right order. 
        if (len(lLst) > len(rLst)):
            return False
        elif (len(lLst) == len(rLst)):
            return None
        else:
            if (pairNum != None):
                print("why thou: ", pairNum)
                self.runningSum += pairNum

        return True

        
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


# Spent 57min in the morning but misintrepted the problem
# Spent another 30 min debugging
# Final Answer 5852