from aoc_commons import file_reader, pretty_print, grid_stuff
from copy import copy, deepcopy

class Solution():
    grid = []
    galaxies = []
    # Step 1. Add in empty spaces
    # Step 2. Find all the galaxies
    # Step 3. Do matrix distance math on every point to every ohter point

    def parse_input(self):
        f = file_reader.read_file_get_input_string()
        for line in f:
            line_list = [e for e in line]
            self.grid.append(line_list)
        return

    def step_1_add_in_empty_spaces(self):
        self.grid = self.step_1_add_empty_rows_helper(self.grid)

        # vertical (so rotate)
        self.grid= grid_stuff.rotate_matrix(self.grid)
        self.grid = self.step_1_add_empty_rows_helper(self.grid)
        self.grid = grid_stuff.rotate_matrix_counterclockwise(self.grid)

    def step_1_add_empty_rows_helper(self, given_grid):
        new_grid = []
        # horizontal
        for row in given_grid:
            if all(char == '.' for char in row):
                new_grid.append(copy(row)) #copy only copies reference if its list of lists
            new_grid.append(copy(row))
        return deepcopy(new_grid) # deepcopy meansthe lists in the list is new (not refs)

    def step_2_find_all_galaxies(self):
        for ri, r in enumerate(self.grid):
            for ci, c in enumerate(r):
                if c == '#':
                    self.galaxies.append((ri, ci))
        return

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
        self.step_1_add_in_empty_spaces()
        # pretty_print.two_d_list(self.grid)
        self.step_2_find_all_galaxies()
        print(self.galaxies)
        self.step_3_matrix_maths()
        return

if __name__ == "__main__":
    sol = Solution()
    sol.cosmic_expansion()
