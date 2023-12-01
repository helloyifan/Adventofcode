import heapq

class Solution:

    def calorieSum(self):
        cache = {}

        # So its just the max Stack question 
        maxHeap = []


        counter = 0
        rollingSum = 0

        f = open("input.txt", "r")
        for x in f:
            if (x == '\n'):  # line break
                cache[counter] = rollingSum

                heapq.heappush(maxHeap, rollingSum * -1)

                counter +=1
                rollingSum = 0

            else:
                rollingSum += float(x)
        
        print(cache)

        num1 = heapq.heappop(maxHeap) * -1
        num2 = heapq.heappop(maxHeap) * -1
        num3 = heapq.heappop(maxHeap) * -1
        print("num1: ", num1)
        print("num2: ", num2)
        print("num3: ", num3)

        sumNum = num1 + num2 + num3
        print("sumNum: ", sumNum)
        return None

sol = Solution()
sol.calorieSum()

