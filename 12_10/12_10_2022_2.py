class Solution():
    def main(self):
        #consts
        f = open("input.txt", "r")
        cycle = 0
        xRegVal = 1
        signalStrength = 40 #updated to 40
        currentCRTRow = ''
        actionStack = []

        runningSumOfBoostedVals = 0

        while True:
            cycle += 1

            screenSymbol = self.checkLit(currentCRTRow, xRegVal)
            # Not sure what i want to do with this 
            # currentScreen= self.stringReplacement(currentScreen, cycle-1, screenSymbol)
            currentCRTRow += screenSymbol

            if (cycle == signalStrength):
                boostedVal = xRegVal*signalStrength
                runningSumOfBoostedVals += boostedVal
                signalStrength += 40
                print(currentCRTRow)
                currentCRTRow = '' #reset

            if (len(actionStack) > 0):
                xVal = actionStack.pop()
                #print(xRegVal, xVal)
                xRegVal += xVal

            else:
                # cleaning up input
                line =  f.readline()
                if (not line):
                    break
                
                command = line.strip().split()
                if (command[0] == 'noop'):
                    continue
                elif (command[0] == 'addx'):
                    toProcess =int(command[1])
                    actionStack.append(toProcess)

        if (len(actionStack) > 0):
            xVal = actionStack.pop()
            xRegVal += xVal


        return None

    # If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, 
    # the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.).
    def checkLit(self, currentCRTRow, middleSprintPos):
        if (len(currentCRTRow) == middleSprintPos-1 or
            len(currentCRTRow) == middleSprintPos or
            len(currentCRTRow) == middleSprintPos +1):
            return '#'
        return '.'

    def stringReplacement(self, myStr, n, replacement):
        return myStr[0:n] + replacement + myStr[n+1:]
            
sol = Solution()
sol.main()


## Answer is : Go fuck yourself
###..###..###...##..###...##...##..####.
#..#.#..#.#..#.#..#.#..#.#..#.#..#.#....
#..#.###..#..#.#..#.#..#.#..#.#....###..
###..#..#.###..####.###..####.#.##.#....
#.#..#..#.#....#..#.#.#..#..#.#..#.#....
#..#.###..#....#..#.#..#.#..#..###.#....

## Took me atleast another 33 mins
