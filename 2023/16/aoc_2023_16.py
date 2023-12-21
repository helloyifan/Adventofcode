import sys
import re
from aoc_commons import file_reader
from aoc_commons import pretty_print

class Solution():
 
    grid = [] # y, x
    grid_y_size = None
    grid_x_size = None
    walked = []

    # Direction
    # 0: up
    # 1: right
    # 2: down
    # 3: left

    def floor_will_be_lava(self):
        f = file_reader.read_file_get_input_string()

        self.setup_grid_and_walked(f)
        
        print(pretty_print.two_d_list(self.grid))
        print(pretty_print.two_d_list(self.walked))

        self.move([0,0], 1) # 1 is right

        print('Done: ')
        print(pretty_print.two_d_list(self.walked))
        return

    def setup_grid_and_walked(self, f):
        self.grid_y_size = len(f)
        self.grid_x_size = len(f[0])


        for line in f:
            t = [char for char in line]
            w = ['.' for char in line]
            self.grid.append(t)
            self.walked.append(w)

    def move(self, loc, dir):
        # set grid/walked
        print('start_loc: ', loc)

        self. walked[loc[1]][loc[0]] = '#'

        moved = None
        if dir == 0:
            moved = self.move_up(loc)
        elif dir == 1:
            moved = self.move_right(loc)
        elif dir == 2:
            moved = self.move_down(loc)
        elif dir == 3:
            moved = self.move_left(loc)        
        if moved == False:
            return

        # handle next move
        y = loc[1]
        x = loc[0]

        print('moved_loc: ', loc, 'dir', dir)

        cur_grid_symbol = self.grid[y][x] 
        if cur_grid_symbol == '/':
            dir_mapping = {0: 1, 1: 0, 2: 3, 3: 2}
            new_dir = dir_mapping.get(dir)
            if new_dir is not None:
                self.move(loc, new_dir)
        elif cur_grid_symbol == '\\':
            dir_mapping ={0: 3, 3:0, 1:2, 2: 1}
            new_dir = dir_mapping.get(dir)
            if new_dir is not None:
                self.move(loc, new_dir)
        elif cur_grid_symbol == '|':
            if dir == 1 or dir == 3:
                self.move(loc, 0)
                self.move(loc, 2)
        elif cur_grid_symbol == '-':
            if dir == 0 or dir == 2:
                self.move(loc, 1)
                self.move(loc, 3)
        else:
            self.move(loc, dir)

        return
    
    def move_down(self, loc):
        if (loc[0] + 1 >= self.grid_y_size):
            return False
        loc[0] += 1
        return True
    
    def move_up(self, loc):
        if (loc[0] < 0):
            return False
        loc[0] -= 1
        return True

    def move_right(self, loc):
        if (loc[1] >= self.grid_x_size):
            return False
        loc[1] += 1
        return True

    def move_left(self, loc):
        if (loc[1] < 0):
            return False
        loc[1] -= 1
        return True



if __name__ == "__main__":
    sol = Solution()
    sol.floor_will_be_lava()