import sys
from collections import defaultdict 
from functools import cmp_to_key

## Plan

# step 1: create ds [ 12, 11, 10] convert Q to 12, J to 0 etc

# step 2 label matching types, : { type: "Two Pair", [10, 10, 11, 11, 1] }

# step 2.1: process the J, if the J is not a part of the current type, then you can increase the type

# step 3: write sorting lambda function

# step 4: calculae winning

class Solution: 

    ds = []

    def parse_input(self):
        with open(sys.argv[1]) as fin:
            lines = fin.read().strip().split("\n")
        return lines

    def step_1_take_input(self, lines):
        card_values = { 'T': 10, 'J': 0, 'Q': 12, 'K': 13, 'A': 14}

        for l in lines:
            cards_string, wager = l.split(' ')[0], int(l.split(' ')[1])
            cards = [card_values[i] if i in card_values else int(i) for i in cards_string ]
            ds = {
                'type': None,
                'cards': cards,
                'wager': wager
            }

            self.ds.append(ds)
        return
    
    def step_2_set_type(self):
        for i, val in enumerate(self.ds):
            # iterate through cards
            cards = val['cards']

            current_memory = defaultdict(int)
            for card in cards:
                current_memory[card] += 1 

            # sorted_dict_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
            sorted_current_memory = dict(sorted(current_memory.items(), key=lambda i: -i[1]))

            type = None
            occurance_sets = [ e for i, e in sorted_current_memory.items()]
            if occurance_sets[0] == 5:
                type = 7 # 'Five of a kind'
            elif occurance_sets[0] == 4:
                type = 6 #'Four of a kind'
            elif occurance_sets[0] == 3 and occurance_sets[1] == 2:
                type = 5 #'Full house'
            elif occurance_sets[0] == 3:
                type = 4 #'Three of a kind'
            elif occurance_sets[0] == 2 and occurance_sets[1] == 2:
                type = 3 # 'Two pair'
            elif occurance_sets[0] == 2:
                type = 2 # 'One pair'
            else:
                type = 1 #'High card'

            self.ds[i]['type'] = type
        return
    
    def step_2_1_process_j(self):
        for i, val in enumerate(self.ds):
            num_of_j = val['cards'].count(0)

            if num_of_j > 0: 
                cur_type = val['type']    
                new_type = cur_type
                if cur_type == 7: # Five of a kind
                    continue
                elif cur_type == 6: # Four of a kind
                    if num_of_j == 4 or num_of_j == 1: 
                        new_type = 7
                elif cur_type == 5: # Full house
                    # If there are 2 J's we go to  five of a kind
                    if num_of_j == 2 or num_of_j == 3: 
                        new_type = 7
                elif cur_type == 4: # Three of a kind
                    if num_of_j == 3 or num_of_j == 1:
                        new_type = 6
                elif cur_type == 3: # Two pair
                    # If there a J in two pair, its still a 3 of a kind
                    if num_of_j == 1:                
                        new_type = 5
                    # If there are two J and a two pair, its 4 of a kind
                    elif num_of_j == 2:
                        new_type = 6
                elif cur_type == 2: # pair
                    # from one pair, you can go to two pair
                    # of you can go two, 3 of a kind, which you would always do

                    # if the pair is 'j' then its also 3 of a kind
                    new_type = 4
                    
                elif cur_type == 1: # high 
                    new_type = 2   

                val['type'] = new_type
        return



    def sorting_helper(self, item1, item2):
        if item1['type'] == item2['type']:
            card1, card2 = item1['cards'], item2['cards']
            for i in range(0, len(item1['cards'])):
               if card1[i] > card2[i]:
                   return -1
               elif card1[i] < card2[i]:
                   return 1
               else:
                   continue
            return 1
                   
        return -1 if item1['type'] > item2['type'] else 1 

    def step_3_sort(self):        
        custom_key = cmp_to_key(self.sorting_helper) 
        self.ds = sorted(self.ds, key=custom_key)
        return

    def step_4_calculate_winnings(self):
        len_of_ds = len(self.ds)
        ret = 0
        for i, e in enumerate(self.ds):
            multiplier = len_of_ds - i
            ret += (multiplier) * e['wager']
            
        return ret
    def camel_cards(self):
        lines = self.parse_input()
        self.step_1_take_input(lines)
        self.step_2_set_type()
        self.step_2_1_process_j()
        self.step_3_sort()

        self.debug_printer_for_j()
        ret = self.step_4_calculate_winnings()
        print(ret)
        return 

    def debug_printer(self):
        for i, e in enumerate(self.ds):
            print('type:', e['type'], ' cards: ', e['cards'] )
        return
    
    def debug_printer_for_j(self):
        for i, e in enumerate(self.ds):
            if 0 in e['cards']:
                print('type:', e['type'], ' cards: ', e['cards'] )
        return
if __name__ == "__main__":
    sol = Solution()
    sol.camel_cards()


## P2 Shame
    # 254890761 too high
    # 254250996
    # 254443938 too high
    # 254461928
    # 254083736 is answer