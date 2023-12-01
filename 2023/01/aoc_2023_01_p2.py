
import sys
sys.path.append('/home/jonathan/workspace/gitShitDone/Adventofcode/2023')
from helper.file_reader import read_file

spelled_out_number_dict = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

reversed_spelled_out_number_dict = {
    'eno': '1',
    'owt': '2',
    'eerht': '3',
    'ruof': '4',
    'evif': '5',
    'xis': '6',
    'neves': '7',
    'thgie': '8',
    'enin': '9'
}

number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

class Solution():
    def trebuchet(self):
        f = read_file()
        runningSum = 0
        for line in f:
            firstLetter = self.findFirstNum(line)
            lastLetter = self.findLastNum(line)
            curVal = int(firstLetter + lastLetter)

            runningSum += curVal
        print("runningSum: ", runningSum)
        return runningSum

    
    def findFirstNum(self, string):
        return self.helper(string, spelled_out_number_dict)

    def findLastNum(self, string):
        reversed_string = string[::-1]
        return self.helper(reversed_string, reversed_spelled_out_number_dict)


    def helper(self, string, dictOfNumbers):
        lowestIndex = float('inf')
        lowestIndexVal = None

        for spelled_out in dictOfNumbers:
            index = string.find(spelled_out)
            if (index != -1):

                if (lowestIndex > index):
                    lowestIndex = index
                    lowestIndexVal = dictOfNumbers[spelled_out]

        for number in number_list:
            index = string.find(number)

            if (index != -1):

                if (lowestIndex > index):
                    lowestIndex = index
                    lowestIndexVal = number


        return lowestIndexVal

if __name__ == "__main__":
    sol = Solution()
    sol.trebuchet()