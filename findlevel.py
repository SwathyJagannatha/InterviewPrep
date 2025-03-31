# Python code to find Level with maximum number of nodes using BFS
from collections import deque

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# A function to find level with maximum number of nodes
def maxNodeLevel(root):
    if root is None:
        return -1

    q = deque()
    q.append(root)

    level = 0
    maxNodes = 0
    maxLevel = 0

    while q:

        # Number of nodes at current level
        size = len(q)

        if size > maxNodes:
            maxNodes = size
            maxLevel = level

        # Process all nodes at current level
        for _ in range(size):
            current = q.popleft()

            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

        level += 1

    return maxLevel

if __name__ == "__main__":

    #          2
    #        /   \
    #       1     3
    #      / \     \
    #     4   6     8
    #    /
    #   5
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(8)
    root.left.left.left = Node(5)

    print(maxNodeLevel(root))