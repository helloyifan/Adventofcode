import sys
import re
import copy
import json
from aoc_commons import file_reader


class Solution():
    seeds = []
    parsed_input = {}

    ranges = {
    }

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

        # humidity-to-location map:    
        input_lines.append(input_category[:])
        input_category = []
        
    
        for line in input_lines:
            if len(line) == 1: # special case for ['seeds: 79 14 55 13']
                seeds = line[0].split(' ')
                self.seeds = [int(seed) for seed in seeds[1:]]
            else:

                ret = []
                for row in line[1:]:
                    num_str_list = row.split(' ')

                    num_list = []
                    for num_str in num_str_list:
                        num_list.append(int(num_str))

                    ret.append(num_list)

                self.parsed_input[line[0]] = ret

        # print(self.parsed_input)

        return


    def build_ranges(self):
        for map_key in self.parsed_input:
            list_of_ranges = []
            for encoded_range in self.parsed_input[map_key]:
                proper_range = {
                    'dr_start':  encoded_range[0],
                    'dr_end': encoded_range[0] + encoded_range[2],
                    'sr_start':  encoded_range[1],
                    'sr_end': encoded_range[1] + encoded_range[2],
                    'offset': encoded_range[0] - encoded_range[1] 
                }
                list_of_ranges.append(proper_range)
            self.ranges[map_key] = list_of_ranges


        # print(self.ranges)
        # print(json.dumps(self.ranges, indent=2))
        return

    def check_ranges(self, val, ranges):
        for r in ranges:
            if r['sr_start'] <= val and val <= r['sr_end']:
                return val + r['offset']

        return val


    def process_seed(self, seed):
        r = self.ranges
        seed_to_soil = r['seed-to-soil map:']
        soil_to_fertilizer = r['soil-to-fertilizer map:']
        fertilizer_to_water = r['fertilizer-to-water map:']
        water_to_light = r['water-to-light map:']
        light_to_temperature = r['light-to-temperature map:']
        temperature_to_humidity = r['temperature-to-humidity map:']
        humidity_to_location = r['humidity-to-location map:']

        soil =  self.check_ranges(seed,seed_to_soil )
        fertilizer =  self.check_ranges(soil, soil_to_fertilizer )
        water = self.check_ranges(fertilizer, fertilizer_to_water )
        light = self.check_ranges(water, water_to_light)
        temperature = self.check_ranges(light, light_to_temperature)
        humidity = self.check_ranges(temperature, temperature_to_humidity)
        location = self.check_ranges(humidity, humidity_to_location)

        print(f"soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}")
        return location

    def solution(self):
        self.read_whole_file()
        self.build_ranges()

        min_location = float('inf')
        for seed in self.seeds:
            location = self.process_seed(seed)
            min_location = min(min_location, location)

        print('min_location: ', min_location)

        return

if __name__ == "__main__":
    sol = Solution()
    sol.solution()