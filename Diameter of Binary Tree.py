# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        l_height = self.gothrough(root.left)
        r_height = self.gothrough(root.right)
        l_diameter = self.diameterOfBinaryTree(root.left)
        r_diameter = self.diameterOfBinaryTree(root.right)
        return max(l_height+r_height, max(l_diameter, r_diameter))
    
    ##Find height
    def gothrough(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        return 1 + max(self.gothrough(root.left), self.gothrough(root.right))
