import sys
import re


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
        cur_loc = 'AAA'
        
        while True:
            next_step_dir = self.directions[ steps % len(self.directions)]
            
            # print('next_step_dir: ', next_step_dir)

            cur_loc =  self.wasteland_map[cur_loc][next_step_dir]
            # print('cur_loc: ', cur_loc)

            steps += 1
            
            if cur_loc == 'ZZZ':
                return steps
            
        return 


    def haunted_wasteland(self):
        l = self.parse_input()
        self.process_input(l)
        ret = self.move_through_wasteland()

        print(self.directions)
        print(self.wasteland_map)
        print('ret: ', ret)
        return
    

if __name__ == "__main__":
    sol = Solution()
    sol.haunted_wasteland()