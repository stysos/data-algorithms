

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
            print(f"{result = }")
            print(f"{stack = }")

        return result



        
if __name__ == "__main__":
    
    node3 = TreeNode(val=3, left=None, right=None)
    
    node2 = TreeNode(val=2, left=node3, right=None)
    
    node = TreeNode(val=1, left=None, right=node2)
    
    # node = TreeNode(val=1, left=TreeNode(val=2), right=None)
    
    
    
    test_case = Solution()
    
    print(test_case.inorderTraversal(root=node))
    
    
    