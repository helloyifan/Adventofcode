import sys
import re
from aoc_commons import file_reader
from aoc_commons import pretty_print
import copy

class Solution():
    grid = []
    grid_copy = []
    start_loc = None
    starting_pipes = []
    traversed = []
    pipe_chars = '|-LJ7F'

    pipe_dirs = { # key is the direction that we WERE going
        '|' :{'u': 'u','d': 'd'},
        '-' :{'l': 'l','r':'r'},
        'L' :{'d': 'r','l': 'u'},
        'J' :{'d': 'l','r': 'u'},
        '7' :{'u': 'l','r': 'd'},
        'F' :{'u': 'r','l': 'd'},
    }
    dirs = {
        'd': (1, 0),
        'u': (-1, 0),
        'r': (0, 1),
        'l':  (0, -1)
    }

    # Step 1. Find S
    # Step 1.5 find pipes for S
    # Step 2. BFS on S, 
    #   - keep track of visited
    #   - Left and right should meet up at the same sport
    # Step 3. Ray casting algo (point in polygon)
    #   - cast a ray to the left and see how many times it intersects a wall
    #   - even number means its outside of the shape (including 0)
    #   - odd number means its inside of the shape

    def parse_input(self):
        f = file_reader.read_file_get_input_string()
        for line in f:
            line_list = [e for e in line]
            self.grid.append(line_list)
        return

    def step_1_find_s(self):
        for r_i, r_e in enumerate(self.grid):
            for c_i, c_e in enumerate(r_e):
                if c_e == 'S':
                    self.start_loc = (r_i, c_i)
                    # BTW WE TRAVERSED S
                    self.traversed.append(self.start_loc)
                    self.grid[self.start_loc[0]][self.start_loc[1]] = '|'
                    return
    
    def step_1_5_find_starting_pipes(self):
        row, col = self.start_loc[0], self.start_loc[1]
        for k, d in self.dirs.items():
            e = (row + d[0], col + d[1])
            if e[0] < 0 or e[0] >= len(self.grid):
                continue
            if e[1] < 0 or e[1] >= len(self.grid[0]):
                continue
            
            e_char = self.grid[e[0]][e[1]]
            if e_char in self.pipe_dirs:
                if k in self.pipe_dirs[e_char]:
                    self.starting_pipes.append((e[0], e[1], k, 1))
        return

    def step_2_bfs_on_s(self):
        q = []
        q.extend(self.starting_pipes)

        max_dist = 0
        while len(q) > 0: 
            cur_pipe = q.pop(0) # remove from start of list
            cur_pipe_row, cur_pipe_col, cur_pipe_prev_dir, cur_pipe_dist = cur_pipe[0],cur_pipe[1],cur_pipe[2],cur_pipe[3]
            cur_pipe_char = self.grid[cur_pipe_row][cur_pipe_col]

            # This is calculating the result
            max_dist = max(max_dist, cur_pipe_dist)
            # This is when we check when we finished the game
            cur_loc = (cur_pipe_row, cur_pipe_col)
            if (cur_loc in self.traversed):
                break

            self.traversed.append(cur_loc)

            self.grid_copy[cur_pipe_row][cur_pipe_col] = '#'

            new_dir = self.pipe_dirs[cur_pipe_char][cur_pipe_prev_dir]


            new_dir_val = self.dirs[new_dir]

            new_pipe_row = cur_pipe_row + new_dir_val[0]
            new_pipe_col = cur_pipe_col + new_dir_val[1]
            
            new_pipe = (new_pipe_row, new_pipe_col, new_dir, cur_pipe_dist + 1) 

            q.append(new_pipe)


        return max_dist

    def step_3_ray_cast_caller(self):
        cell_in_shape = 0
        for row_i, row_e in enumerate(self.grid):
            for col_i, col_e in enumerate(row_e):
                if (row_i == 19 and col_i == 94):
                    print("god damn")

                if((row_i, col_i) not in self.traversed):
                    if self.step_3_ray_cast_helper(row_i, col_i):


                        print((row_i, col_i))
                        cell_in_shape += 1

        print("cell_in_shape: ", cell_in_shape)
        return cell_in_shape
    
    # We will ray cast to from left to right for simplicity 
    def step_3_ray_cast_helper(self, row, col):
        max_col = len(self.grid[0])
        chars_to_watch = {'|', 'J', 'L'}

        num_of_intersection = 0
        for i in range(col, max_col):
            if((row, i) in self.traversed and self.grid[row][i] in chars_to_watch):
                num_of_intersection += 1

        return num_of_intersection % 2 == 1 # odd means inside the shape

    def pipe_maze(self):
        self.parse_input()
        # pretty_print.two_d_list(self.grid)
        
        self.grid_copy = copy.deepcopy(self.grid)

        self.step_1_find_s()

        self.step_1_5_find_starting_pipes()
        self.step_2_bfs_on_s()

        self.step_3_ray_cast_caller()
        # pretty_print.two_d_list(self.grid_copy)
        return


if __name__ == "__main__":
    sol = Solution()
    sol.pipe_maze()

# cell_in_shape:  5762 is too high (whoops i counted for outside instead of inside)
# cell_in_shape:  405 is too high 
# cell_in_shape: 381
