'''
Question Description :-

Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
        Input: [10,2]
        Output: "210"

Example 2:
        Input: [3,30,34,5,9]
        Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.
'''
def largestNumber(nums):
    
    if not any(map(bool,nums)):
        return '0'
    
    nums = list(map(str,nums))

    for x in range(len(nums)-1):
        for y in range(x+1,len(nums)):
            if int(nums[x]+nums[y]) < int(nums[y]+nums[x]):
                nums[x], nums[y] = nums[y], nums[x]
    return ''.join(nums)

print(largestNumber([3,30,34,5,9]))
'''
Optimal Solution :-

def largestNumber(nums):
    
    def cmp(x, y):
        
        u = x + y
        v = y + x
        if u == v:
            return 0
        elif u < v:
            return -1
        else:
            return 1

    v = map(str, nums)
    result = ''.join(reversed(sorted(v, key=cmp_to_key(cmp))))
    if result and result[0] == '0':
        return '0'
    else:
        return result
'''