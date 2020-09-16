'''
Question Description :-

Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
Could you do this in O(n) runtime?

Example:
        Input: [3, 10, 5, 25, 2, 8]
        Output: 28
        Explanation: The maximum result is 5 ^ 25 = 28.
'''
class Node:
    def __init__(self):
        self.data = 1
        self.right = None
        self.left = None

class tree:
    def __init__(self):
        self.root = Node()
        
    def add(self,num):
        
        cur = self.root
        
        string = bin(num).replace("0b", "")

        temp = ''
        for x in range(32-len(string)):
            temp += '0'

        string = temp + string

        for x in string:
            if x == '0':
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node()
                    cur = cur.left
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node()
                    cur = cur.right
                
    def find_max(self,num):
        
        
        cur = self.root
        string2 = ''
        string1 = bin(num).replace("0b", "")
        temp = ''
        for x in range(32-len(string1)):
            temp += '0'

        string1 = temp + string1
        for x in string1:
            if x == '0':
                if cur.right:
                    string2 += '1'
                    cur = cur.right
                else:
                    string2 += '0'
                    cur = cur.left
            else:
                if cur.left:
                    string2 += '1'
                    cur = cur.left
                else:
                    string2 += '0'
                    cur = cur.right
                
        return int(string2,2)


def findMaximumXOR(nums):
        
    trie = tree()
    max_xor = 0
    for x in nums:
            
        trie.add(x)
        max_xor = max(max_xor,trie.find_max(x))
    
    return max_xor


print(findMaximumXOR([3, 10, 5, 25, 2, 8]))

'''
Reference for above solution :- https://www.ritambhara.in/maximum-xor-value-of-two-elements/

Optimal Solution:-

def findMaximumXOR(nums):
    res = 0
    for i in range(30, -1, -1):
        mySet = set()
        res <<= 1
        res += 1
        isValid = False
        for num in nums:
            if (num >> i) in mySet:
                isValid = True
                break
            mySet.add((num >> i) ^ res)
        if not isValid:
            res -= 1
    return res
'''