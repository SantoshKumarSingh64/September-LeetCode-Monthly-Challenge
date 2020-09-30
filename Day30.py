'''
Question Description :-

First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
    Input: [1,2,0]
    Output: 3

Example 2:
    Input: [3,4,-1,1]
    Output: 2

Example 3:
    Input: [7,8,9,11,12]
    Output: 1

Follow up: Your algorithm should run in O(n) time and uses constant extra space.
'''
def firstMissingPositive(nums):
    
    x = 1
    while True:
        if x not in nums:
            return x
        x += 1 

print(firstMissingPositive([3,4,-1,1]))
'''
Optimal Solution :-

def firstMissingPositive(nums):
    if nums==[]:
        return 1
    s = set(nums)
    for i in range(1,len(nums)+2):
        if i not in s:
            return i
'''