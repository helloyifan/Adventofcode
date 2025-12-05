
import sys

class Solution():
    def solve(self):
        input = read_file_get_input_string()

        temp = self.processInput(input)
        ranges = temp['ranges']
        ingredients = temp['ingredients']
        processedRanges = self.processedRanges(ranges)

        processedRanges.sort(key=lambda d: d['start'])


        
        # Stack Processing
        s = [processedRanges[0]]

        for i, e in enumerate(processedRanges[1:]):
        
            if e['start'] <= s[-1]['end']:
                if e['end'] > s[-1]['end']:
                    s[-1]['end'] = e['end']
                else:
                    print('this value is legit just smaller then the prev val lol')                    
            else:
                s.append(e)

        finRet = 0
        # Sum up the ranges
        for i in s:
            finRet += i['end'] - i['start'] + 1 # +1 becaues 3-5 has 3 values and 10-20 has 11 values fuck you it makes sense


        print('finRet: ', finRet)
 


        return
    
    def processInput(self, input):
        # Find middle
        gapIndex = 0
        for i, e in enumerate(input):
            if e == '':
                gapIndex = i
         
        ranges = input[:gapIndex]
        ingredients = input[gapIndex+1:]
        return {'ranges': ranges, 'ingredients': ingredients }
    
    def processedRanges(self, ranges):
        ret = []
        for r in ranges:
            startEndList = r.split('-')
            ret.append({'start': int(startEndList[0]),'end': int(startEndList[1]) })
        return ret

def read_file():
    if len(sys.argv) != 2:
        print("Pass in a file name (and only the filename)")
        sys.exit(1)

    file_name = sys.argv[1]
    file = open(file_name, "r")
    return file

def read_file_get_input_string():
    return read_file().read().strip().split('\n')



sol = Solution()
sol.solve()