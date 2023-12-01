

class Solution():

    def main(self):
        f = open("input.txt", "r")
        rollingSum = 0
        for x in f:
            ret = self.findDuplicate(x.rstrip())
            #print(ret)
            val = self.convertLetterToVal(ret)
            #print(val)
            rollingSum += val

        print("Rolling Sum:", rollingSum)
        return None

    def findDuplicate(self, s):
        strLen = len(s)
        halfStrLen = strLen//2 #Floor division to get integer
        frontHalf = s[:halfStrLen]
        backHalf = s[halfStrLen:]

        frontHalfSet = set(frontHalf)
        for x in backHalf:
            if (x in frontHalfSet):
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