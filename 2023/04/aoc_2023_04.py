import sys
import re
from aoc_commons import file_reader

#  python3 -m 01.aoc_2023_01 01/input.txt

class Solution():
    
    p1_ret = 0

    def scratchcards(self):
        f = file_reader.read_file()

        for line in f:
            card, numbers = self.parse_input(line)
            self.match_num(card, numbers)

        print('p1_ret: ', self.p1_ret)
        return

    def parse_input(self, line):
        card_and_numbers = line.split(':')[1].strip()
        card_string = card_and_numbers.split('|')[0].strip()
        numbers_string = card_and_numbers.split('|')[1].strip()
        
        card = [item for item in card_string.split(' ') if item != '']

        numbers = [item for item in numbers_string.split(' ') if item != '']

        return card, numbers

    def match_num(self, card, numbers):
        pow_of_2 = -1 

        for n in numbers:
            if n in card:
                pow_of_2 += 1


        if pow_of_2 != -1:
            self.p1_ret += 2**pow_of_2
            
        return
        

if __name__ == "__main__":
    sol = Solution()
    sol.scratchcards()