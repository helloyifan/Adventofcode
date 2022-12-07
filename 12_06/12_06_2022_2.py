from collections import defaultdict

class Solution():

    def test_input_runner(self):
        f = open("test_input_2.txt", "r")

        counter = 1
        for packet in f:
            print("---Test counter: ---", counter)
            self.main(packet)
            counter +=1 

    def part2_input_runner(self):
        f = open("input.txt", "r")
        packet = f.readline()
        self.main(packet)
    

    def main(self, packet):
        head = 0
        tail = 13
        cache = defaultdict(int)

        ## Init the sliding window

        for i in range(tail + 1): # +1 because its exclusive
            cache[packet[i]] += 1

        counter = 0
        while (not self.validate(cache) and tail < len(packet)):
            counter += 1
            tail += 1
            cache[packet[tail]] += 1
            cache[packet[head]] -= 1
            head += 1
        
        print("Tail: ", tail)
        print("Result: ", tail + 1 )
        
        return None


    def validate(self, cache):
        for key in cache:
            if (cache[key] != 1 and cache[key] != 0):
                return False
        return True



sol = Solution()
#sol.test_input_runner()
sol.part2_input_runner() 