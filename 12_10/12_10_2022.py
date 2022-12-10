class Solution():
    def main(self):
        f = open("test_input.txt", "r")

        cycle = 0
        xRegVal = 1
        signalStrength = 20

        actionStack = []

        runningSumOfBoostedVals = 0

        while True:
            cycle += 1

            if (cycle == signalStrength and signalStrength <= 220):
                #print(signalStrength, "*", xRegVal)
                #print(xRegVal*signalStrength)
                boostedVal = xRegVal*signalStrength
                runningSumOfBoostedVals += boostedVal
                signalStrength += 40

            if (len(actionStack) > 0):
                xVal = actionStack.pop()
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


        print("Running Sum of Boosted Vals: ", runningSumOfBoostedVals)
        return None

sol = Solution()
sol.main()


## Answer is : 12740
## Took me 36 mins
