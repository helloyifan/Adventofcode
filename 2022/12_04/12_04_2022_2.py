
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

            if (self.existOverlap(xStart, xEnd, yStart, yEnd) or 
                self.existOverlap(yStart, yEnd, xStart, xEnd)):

                print("xStart: ", xStart)
                print("xEnd: ", xEnd)
                print("yStart: ", yStart)
                print("yEnd: ", yEnd)
                print('---')
                rollingSum += 1

        print("rollingSum:", rollingSum)
        return None

    def existOverlap(self, start1, end1, start2, end2):
        if( (start1 <= start2) and (end1 >= start2)):
            return True
        elif( (start1 <= end2) and (end1 >= end2)):
            return True
        else:
            return False

sol = Solution()
sol.main()