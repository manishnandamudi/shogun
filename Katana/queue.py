from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

#bfs algo usses queue
class Solution:
    def maxDepth(self, queue: Queue) -> int:
        if not queue:
            return 0
        
        level = 0
        q = deque([queue.front()])  # Start from the root node
        while q:
            level += 1  # Increment the level for each level of the tree
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return level

# Example usage:
queue = Queue()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = None  # Placeholder for empty left child
root.right.right = None  # Placeholder for empty right child
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)
root.left.right = TreeNode(71)
queue.enqueue(root)

# Create a solution object
solution = Solution()

# Calculate the maximum depth of the binary tree
max_depth = solution.maxDepth(queue)
print("Maximum Depth:", max_depth)
