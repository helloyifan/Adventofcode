import re

class Solution():
    def main(self):
        f = open("input.txt", "r")

        stacks = {} # 9 because there can be 9 stacks
        for i in range(1,10):
            stacks[i] = []
        #1,5,9

        # Part 1: Handle list building 
        ## Handle list parseing
        for i in range (0, 8): #first part of input has 8 lines
            line = f.readline()
            
            for j in range(1,10): #there are 9 stacks
                pos = (j-1)*4 + 1 # position of letter
                if (line[pos] != ' '):
                    stacks[j].insert(0, line[pos]) # insert to write at start of list


        # Part 2: Throw away formatting
        f.readline()
        f.readline()

        # Part 3: Move arround the box
        for line2 in f:
            nums = re.findall('\d+', line2)  #\d means Digit, +1 or more
            # re.findall(pattern, string, flags=0)
            # https://docs.python.org/3/library/re.html#re.findall
            
            # If I was a smarter and better person
            # I do this properly
            move = int(nums[0])
            moveFrom = int(nums[1])
            moveTo = int(nums[2])
            
            # moving it all at once is annoying
            # so gonna pop and append 

            for i in range(move):
                val = stacks[moveFrom].pop()
                stacks[moveTo].append(val)

        ### Part 4: Print the top of every stack
        print(stacks)        
        ret = ''
        for i in range(1,10):
            print(i, "top val", stacks[i][-1] if len(stacks[i]) > 0 else 'None')
            if (len(stacks[i]) > 0 ):
                ret +=(stacks[i][-1])
        print("Final result: ", ret)
sol = Solution()
sol.main()

'''
{1: ['P', 'L'], 2: ['S', 'G', 'B', 'H', 'B', 'F', 'V', 'Z', 'D', 'R', 'B', 'W', 'J'], 3: ['J', 'C', 'P', 'P', 'B', 'N', 'R', 'L', 'S'], 4: ['C', 'F', 'V'], 5: ['R', 'S', 'D', 'L'], 6: ['T', 'T'], 7: ['J', 'W'], 8: ['J', 'T', 'V', 'C', 'D', 'B', 'M', 'R', 'N', 'W', 'P', 'H', 'B', 'B', 'T', 'R', 'P', 'Q'], 9: ['N', 'P', 'M']}
1 top val L
2 top val J
3 top val S
4 top val V
5 top val L
6 top val T
7 top val W
8 top val Q
9 top val M
Final result:  LJSVLTWQM
'''