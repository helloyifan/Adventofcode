import sys
import re
from aoc_commons import file_reader as ac

#  python3 -m 01.aoc_2023_01 01/input.txt

class Solution():
    
    game_input = []
    print("i just added this lol")
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
        f = ac.read_file()
        final_ret = 0
        for line in f:
            self.parse_input_string(line)
        
        for num_game, game in enumerate(self.game_input):
            lost_flag = False
            for roundd in game:
                if (
                    (roundd.get('red') and roundd['red'] > self.limits['red']) or 
                    (roundd.get('blue') and roundd['blue'] > self.limits['blue']) or
                    (roundd.get('green') and roundd['green'] > self.limits['green'])
                ):
                    print("cant beat: ", num_game + 1)
                    print(roundd)
                    lost_flag = True
                    break
            
            if (lost_flag == False):
                num_game_with_index_offset = num_game +1
                final_ret = final_ret + num_game_with_index_offset

        print("final_ret: ", final_ret)
        return final_ret



if __name__ == "__main__":
    sol = Solution()
    sol.cube_conundrum()
