import sys

class Solution():

    def parse_input(self):
        with open(sys.argv[1]) as fin:
            lines = fin.read().strip().split('\n')
        return lines

    def process_input(self, lines):
        input_lines = []
        for line in lines:
            input_lines.append([ int(num) for num in line.split(' ')])
        return input_lines

    def mirage_maintenance(self):
        lines = self.parse_input()
        input_lines = self.process_input(lines)

        running_sum = 0
        for i, e in enumerate(input_lines):
            running_sum += self.build_prediction(e)

        print("Final Ret: ", running_sum)
        return 

    def build_prediction(self, line):
        prediction = []
        prediction.append(line)
        q_index = 0
        
        all_zero = False
        while not all_zero:
            new_line = []
            cur_list = prediction[q_index]
            for i, num in enumerate(cur_list):
                if i < (len(cur_list) - 1): # -1 because we wanna skip last index
                    new_line.append(cur_list[i + 1] - cur_list[i])

            all_zero = all(i == 0 for i in new_line)
            prediction.append(new_line)
            q_index += 1
        
        return self.extrapolate(prediction)
            
    def extrapolate(self, prediction):
        running_sum = 0
        for i, e in enumerate(prediction):
            running_sum += e[-1]
        return running_sum

        

if __name__ == '__main__':
    sol = Solution()
    sol.mirage_maintenance()
