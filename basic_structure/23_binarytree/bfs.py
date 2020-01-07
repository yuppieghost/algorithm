# Recursive Python program for level order traversal of Binary Tree
# solution 1
# A node structure
class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)


def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print("%d" % (root.data))
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


""" Compute the height of a tree--the number of nodes 
	along the longest path from the root node down to 
	the farthest leaf node 
"""


def height(root):
    if not root:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1


# solution 2
def recursive(root):
    if root:
        q = [root]
        while q:
            for i in range(len(q)):
                r = q.pop(0)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
                print(r.data)


if __name__ == '__main__':
    # Driver program to test above function
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(6)
    root.left.right = Node(5)
    # root.left.right = Node(6)

    printLevelOrder(root)
    # recursive(root)

    # This code is contributed by Nikhil Kumar Singh(nickzuck_007)
