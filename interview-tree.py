'''
    Created on Sep 26, 2015
    
    @author: lanasu
    '''
import collections
from collections import deque
import math

#This takes in an input value to determine what depth of tree to create
depth = int(input("Please enter the depth of tree (> 1):  "))
nodeArray = []
originalDepth = depth
nodeJ = 3

nodeList = []

#Defines the node of a binary tree
class Node:
    def __init__(self, value, level):
        
        self.left = None
        self.right = None
        self.value = value
        self.level = level
    
    def __str__(self):
        return str(self.value)

    #Creates a default tree
    def insert(self,value):
        if (self.left) is None:
            self.value = value
            self.level = 1
            self.left = Node(1,2)
        if (self.right) is None:
            self.right = Node(1,2)
        
        self._insert(self.left, self.right, depth-2)
    
    def defArray(self):
        n = len(nodeArray)
        for i in range(0, n):
            print(str(i)+' '+str(nodeArray[i].value))

    #Local method that recursively creates the tree for a given depth
    def _insert(self, leftNode, rightNode, depth):
        if(depth==0): return None
        leftNode.left = Node(0, originalDepth-depth+1)
        leftNode.right = Node(0, originalDepth-depth+1)
        rightNode.left = Node(0, originalDepth-depth+1)
        rightNode.right = Node(0, originalDepth-depth+1)
        
        self._insert(leftNode.left, leftNode.right, depth-1)
        self._insert(rightNode.left, rightNode.right, depth-1)
    
    #This process is copied from a code found on the internet and then customized        
    #Prints the tree in layers
    def iterLayers(self):
        q = deque()
        q.append(self)
        def layerIterator(layerSize):
            for i in range(layerSize):
                n = q.popleft()
                if n.left: 
                    q.append(n.left)
                if n.right: 
                    q.append(n.right)
                yield n.value
        
        while (q):
            yield layerIterator(len(q))
    
    def printByLayer(self):
        for layer in self.iterLayers():
            
            print (' '.join([str(v) for v in layer]))

    #Initializes first two layers of the tree
    def populateTree(self):
        nodeArray[0].value = 1
        nodeArray[1].value = 1
        nodeArray[2].value = 1
        nodeArray[3].value = 1
        self._populateTree(depth-2, nodeJ)
        self._rearrange()

    #When an array is created, it starts from 0, but because BFS starts with 1, this is used to manipulate the array
    def _rearrange(self):
        n = len(nodeArray)
        for i in range (1, n):
            nodeArray[i-1].value = nodeArray[i].value

    #Recursively updates the node values, going layer by layer
    def _populateTree(self, depth, nodeJ):
        if(depth==0): return None
        n = int(math.pow(2,(originalDepth-depth)))
        for i in range(0, n):
            nodeJ=nodeJ+1
            #Sets the left-most nodes of the tree to value 1
            if(i==0):
                nodeArray[nodeJ].value = 1
            #Sets the right-most nodes of the tree to value 1
            elif(i==n-1):
                nodeArray[nodeJ].value = 1
            #Sets the values of all other nodes 
            else:
                nodeArray[nodeJ].value = nodeArray[int((nodeJ-1)/2)].value + nodeArray[int((nodeJ+1)/2)].value
        
        self._populateTree(depth-1, nodeJ)

#This process is also copied from a code found on the internet and then customized
#Breath first traversal
#Traveses the tree and gets all the nodes in an array where the array is populated with required logic
def BFT(node):
    
    node.level = 1
    queue = deque([node])
    #    output = []
    current_level = node.level
    
    while len(queue)>0:
        
        current_node = queue.popleft()
        
        if(current_node.level > current_level):
            #              output.append("\n")
            current_level += 1
        
        nodeArray.append((current_node))
        
        if current_node.left != None:
            current_node.left.level = current_level + 1 
            queue.append(current_node.left) 
        
        if current_node.right != None:
            current_node.right.level = current_level + 1 
            queue.append(current_node.right)
    
    nodeArray.append(Node(0,originalDepth))             


tree = Node(1,1)
tree.insert(1)
BFT(tree)
tree.populateTree()
tree.iterLayers()
tree.printByLayer()


