'''
Question Description :- 

All Elements in Two Binary Search Trees

    Given two binary search trees root1 and root2.
    Return a list containing all the integers from both trees sorted in ascending order.

 
Example 1:

            2                  0              
          /   \              /   \
         1     4            1     3
     
        Input: root1 = [2,1,4], root2 = [1,0,3]
        Output: [0,1,1,2,3,4]


Example 2:

        Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
        Output: [-10,0,0,1,2,5,7,10]


Example 3:

        Input: root1 = [], root2 = [5,1,7,0,2]
        Output: [0,1,2,5,7]


Example 4:

        Input: root1 = [0,-10,10], root2 = []
        Output: [-10,0,10]


Example 5:

            1            8
             \          /
              8        1
        
        Input: root1 = [1,null,8], root2 = [8,1]    
        Output: [1,1,8,8]
 
Constraints:
Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
'''

def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
    def preorder(cur_node,lt):
            
        if cur_node:
            preorder(cur_node.left,lt)
            lt.append(cur_node.val)
            preorder(cur_node.right,lt)
                
        return lt
                
    arr1 = preorder(root1,[])
    arr2 = preorder(root2,[])
                
    arr = []
        
    i = 0
    j = 0
        
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
            
        else:
            arr.append(arr2[j])
            j += 1
                
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
            
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
        
    return arr

'''
Optimal Solution :-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1, stack1, root = [], [], root1
        while stack1 or root:
            while root:
                stack1.append(root)
                root = root.left
            root = stack1.pop()
            l1.append(root.val)
            root = root.right
        l2, stack2, root = [], [], root2
        while stack2 or root:
            while root:
                stack2.append(root)
                root = root.left
            root = stack2.pop()
            l2.append(root.val)
            root = root.right
        l = l1 + l2
        return sorted(l)
'''