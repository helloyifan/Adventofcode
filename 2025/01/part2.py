
import sys


class Solution():
    def solve(self):
        input = read_file_get_input_string()

        curPos = 50
        self.finRet = 0

        for str in input:
            obj = self.splitDirAndMagnitude(str)

            if obj['d'] == 'L':
                curPos = self.turnLeft(curPos, obj['mag'])
            elif obj['d'] == 'R':
                curPos = self.turnRight(curPos, obj['mag'])
            else:
                raise "you fucked up"

            print(curPos)

        print("End ret: ", self.finRet)
        return self.finRet
    
    def splitDirAndMagnitude(self, str):
        d = str[:1]
        mag = int(str[1:])
        return {'d': d, 'mag': mag}

    # Module division got too complicated, there is a way, but fuck you brute force is funny to me  
    def turnRight(self, cur, mag):
        for i in range(mag):
            cur -=1
            cur = cur % 100
            if cur == 0:
                self.finRet+=1

        return cur

    def turnLeft(self, cur, mag):
        for i in range(mag):
            cur += 1
            cur = cur % 100
            if cur == 0:
                self.finRet+=1
        return cur

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


# 5967 is too high
# 5937 is right