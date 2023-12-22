from aoc_commons import file_reader, pretty_print, grid_stuff
from copy import copy, deepcopy

class Solution():
    grid = []
    galaxies = []
    max_row = 0
    max_col = 0
    # Step 1. Find all the galaxies
    # Step 2. offset for the empty rows and cols
    # Step 3. Do matrix distance math on every point to every ohter point

    def parse_input(self):
        f = file_reader.read_file_get_input_string()
        for line in f:
            line_list = [e for e in line]
            self.grid.append(line_list)
        return

    def step_1_find_all_galaxies(self):
        self.max_row = len(self.grid)
        self.max_col = len(self.grid[0])
        
        for ri, r in enumerate(self.grid):
            for ci, c in enumerate(r):
                if c == '#':
                    self.galaxies.append([ri, ci]) #Tuple doesnt allow re assingment, so using list
        return
    
    def step_2_offset_row_cols(self, magnitude):
        self.step_2_offset_row_helper(magnitude, self.max_row)
        self.step_2_flip_row_col_helper()
        self.step_2_offset_row_helper(magnitude, self.max_col)
        self.step_2_flip_row_col_helper()        
        return

    def step_2_offset_row_helper(self, magnitude, max_val):
        num_of_galaxies = len(self.galaxies)
        running_offset = 0 
        galaxies_offset_tracker = [0]* num_of_galaxies
        
        for i in range(0, max_val):
            if all(galaxy[0] != i for galaxy in self.galaxies):
                running_offset += magnitude

                for g_i, g_e in enumerate(self.galaxies):
                    if g_e[0] > i:
                        galaxies_offset_tracker[g_i] += magnitude
        for i, e in enumerate(galaxies_offset_tracker):
            cur_galaxy = self.galaxies[i]
            cur_galaxy[0] += e
        return

    def step_2_flip_row_col_helper(self):
        for galaxy in self.galaxies:
            temp = galaxy[0]
            galaxy[0] = galaxy[1]
            galaxy[1] = temp
        
    def step_3_matrix_maths(self):
        running_sum = 0
        for i, start_galaxy in enumerate(self.galaxies):
            for j in range(i, len(self.galaxies)):
                end_galaxy = self.galaxies[j]
                cursum = 0
                cursum += abs(start_galaxy[0] - end_galaxy[0]) #row index
                cursum += abs(start_galaxy[1] - end_galaxy[1]) #col index
                running_sum+= cursum
        print('running: sum', running_sum)
        return running_sum



    def cosmic_expansion(self):
        self.parse_input()
        self.step_1_find_all_galaxies()
        self.step_2_offset_row_cols(1000000 - 1) #because its replace, but we dont remove existing in our code
        self.step_3_matrix_maths()
        return

if __name__ == "__main__":
    sol = Solution()
    sol.cosmic_expansion()
