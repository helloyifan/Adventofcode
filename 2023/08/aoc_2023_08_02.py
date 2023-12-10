import sys
import re
import math

class Solution:
    
    directions = []
    wasteland_map = {}

    def parse_input(self):
        with open(sys.argv[1]) as fin:
            lines = fin.read().strip().split("\n")
        return lines
    
    def process_input(self, lines):
        pattern  =r'(\w+) = \((\w+), (\w+)\)'
        for i, e in enumerate(lines):
            if i == 0:
                for d in e:
                    self.directions.append(d)
                continue
            if not e: # empty case im lazy
                continue
        
            match = re.match(pattern, e)
            rets = match.groups()

            self.wasteland_map[rets[0]] = {
                'L': rets[1],
                'R': rets[2]
            }
        return
    
    def move_through_wasteland(self):
        steps = 0
        cur_loc = []

        for i, e in self.wasteland_map.items():
            if i[2] == 'A':
                cur_loc.append(i)
        
        step_list = []
        for cl in cur_loc:
            temp = self.move_through_wasteland_helper(cl)
            step_list.append(temp)
        return step_list


    def move_through_wasteland_helper(self, starting_loc):
        steps = 0
        cur_loc = starting_loc
        while True:
            next_step_dir = self.directions[ steps % len(self.directions)]
            cur_loc =  self.wasteland_map[cur_loc][next_step_dir]
            steps += 1
            if cur_loc[2] == 'Z':
                print(cur_loc)
                return steps
            


    def haunted_wasteland(self):
        l = self.parse_input()
        self.process_input(l)
        ret = self.move_through_wasteland()

        fin_ret = math.lcm(*ret)
        print('ret: ', ret)
        print('fin_ret: ', fin_ret)
        return
    

if __name__ == "__main__":
    sol = Solution()
    sol.haunted_wasteland()


# 14449445933179