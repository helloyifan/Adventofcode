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
        self.nameNumberCache['humn'] = 1j

        rootMonkey1 = self.nameProblemCache['root']['monkey1']
        rootMonkey2 = self.nameProblemCache['root']['monkey2']

        while len(self.nameProblemCache) > 0:
            self.goThroughProblems()
            print("nameNumberCache:", self.nameNumberCache)
            print("nameProblemCache:", self.nameProblemCache)
            print('----')


        print(rootMonkey1 , self.nameNumberCache[rootMonkey1])
        print(rootMonkey2 , self.nameNumberCache[rootMonkey2])

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

'''
Alternative solution approach, not recommmended

Anecdote: take advantage of imaginary nubmers (1j)
We know that root: bzrn == gvhs

if we set humn to be 1j we set the following values

bzrn (17255400702289.148-3.4265558075081888j)
gvhs 3952741911612.0

If we treat j like a variable for humn, we see that j = 3882224466191 which is the answer

>>> 3952741911612.0 - 17255400702289.148
-13302658790677.148
>>> a = 3.4265558075081888
>>> b = 13302658790677.148
>>> b/a
3882224466191.0
'''