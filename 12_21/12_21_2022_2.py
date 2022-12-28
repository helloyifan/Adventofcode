import sys
import re
import operator

lambdaOps = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

class Solution():
    nameNumberCache = {}
    nameProblemCache = {}

    def main(self):
        numberCache, problemCache = self.parseInput()

        # Modify input for part2
        del numberCache['humn']
        problemCache['root']['operator'] = '='

        self.firstSolveAsMuchAsYouCan(numberCache, problemCache)

        print("nameNumberCache:", numberCache)
        print("nameProblemCache:", problemCache)
        print('----')
        return None

    
    def firstSolveAsMuchAsYouCan(self, nameNumberCache, nameProblemCache):
        cur, prev = 0, len(self.nameProblemCache)
        while cur != prev:
            self.goThroughProblems(nameNumberCache, nameProblemCache)
            prev = cur
            cur = len(self.nameProblemCache)

        return None

    def secondBuildNewListOfProblems(self):
        return None

    def thirdSolvedNewListOfProblems(self):
        return None

    def goThroughProblems(self, nameNumberCache, nameProblemCache):
        problemsToRemove = []

        for key in nameProblemCache:
            problem = nameProblemCache[key]
            cache = nameNumberCache

            if (problem['monkey1'] in cache and problem['monkey2'] in cache):
                cache[key] = lambdaOps[problem['operator']](cache[problem['monkey1']], cache[problem['monkey2']])
                problemsToRemove.append(key)
                print(cache[key])

        for key in problemsToRemove:
            del nameProblemCache[key] # Remove the problems we just solved

    def parseInput(self):
        numberCache, problemCache = {}, {}
        f = open(str(sys.argv[1]), 'r')

        for line in f:
            # match function will return None when there is no match
            # match = res.search('[a-z][a-z][a-z][a-z]\: \d+', line)
            m = re.match("(?P<name>\w+)\: (?P<val>\d+)", line)
            if (m):
                numberCache[m['name']] = int(m['val'])

            n = re.match("(?P<name>\w+)\: (?P<monkey1>\w+) (?P<operator>(\+|\-|\/|\*)) (?P<monkey2>\w+)", line)
            if (n):
                problemCache[n['name']] = {
                    'monkey1':  n['monkey1'],
                    'monkey2':  n['monkey2'],
                    'operator': n['operator']
                }



        # Debug
        # print(self.nameNumberCache)
        # print(self.nameProblemCache)
        return numberCache, problemCache

sol = Solution()
sol.main()

# WIP but unifished, should return the same result as 12_21_2022_2_alt.py