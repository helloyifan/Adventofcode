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
        self.parseInput()

        while len(self.nameProblemCache) > 0:
            self.goThroughProblems()
            print("nameNumberCache:", self.nameNumberCache)
            print("nameProblemCache:", self.nameProblemCache)
            print('----')

        return None

    def goThroughProblems(self):
        problemsToRemove = []

        for key in self.nameProblemCache:
            problem = self.nameProblemCache[key]
            cache = self.nameNumberCache

            if (problem['monkey1'] in cache and problem['monkey2'] in cache):
                cache[key] = lambdaOps[problem['operator']](cache[problem['monkey1']], cache[problem['monkey2']])
                problemsToRemove.append(key)
                print(cache[key])

        for key in problemsToRemove:
            del self.nameProblemCache[key] # Remove the problems we just solved

    def parseInput(self):
        f = open(str(sys.argv[1]), 'r')

        for line in f:
            # match function will return None when there is no match
            # match = res.search('[a-z][a-z][a-z][a-z]\: \d+', line)
            m = re.match("(?P<name>\w+)\: (?P<val>\d+)", line)
            if (m):
                self.nameNumberCache[m['name']] = int(m['val'])

            n = re.match("(?P<name>\w+)\: (?P<monkey1>\w+) (?P<operator>(\+|\-|\/|\*)) (?P<monkey2>\w+)", line)
            if (n):
                self.nameProblemCache[n['name']] = {
                    'monkey1':  n['monkey1'],
                    'monkey2':  n['monkey2'],
                    'operator': n['operator']
                }

        # Debug
        # print(self.nameNumberCache)
        # print(self.nameProblemCache)
        return None

sol = Solution()
sol.main()