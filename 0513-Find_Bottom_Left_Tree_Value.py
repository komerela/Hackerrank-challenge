# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Uses a right to left implementation of Level Order Traversal, and returns the last element

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        returnList = []
        levelNodes = [root]
        while levelNodes:
            returnList.append([node.val for node in levelNodes])
            nextLevel = []
            for node in levelNodes:
                nextLevel.extend([node.right, node.left])
            levelNodes = [node for node in nextLevel if node]
        return returnList[-1][-1]