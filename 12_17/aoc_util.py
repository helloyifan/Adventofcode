from collections import defaultdict

shape1 = '''
####
'''

shape2 = '''
.#.
###
.#.
'''

shape3 = '''
..#
..#
###
'''
shape4='''
#
#
#
#
'''

shape5='''
##
##
'''

def convertLinesIntoSparceMatList(shape):
    curRock = defaultdict(lambda: defaultdict(str))

    lines = shape.splitlines()[1:] # Stupid confusiong logic, but firts line is '', ignore it
    for lineIndex, lineVal in enumerate(lines):
        for charIndex, charVal in enumerate(lineVal):
            if (charVal == '#'):
                curRock[len(lines) - lineIndex][charIndex] = True
    return curRock

def findMaxHeightOfRocksInChamber(rocksInChamber):
    maxHeight = 0
    for y in rocksInChamber:
        for x in rocksInChamber[y]:
            if (rocksInChamber[y][x]):
                maxHeight = max(maxHeight, y)
                break
    return maxHeight

def printRockInChamber(rocksInChamber):
    maxHeight = findMaxHeightOfRocksInChamber(rocksInChamber)
    print('+-------+')
    for y in range(maxHeight, -1, -1):
        line = ['.'] * 7

        for x in rocksInChamber[y]:
            if (rocksInChamber[y][x] == True):
                line[x] = '#'
        
        printLine = ''
        for i in line:
            printLine += i
        
        print('|' + printLine + '|:' + str(y))
    print('+-------+')