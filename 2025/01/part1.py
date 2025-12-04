
import sys


class Solution():
    def solve(self):
        input = read_file_get_input_string()

        curPos = 50
        ret = 0

        for str in input:
            obj = self.splitDirAndMagnitude(str)

            if obj['d'] == 'L':
                curPos = self.turnLeft(curPos, obj['mag'])
            elif obj['d'] == 'R':
                curPos = self.turnRight(curPos, obj['mag'])
            else:
                raise "you fucked up"

            print(curPos)
            if curPos == 0:
                ret += 1

        print("End ret: ", ret)
        return ret
    
    def splitDirAndMagnitude(self, str):
        d = str[:1]
        mag = int(str[1:])
        return {'d': d, 'mag': mag}

    def turnLeft(self, curPos, num):
        ret = curPos - num
        while ret < 0:
            ret += 100
        return ret
    
    def turnRight(self, curPos, num):
        ret = curPos + num
        while ret > 99:
            ret -= 100
        return ret



def read_file():
    if len(sys.argv) != 2:
        print("Pass in a file name (and only the filename)")
        sys.exit(1)

    file_name = sys.argv[1]
    file = open(file_name, "r")
    return file

def read_file_get_input_string():
    return read_file().read().strip().split('\n')


sol = Solution()
sol.solve()


# 272 is too low