
import sys
import re

#sys.path.append('/home/jonathan/workspace/gitShitDone/Adventofcode/2023')
from aoc_commons import file_reader

#  python3 -m 01.aoc_2023_01 01/input.txt

class Solution():
    
    game_input = []

    limits = {
        'red':  12,
        'green': 13,
        'blue': 14
    }

    def parse_input_string(self, i):
        ## Remove ":"
        index_of_colon = i.find(':')
        input_no_colon = i[index_of_colon + 1:]

        ## Split up into sections ";"
        list_of_rounds = input_no_colon.split(';')
        
        round_set = []
        for r in list_of_rounds:
            colors = r.split(',')

            input_set = {}
            for color in colors:

                if color.find('red') != -1:
                    input_set['red'] = self.pull_num_from_string_lol(color)
                elif color.find('blue') != -1:
                    input_set['blue'] = self.pull_num_from_string_lol(color)
                elif color.find('green') != -1:
                    input_set['green'] = self.pull_num_from_string_lol(color)

            round_set.append(input_set)

        self.game_input.append(round_set)
    
    def pull_num_from_string_lol(self, input_string):
        # Define the regex pattern to match a number
        pattern = r'\d+'
        matches = re.findall(pattern, input_string)
        return int(matches[0])


    def cube_conundrum(self):
        f = file_reader.read_file()
        final_ret = 0
        for line in f:
            self.parse_input_string(line)
        
        for num_game, game in enumerate(self.game_input):
            lost_flag = False

            min_of_color = {
                'red':  float('-inf'),
                'green': float('-inf'),
                'blue': float('-inf')
            }

            for roundd in game:
                if (roundd.get('red') and roundd.get('red') > min_of_color.get('red')):
                    min_of_color['red'] = roundd.get('red')
                if (roundd.get('blue') and roundd.get('blue') > min_of_color.get('blue')):
                    min_of_color['blue'] = roundd.get('blue')
                if (roundd.get('green') and roundd.get('green') > min_of_color.get('green')):
                    min_of_color['green'] = roundd.get('green')

            print(min_of_color)

            power = min_of_color['red'] * min_of_color['blue'] * min_of_color['green'] 
            final_ret = final_ret + power

        print("final_ret: ", final_ret)
        return final_ret



if __name__ == "__main__":
    sol = Solution()
    sol.cube_conundrum()