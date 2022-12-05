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

            #So [move*-1:] works because [-1:] is ignoring the first number right
            numbersToMove = stacks[moveFrom][move*-1:]

            # .extend does not need reassignment
            stacks[moveTo].extend(numbersToMove)

            # And [:move*-1] is just the other vals in the list
            stacks[moveFrom] = stacks[moveFrom][:move*-1] #we are doing a reassignemnt


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

##
## 1 5 9 13
## 
