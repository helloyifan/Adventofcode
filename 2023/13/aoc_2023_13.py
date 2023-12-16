import sys

class Solution():
    mirror_maps = []

    def parse_input(self):
        with open(sys.argv[1]) as fin:
            lines = fin.read().strip().split('\n')
        return lines
    
    def process_input(self, lines):
        cur_map = []
        for i, e in enumerate(lines):
            if all( char == ' ' for char in e):
                self.mirror_maps.append(cur_map.copy())
                cur_map = [] # reset it
            else:
                cur_map.append(e)

        self.mirror_maps.append(cur_map.copy())
        return

    def point_of_incidence(self):
        lines = self.parse_input()
        self.process_input(lines)

        for mirror_map in self.mirror_maps:
            # self.grid_print(mirror_map)

            normal_map = mirror_map
            flipped_map = list(zip(*normal_map[::-1]))

            self.process_horizational(normal_map)
            self.process_horizational(flipped_map)




        return

    def process_horizational(self, mirror_map):
        for i in range(1, len(mirror_map) -1): # we do 1 and -1 because we dont wanna check edges, this seems prone to error
            matches = self.check_mirror_horizontal(mirror_map, i)
            if (matches):
                print("done: ", i )
                break
            
    def check_mirror_horizontal(self, mirror_map, mirror_loc):
        matches = True
        for i in range(0, mirror_loc + 1):
            left_check = mirror_loc - i
            right_check = mirror_loc + i + 1

            if left_check < 0:
                print('left_check < 0')
                break
            elif right_check >= len(mirror_map):
                print('right_check > len(mirror_map)')
                break

            if mirror_map[left_check] != mirror_map[right_check]:
                matches = False
                break
            # elif mirror_map[left_check] == mirror_map[right_check]:
                # print("matches: ", mirror_loc, i , mirror_map[left_check],  mirror_map[right_check])

        return matches

    def grid_print(self, lines):
        for l in lines:
            print(l)
        return


if __name__ == '__main__':
    sol = Solution()
    sol.point_of_incidence()