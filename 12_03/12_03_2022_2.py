

class Solution():

    def main(self):
        f = open("input.txt", "r")
        rollingSum = 0
        inputStack = []
        for i, x in enumerate(f):
            inputStack.append(x.rstrip())

            if (len(inputStack) == 3):
                ret = self.findDuplicate(inputStack)
                print("Ret: ", ret)
                val = self.convertLetterToVal(ret)
                rollingSum += val
                inputStack = []


        print("Rolling Sum:", rollingSum)
        return None

    def findDuplicate(self, inputStack):
        set1 = set(inputStack[0])
        set2 = set(inputStack[1])
        
        for x in inputStack[2]:
            if (x in set1 and x in set2):
                return x
        
        print("Something is wrong")
        return None
    
    def convertLetterToVal(self, s):
        numVal = ord(s)

        if (numVal > 96):
            numVal -= 96
        else:
            numVal -= 65 # Bcuz A is 65
            numVal += 27 # Because Uppercase item types A through Z have priorities 27 through 52.

        return numVal

sol = Solution()
sol.main()