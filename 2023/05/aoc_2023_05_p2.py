import sys
import re
import copy
import json
from aoc_commons import file_reader


class Solution():
    seed_ranges = []
    parsed_input = {}

    ranges = {}

    def read_whole_file(self):
        input_lines = []

        input_category = []

        f = file_reader.read_file()
        for line in f:
            cur_line = line.strip()
            if cur_line == '':
                input_lines.append(input_category[:])
                input_category = []
            else:
                input_category.append(line.strip())

        input_lines.append(input_category[:])
        input_category = []
        
    
        for line in input_lines:
            if len(line) == 1: # special case for ['seeds: 79 14 55 13']
                seeds = [int(string) for string in line[0].split(' ')[1:]]
                
                ## part 2, build the seeds
                index = 0
                while index < len(seeds):
                    seed_range_entry = {
                        'range_start': seeds[index],
                        'range_end': seeds[index] + seeds[index + 1]
                    }
                    self.seed_ranges.append(seed_range_entry)
                    index += 2

            else:

                ret = []
                for row in line[1:]:
                    num_str_list = row.split(' ')

                    num_list = []
                    for num_str in num_str_list:
                        num_list.append(int(num_str))

                    ret.append(num_list)

                self.parsed_input[line[0]] = ret
    
        print('seed_ranges: ', self.seed_ranges)
        return

    def build_ranges(self):
        for map_key in self.parsed_input:
            list_of_ranges = []
            for encoded_range in self.parsed_input[map_key]:
                proper_range = {
                    'sr_start':  encoded_range[1],
                    'sr_end': encoded_range[1] + encoded_range[2],
                    'offset': encoded_range[0] - encoded_range[1] 
                }
                list_of_ranges.append(proper_range)
            self.ranges[map_key] = list_of_ranges
        return

    # Note the end isn't inclusive
    def check_range_inclosure(self, input_range, enclosing_ranges):
        ans = []
        print(input_range)
        for enclosing_range in enclosing_ranges:
            low = enclosing_range['sr_start']
            high = enclosing_range['sr_end']
            offset = enclosing_range['offset']

            i_start = input_range['range_start']
            i_end = input_range['range_end']

            if not (i_end < low or i_start > high):
                print('yeah ')
                ans.append({'range_start': max(i_start, low), 'range_end':min(i_end, high), 'offset': offset})
            # otherwise do we append with 0 offset?

        new_ranges = []
        # process the ans
        for i, interval in enumerate(ans):
            print('i', i)
            print('interval', interval)

        return 
    # This is really messed up, 
    # How do we iterate through all of the current level ranges and new ranges

    def check_seed_ranges(self, input_ranges, enclosing_ranges):
        new_ranges = []

        for input_range in input_ranges:
            cur_rets = self.check_range_inclosure(input_range, enclosing_ranges)
            if cur_rets:
                new_ranges.append(cur_rets)
        return new_ranges

    def process_seed_range(self, seed):
        r = self.ranges
        seed_to_soil = r['seed-to-soil map:']
        soil_to_fertilizer = r['soil-to-fertilizer map:']
        fertilizer_to_water = r['fertilizer-to-water map:']
        water_to_light = r['water-to-light map:']
        light_to_temperature = r['light-to-temperature map:']
        temperature_to_humidity = r['temperature-to-humidity map:']
        humidity_to_location = r['humidity-to-location map:']

        soil =  self.check_seed_ranges(seed,seed_to_soil )
    
        print(soil)
        return None # return Location


    def solution(self):
        self.read_whole_file()
        self.build_ranges()

        min_location = float('inf')

        location = self.process_seed_range(self.seed_ranges)
        # print(location)

        return

if __name__ == "__main__":
    sol = Solution()
    sol.solution()