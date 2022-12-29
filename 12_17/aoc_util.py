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
    print(lines)

    for lineIndex, lineVal in enumerate(lines):
        for charIndex, charVal in enumerate(lineVal):
            if (charVal == '#'):
                curRock[lineIndex][charIndex] = True
    return curRock