class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        returnList = []
        levelNodes = [root]
        while levelNodes:
            returnList.append([node.val for node in levelNodes])
            nextLevel = []
            for node in levelNodes:
                nextLevel.extend([node.left, node.right])
            levelNodes = [node for node in nextLevel if node]
        return returnList