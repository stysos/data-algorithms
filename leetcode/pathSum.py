class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def dfs(node, currSum):
            if not node:
                return False
            
            currSum += node.val
            if not node.left and not node.right:
                return currSum == targetSum
            
            return (dfs(node.left, currSum) or
            dfs(node.right, currSum))
            
            

        sum = 0
        dfs(root, sum)
    
test_case = Solution()

# node = TreeNode(val=5, left=TreeNode(4, 11, None), right=TreeNode(val=8, left=TreeNode(13), right=TreeNode(4, None, 1)))

node = TreeNode(val=5)

test_case.hasPathSum(node, 5)
