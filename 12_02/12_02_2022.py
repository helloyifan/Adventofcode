
class Solution():
    def main(self):
        f = open("input.txt", "r")
        runningSum =0
        for x in f:
            pts = self.rockPaperScissorsPoints(x[0], x[2])
            print(pts)
            runningSum += pts

        print("RunningSum:", runningSum)
        return None

    def rockPaperScissorsPoints(self, p1, p2):
        pts = 0
        # You: X for Rock, Y for Paper, and Z for Scissors
        # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
        if (p2 == 'X'):
            pts += 1
            #Opponent: A for Rock, B for Paper, and C for Scissors
            # plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

            if (p1 == 'A'):
                pts += 3
            elif(p1 == 'B'):
                pts += 0
            elif(p1 == 'C'):
                pts += 6

        elif(p2 == 'Y'):
            pts += 2
            if (p1 == 'A'):
                pts += 6
            elif(p1 == 'B'):
                pts += 3
            elif(p1 == 'C'):
                pts += 0

        elif(p2 == 'Z'):
            pts += 3
            if (p1 == 'A'):
                pts += 0
            elif(p1 == 'B'):
                pts += 6
            elif(p1 == 'C'):
                pts += 3

        return pts

sol = Solution()
sol.main()