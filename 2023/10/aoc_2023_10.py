import sys
import re
from aoc_commons import file_reader
from aoc_commons import pretty_print

class Solution():
    grid = []
    start_loc = None
    starting_pipes = []

    pipe_chars = '|-LJ7F'
    # wrong_pipe_dirs = { # key is the direction u come from
    #     '|' :{'u': 'd','d': 'u'},
    #     '-' :{'l': 'r','r':'d'},
    #     'L' :{'u': 'r','r': 'u'},
    #     'J' :{'u': 'l','l': 'u'},
    #     '7' :{'d': 'l','l': 'd'},
    #     'F' :{'d': 'r','r': 'd'},
    # }
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
        print('start:', q)

        max_dist = 0
        traversed = []
        while len(q) > 0: 
            cur_pipe = q.pop(0) # remove from start of list
            cur_pipe_row, cur_pipe_col, cur_pipe_prev_dir, cur_pipe_dist = cur_pipe[0],cur_pipe[1],cur_pipe[2],cur_pipe[3]
            cur_pipe_char = self.grid[cur_pipe_row][cur_pipe_col]

            # This is calculating the result
            max_dist = max(max_dist, cur_pipe_dist)
            # This is when we check when we finished the game
            cur_loc = (cur_pipe_row, cur_pipe_col)
            if (cur_loc in traversed):
                break
            traversed.append(cur_loc)

            if (cur_pipe_char == 'S'):
                continue

            new_dir = self.pipe_dirs[cur_pipe_char][cur_pipe_prev_dir]


            new_dir_val = self.dirs[new_dir]

            new_pipe_row = cur_pipe_row + new_dir_val[0]
            new_pipe_col = cur_pipe_col + new_dir_val[1]
            
            new_pipe = (new_pipe_row, new_pipe_col, new_dir, cur_pipe_dist + 1) 

            q.append(new_pipe)

        print('q:',  q)
        print('max_dist: ', max_dist)
        return max_dist


    def pipe_maze(self):
        self.parse_input()
        # pretty_print.two_d_list(self.grid)
        
        self.step_1_find_s()
        self.step_1_5_find_starting_pipes()
        self.step_2_bfs_on_s()
        return


if __name__ == "__main__":
    sol = Solution()
    sol.pipe_maze()