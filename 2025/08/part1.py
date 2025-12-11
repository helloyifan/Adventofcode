import sys

class Solution():
    def solve(self):

        input = read_file_get_input_string()

        ds = {}
        self.parseInput(input, ds)

        ncoords = len(ds)

        visited = []

        matrix = []
        for x in range(ncoords):
            print(x)
            for y in range(x+1, ):
                if x == y:
                   continue
                         
                # if (y,x) in visited:
                #     continue

                xVal = ds[x]
                yVal = ds[y]
                e = euclidean_distance_3d(xVal, yVal)

                matrix.append(((x,y), e))
                visited.append((x,y))
        
        # Sort the matrix by e

        matrix.sort(key=lambda x:x[1])

        # We only need the 10 shortest connections

        shortest10 = matrix[:1000]
        print(shortest10)
        n = len(ds)
        dsu = DSU(n)

        # for itemI
        for ele in shortest10:
            x = ele[0][0]
            y = ele[0][1]
            print('x:', x, 'y',y)
            dsu.union(x, y)

        components = {}

        for i in range(n):
            root = dsu.find(i)
            components[root] = dsu.size[root]


        finRet = []
        for key in  components:
            finRet.append((key,components[key]))

        finRet.sort(key=lambda x:-x[1]) #Sort by largest to smallest
        print(finRet)

        finVal = finRet[0][1] * finRet[1][1] * finRet[2][1] 
        print('Fin Val: ', finVal)
        return
    

    def parseInput(self, input, ds):

        for i,e in enumerate(input):
            coords = e.split(',')
            ds[i] = {'x': int(coords[0]), 'y': int(coords[1]), 'z': int(coords[2])}
            #ds[i] = (coords[0], coords[1], coords[2])
        return

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        # union by size
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]

def euclidean_distance_3d(p1, p2):
    dx = p1['x'] - p2['x']
    dy = p1['y'] - p2['y']
    dz = p1['z'] - p2['z']

    return (dx**2 + dy**2 + dz**2)**0.5

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