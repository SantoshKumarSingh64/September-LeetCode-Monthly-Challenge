'''
Question Description :-

    Given an array of integers, find out whether there are two distinct indices i and j in the array such that 
    the absolute difference between nums[i] and nums[j] is at most t 
    and the absolute difference between i and j is at most k.

Example 1:
    Input: nums = [1,2,3,1], k = 3, t = 0
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1, t = 2
    Output: true

Example 3:
    Input: nums = [1,5,9,1,5,9], k = 2, t = 3
    Output: false

'''

def containsNearbyAlmostDuplicate(nums, k, t):
    
    nums_len = len(nums)

    if t == 0 and nums_len == len(set(nums)):
        return False

    for idx , val in enumerate(nums):

        for j in range(idx+1, min(idx+k+1,min(idx+k+1, nums_len))):
            
            if abs(val - nums[j]) <= t:
                return True
        
    return False


print(containsNearbyAlmostDuplicate([1,0,1,1],1,2))
    
'''

Optimal Solution :- 

        if t < 0 or not nums or k <= 0:
            return False
        buckets = {}
        width = t + 1

        for i, n in enumerate(nums):
            buck = n // width
            if buck in buckets:
                return True
            buckets[buck] = n
            if buck+1 in buckets and (buckets[buck+1] - n) <= t:
                return True
            if buck-1 in buckets and (n - buckets[buck-1]) <= t:
                return True
            if i >= k:
                del buckets[nums[i - k] // width]
        return False
'''
