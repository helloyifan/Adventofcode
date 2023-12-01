import sys
import re

ORE, CLAY, OBSIDIAN, GEODE = 'ORE', 'CLAY', 'OBSIDIAN', 'GEODE'
MATERIALS = [ORE, CLAY, OBSIDIAN, GEODE]
Resource = 'Resource'
Robot = 'Robot'
unit = {
    Resource: {
        ORE: 0,
        CLAY: 0,
        OBSIDIAN:0,
        GEODE:0
    },
    Robot: {
        ORE: 0,
        CLAY: 0,
        OBSIDIAN:0,
        GEODE:0  
    }

}

class Solution:
    bluePrints = []
    dp = {}

    def main(self):
        self.parseInput()
        unit1 = unit.copy()

        unit1[Robot][ORE] = 1

        print(unit1)
        return None

    def parseInput(self):
        f = open(str(sys.argv[1]), 'r')

        for line in f:
            q = re.findall('\d+', line)
            blueprint = {
                ORE: {
                    ORE: int(q[1])
                },
                CLAY: {
                    ORE: int(q[2])
                },
                OBSIDIAN: {
                    ORE: int(q[3]),
                    CLAY: int(q[4]),
                },
                GEODE: {
                    ORE: int(q[5]),
                    OBSIDIAN: int(q[6])
                }
            }
            self.bluePrints.append(blueprint)

        print(blueprint)
    # Max Geode you can get if you have this set of robots?
    def turn(self, turnNumber):

        return None


sol = Solution()
sol.main()