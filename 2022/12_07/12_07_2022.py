class TreeNode:
    def __init__(self, sym='u missed a sym dumbass', size=0, parent=None):
        self.sym = sym
        self.size = size
        self.children = {}
        self.parent = parent

class Solution():
    def main(self):
        f = open("input.txt", "r")
        root = self.buildTree(f)
        # self.treePrinter(root)

        finalResult = {'sumUnderTarget':0}
        self.treeSummer(root, finalResult)

        print(finalResult)
        return None

    def buildTree(self, f):
        f.readline() #disregard first '/' lol

        tree = TreeNode('/')
        root = tree

        for line in f:
            lineInput = line.strip().split(' ')
            if (lineInput[0] == '$'):
                # Could be cd
                if (lineInput[1] == 'cd'):
                    if (lineInput[2] == '..'):
                        tree = tree.parent
                    else: # Basically if its the name of a thing
                        tree = tree.children[lineInput[2]]

            elif (lineInput[0] == 'dir'):
                # make node
                tree.children[lineInput[1]] = TreeNode(lineInput[1], 0, tree)
            
            elif (lineInput[0].isnumeric()):
                # make leaf node
                tree.children[lineInput[1]] = TreeNode(lineInput[1], int(lineInput[0]), tree)

        return root
    
    def treePrinter(self, treeNode, ret):
        if (treeNode == None):
            return

        print("----")
        print("sym:", treeNode.sym)
        print("size:", treeNode.size)

        for key in treeNode.children:
            childNode = treeNode.children[key]
            self.treePrinter(childNode)
        
        return None
    
    
    def treeSummer(self, treeNode, finalResult):
        if (treeNode == None):
            return
        
        runningSum = treeNode.size
        for key in treeNode.children:
            childNode = treeNode.children[key]
            runningSum += self.treeSummer(childNode, finalResult)
        
        if (runningSum> 0 and runningSum < 100000 and len(treeNode.children) > 0): # len(treeNode.children) > 0 because 'find all of the directories with a total size of at most 100000'
            print(runningSum)
            finalResult['sumUnderTarget'] += runningSum

        return runningSum
    




sol = Solution()
sol.main()