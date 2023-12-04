import sys
import re
from aoc_commons import file_reader

#  python3 -m 01.aoc_2023_01 01/input.txt

class Solution():
    
    p2_ret = 0

    multiplier_map = {}


    def scratchcards(self):
        f = file_reader.read_file()

        lines = f.readlines()

        for line_num in range(1, len(lines) + 1): # I'm an awful person for like assuming line # is same as card number
            self.multiplier_map[line_num] = 1
            
        for line in lines: 
            card_num, card, numbers = self.parse_input(line)
            self.match_num(card_num, card, numbers)


        ## compute ret

        print(self.multiplier_map)
        
        for key in self.multiplier_map:
            self.p2_ret += self.multiplier_map[key]


        print('p2_ret: ', self.p2_ret)

        return

    def parse_input(self, line):
        card_num_string = line.split(':')[0]
        card_num = int(re.search(r'\d+', card_num_string).group())

        card_and_numbers = line.split(':')[1].strip()
        card_string = card_and_numbers.split('|')[0].strip()
        numbers_string = card_and_numbers.split('|')[1].strip()
        
        card = [item for item in card_string.split(' ') if item != '']

        numbers = [item for item in numbers_string.split(' ') if item != '']

        return card_num, card, numbers

    def match_num(self, card_num, card, numbers):
        num_of_matches = 0
        for n in numbers:
            if n in card:
                num_of_matches += 1
                self.multiplier_map[card_num + num_of_matches] += self.multiplier_map[card_num] 

        return
        

if __name__ == "__main__":
    sol = Solution()
    sol.scratchcards()