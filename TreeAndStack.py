def isValid(s):
    #make something like a hashmap
    charDictionary = {}
    #then loop through string updating char key values
    for char in s:
        if char in charDictionary:
            charDictionary[char] += 1
        else:
            charDictionary[char] = 1
    #get list of diff values in dictionary (how many times each char appears)
    diffCharList = list(set(charDictionary.values()))
    #if only 1 char type, then valid
    if len(diffCharList) == 1:
        return "YES"    
    #try removing one of every type char, then see if every char frequency is the same
    for char in charDictionary:
        charDictionary[char] -= 1
        frequency = set(charDictionary.values())
        if len(frequency) == 1 and (0 in frequency or 1 in frequency):
            return "YES"
        charDictionary[char] += 1
    return "NO"

def isBalanced(s):
    #empty stack
    stack = []
    bracketDictionary = { ')': '(', '}': '{', ']': '['}
    #loop through string checking for balance
    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            #too many }]) brackets
            if not stack:
                return "NO"
            top_element = stack.pop()
            #wrong bracket, not balanced
            if bracketDictionary[char] != top_element:
                return "NO"
    if not stack:
        return "YES"
    #too many {[( brackets
    else:
        return "NO"

class Node:
    def __init__(self, intLabel, left = None, right = None):
        self.intLabel = intLabel
        self.left = left
        self.right = right
    
    # root left right
    def preOrder(self):
        nodeList = []
        #check if current node exists
        if self:
            nodeList.append(self.intLabel)
            #if left child exists, add to node list first (recursively loops)
            if self.left:
                nodeList.extend(self.left.preOrder())
            #right side children after left side
            if self.right:
                nodeList.extend(self.right.preOrder())
        return nodeList
    
    #left to right
    def inOrder(self):
        nodeList = []
        #check current node
        if self:
            #delay append, we get to bottom left before starting to append. code works from latest recursion call up
            if self.left:
                nodeList.extend(self.left.inOrder())
            nodeList.append(self.intLabel)
            if self.right:
                nodeList.extend(self.right.inOrder())
        return nodeList
    
    #bottom up
    def postOrder(self):
        nodeList = []
        #check current node
        if self:
            #append is the last part in recursion
            if self.left:
                nodeList.extend(self.left.postOrder())
            if self.right:
                nodeList.extend(self.right.postOrder())
            nodeList.append(self.intLabel)
        return nodeList

    def getHeight(self, value, height = 0):
        #checks at every node to see if it matches value we looking for
        if self.intLabel == value:
            return height
        #check left and right of every node and keep track of current height
        if self.left:
            leftHeight = self.left.getHeight(value, height + 1)
            if leftHeight != -1:
                return leftHeight
        if self.right:
            rightHeight = self.right.getHeight(value, height + 1)
            if rightHeight != -1:
                return rightHeight
        #can not find value return -1
        return -1

    def sumTree(self):
        if self is None:
            return 0
        nodeValues = self.preOrder()
        total = sum(nodeValues)
        return total