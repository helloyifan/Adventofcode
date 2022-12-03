
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
        # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
        if (p2 == 'X'): # We need to lose
            pts += 0
            #Opponent: A for Rock, B for Paper, and C for Scissors
            # plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

            if (p1 == 'A'): # We need to play Scissor which is 3
                pts += 3
            elif(p1 == 'B'): # We need to play Rock which is 1
                pts += 1
            elif(p1 == 'C'):  # We need to play Paper which is 2
                pts += 2

        elif(p2 == 'Y'):  # we need to draw
            pts += 3
            if (p1 == 'A'): # We need to play rock
                pts += 1
            elif(p1 == 'B'): # we need it play paper
                pts += 2
            elif(p1 == 'C'): # we need to play scissor
                pts += 3

        elif(p2 == 'Z'): # we need to win
            pts += 6
            if (p1 == 'A'): #We need to play paper
                pts += 2
            elif(p1 == 'B'): # We need to play scissor
                pts += 3
            elif(p1 == 'C'): # we heed to play rock
                pts += 1

        return pts

sol = Solution()
sol.main()