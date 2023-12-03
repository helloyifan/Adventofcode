import sys
import re

from aoc_commons import file_reader, pretty_print_2d_list

class Solution():

    map_of_data = []
    common_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '/', '?']
    ret = 0

    num_rows = None
    num_cols = None


    def gear_ratios(self):
        f = file_reader.read_file()
        self.create_map(f)


        pretty_print_2d_list.pretty_print(self.map_of_data)
        print("num_rows: ", self.num_rows)
        print("num_cols: ", self.num_cols)

        self.go_through_map()

        print(self.ret)

        return

    def create_map(self, f):
        for line in f:
            row = []
            for character in line: 
                if character == '\n': # Skip new line characters
                    continue

                row.append(character)

            if (not self.num_cols):
                self.num_cols = len(row)

            
            self.map_of_data.append(row)
        self.num_rows = len(self.map_of_data)
        return


    def go_through_map(self):
        for row_index, row_value in enumerate(self.map_of_data):
            print("row_index: ", row_index)
            col_index = 0
            while col_index < len(row_value):
                col_value = row_value[col_index] # Strongly dislike this, but dont know better way

                if col_value.isdigit():
                    num, num_digits = self.get_number_from_start(row_index, col_index)

                    # print(num, num_digits)

                    if self.number_around_letter(row_index, col_index, num_digits):
                        # print("num: ", num)
                        self.ret = self.ret +  num


                    # SKip over the indexs fro the number we just explored
                    col_index += num_digits
                else:
                    col_index += 1
        return


    def get_number_from_start(self, row_index, col_index):
        row = self.map_of_data[row_index]
        starting_col_index = col_index
        num_digits = 0

        while col_index < self.num_cols and row[col_index].isdigit():
            col_index = col_index + 1
            num_digits = num_digits + 1

        num_list = row[starting_col_index: col_index]
        num = int(''.join(num_list))
        return num, num_digits


    def number_around_letter(self, row, col, num_digits):

        # Check top
        if (row > 0):
            top_row = row - 1
            for top_col in range(col -1, col + num_digits + 1): # +1 to cover the diagonal cases
                # Fail fast if check doesn't make sense
                if top_col < 0 or top_col >= self.num_cols:
                    continue

                top_char = self.map_of_data[top_row][top_col]
                if self.check_if_symbol(top_char):
                    # print(top_row, ' ', top_col)
                    return True

        # check bottom
        if (row < self.num_rows - 1):
            bottom_row = row + 1
            for bottom_col in range(col -1, col + num_digits + 1):
                if bottom_col < 0 or bottom_col >= self.num_cols:
                    continue
                

                print(bottom_row, " " , bottom_col)
                bottom_char = self.map_of_data[bottom_row][bottom_col]
                if self.check_if_symbol(bottom_char):
                    # print(bottom_row, ' ', bottom_col)
                    return True

        # check left
        if (col > 0):
            left_col = col - 1 
            left_char = self.map_of_data[row][left_col]
            if self.check_if_symbol(left_char):
                # print(row, ' ', left_col)
                return True

        
        # check right
        if (col + num_digits <  self.num_cols):
            right_col = col + num_digits
            right_char = self.map_of_data[row][right_col]
            if self.check_if_symbol(right_char):
                # print(row, ' ', right_col)
                return True


        return False

    def check_if_symbol(self, char):
        if char in self.common_symbols:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    sol.gear_ratios()