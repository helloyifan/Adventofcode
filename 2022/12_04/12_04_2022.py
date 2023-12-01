
class Solution():

    def main(self):
        rollingSum = 0
        f = open("input.txt", "r")
        for row in f:
            x, y = row.split(',')
            xStart, xEnd = x.split('-')
            xStart = int(xStart)
            xEnd = int(xEnd)
            
            yStart, yEnd = y.split('-')
            yStart = int(yStart)
            yEnd = int(yEnd)

            if (self.fullyContained(xStart, xEnd, yStart, yEnd)):
                print("xStart: ", xStart)
                print("xEnd: ", xEnd)
                print("yStart: ", yStart)
                print("yEnd: ", yEnd)

                rollingSum += 1

        print("rollingSum:", rollingSum)
        return None

    def fullyContained(self, xStart, xEnd, yStart, yEnd):
        if ( (xStart <= yStart) and (xEnd >= yEnd)):
            return True
        elif((yStart <= xStart) and (yEnd >= xEnd)):

            return True
        else:
            return False

sol = Solution()
sol.main()