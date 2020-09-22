'''
Question Description :-

Majority Element II

Given an integer array of size n, find all elements that appear more than [n/3] times.
Note: The algorithm should run in linear time and in O(1) space.


Example 1:
        Input: [3,2,3]
        Output: [3]


Example 2:
        Input: [1,1,1,3,3,2,2,2]
        Output: [1,2]
'''
def majorityElement(nums):
    
    if not nums:
        return []
        
    cand1, count1 = None , 0
    cand2, count2 = None , 0
        
    for num in nums:
        if cand1 == num:
            count1 += 1
        elif cand2 == num:
            count2 += 1
        elif count1 == 0:
            cand1 = num
            count1 += 1
        elif count2 == 0:
            cand2 = num
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
                
    return [x for x in (cand1,cand2) if nums.count(x) > len(nums)//3]


print(majorityElement([1,1,1,3,3,2,2,2]))

#This is a optimal solution.