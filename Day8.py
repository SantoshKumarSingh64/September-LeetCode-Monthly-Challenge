'''
Question Description :- 

Sum of Root To Leaf Binary Numbers

Given a binary tree, each node has value 0 or 1.  
Each root-to-leaf path represents a binary number starting with the most significant bit.  
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers.

 
Example 1:
          1
       /    \
      0      1
     / \    / \
    0   1  0   1

    Input: [1,0,1,0,1,0,1]
    Output: 22
    Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 

Note:

:- The number of nodes in the tree is between 1 and 1000.
:- node.val is 0 or 1.
:- The answer will not exceed 2^31 - 1.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        self.res = 0
        self.path = []
        
        def findPathRec(root):
            if root is not None:
                self.path.append(root.val)
                findPathRec(root.left)
                if root.left is None and root.right is None:
                    self.res += (int("".join(str(i) for i in self.path),2))
                findPathRec(root.right)
                self.path.pop()
            
        findPathRec(root)
        return self.res
        
        
'''
Optimal Solution :-

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        """
        Same as previous solution, but you the fact that bits
        are base 2 to increment, rather than doing string conversion.
        Recursive DFS to save paths
        """
        self.total = 0
        def DFS(root, binary):
            if root == None:
                return
            binary = binary * 2 + root.val
            if root.left == None and root.right == None:
                self.total += binary
            else:
                DFS(root.left, binary)
                DFS(root.right, binary)
        DFS(root, 0)
        return int(self.total)
        
'''