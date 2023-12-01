
import sys
sys.path.append('/home/jonathan/workspace/gitShitDone/Adventofcode/2023')
from helper.file_reader import read_file

class Solution():
    def trebuchet(self):
        f = read_file()

        runningSum = 0
        for line in f:
            firstLetter = self.findFirstNum(line)
            lastLetter = self.findLastNum(line)
            curVal =int(firstLetter + lastLetter)

            runningSum += curVal

        print("Result: " , runningSum)
        return runningSum

    def findFirstNum(self, string):
        for i in range(0, len(string)):
            try:
                return self.checkIfNumber(string[i])
            except ValueError:
                continue
    
    def findLastNum(self, string):
        for i in range(len(string)-1, -1, -1):
            try:
                return self.checkIfNumber(string[i])
            except ValueError:
                continue
    
    def checkIfNumber(self, string):
        try:
            int(string)
            return(string)
        except ValueError:
            raise ValueError("Input is not a valid integer")


if __name__ == "__main__":
    sol = Solution()
    sol.trebuchet()