import re
import math
class Monkey():
    def __init__(self, number, items, op, testVal, passWhenTrue, passWhenFalse ):
        self.number = number
        self.items = items
        self.op = op
        self.testVal = testVal
        self.passWhenTrue = passWhenTrue
        self.passWhenFalse = passWhenFalse
        self.handledItemCounter = 0

    def print(self):
        print("number: ", self.number)
        print("items: ", self.items)
        print("op: ", self.op)
        print("testVal: ", self.testVal)
        print("passWhenTrue: ", self.passWhenTrue)
        print("passWhenFalse: ", self.passWhenFalse)
        print("handledItemCounter: ", self.handledItemCounter)
        print('----------------')

    def printItem(self):
        print("Monkey", self.number, ":", self.items)

class Solution():
    monkeyDict = {}
    monkeyDivisorsMultiplyied = 1 #init value

    def main(self):
        f = open("input.txt", "r")
        # monkey creation
        continueMonkeyCreation = True
        while (continueMonkeyCreation):     
            continueMonkeyCreation = self.readInputCreateMonkey(f)

        for key in self.monkeyDict:
            self.monkeyDivisorsMultiplyied *= self.monkeyDict[key].testVal

        print("monkeyDivisorsMultiplyied: ", self.monkeyDivisorsMultiplyied)

        # handle round 1
        for i in range(10000):
            for key in self.monkeyDict:
                self.handleMonkeyTurn(key)

            ## Debug, handle one money at a time
            #for key in self.monkeyDict:
            #   self.monkeyDict[key].printItem()

        ## Calculate Final Result
        listOfHandledItemCounter = []
        for key in self.monkeyDict:
            listOfHandledItemCounter.append(self.monkeyDict[key].handledItemCounter)
        
        largestCounter = max(listOfHandledItemCounter)
        listOfHandledItemCounter.remove(largestCounter)
        secondLargestCounter = max(listOfHandledItemCounter)

        print('largestCounter: ', largestCounter)
        print('secondLargestCounter: ', secondLargestCounter)
        print ('product: ', largestCounter * secondLargestCounter )
        return None

    def handleMonkeyTurn(self, numberKey):
        currMonkey = self.monkeyDict[numberKey]
        
        while (len(currMonkey.items) > 0):
            old = currMonkey.items.pop(0) #get item from list
            localVariables = {'old': old, 'new': 0}
            exec(currMonkey.op, globals(), localVariables) 

            ## Bored/Review when divide by 3 round down to nearest int 
            boredVal =  localVariables['new'] # For part 2 of the question we don't divide by 3
            
            ## Monkey tests if val is divisible by testVal
            nextMonkey = currMonkey.passWhenTrue if boredVal % currMonkey.testVal == 0 else currMonkey.passWhenFalse

            ## Optimization added Multiply divisors together
            remainderMonkeyDivisorValue = boredVal % self.monkeyDivisorsMultiplyied

            ## Pass to next monkey
            self.monkeyDict[nextMonkey].items.append(remainderMonkeyDivisorValue)
            
            ## Count up the item handled by 1
            currMonkey.handledItemCounter += 1

            ## Print monkey to debug
            # currMonkey.print()
            # self.monkeyDict[nextMonkey].print() #caught the new items
        
        return 0

    def readInputCreateMonkey(self, f):
        numberLine =  f.readline()
        startingItemsLine = f.readline()
        operationLine = f.readline()
        testLine = f.readline()
        passWhenTrueLine = f.readline()
        passWhenFalseLine = f.readline()
        checkForContinue = f.readline() #Throw away

        number = int(re.findall('\d+', numberLine)[0])
        startingItemsString = re.findall('\d+', startingItemsLine)
        startingItems = [int(i) for i in startingItemsString]
        operation = re.findall('new .*', operationLine)[0]
        test = int(re.findall('\d+', testLine)[0])
        passWhenTrue = int(re.findall('\d+', passWhenTrueLine)[0])
        passWhenFalse = int(re.findall('\d+', passWhenFalseLine)[0])

        monkey = Monkey(number, startingItems, operation, test, passWhenTrue, passWhenFalse)
        self.monkeyDict[int(number)] = monkey
        #monkey.print()

        if (checkForContinue == ''):
            return False
        return True

sol = Solution()
sol.main()


## It took me 1hour 30min
#Your puzzle answer was 56595.

