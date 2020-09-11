'''
Question Description :-

Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

Example 1:
        Input: [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.

Example 2:
        Input: [-2,0,-1]
        Output: 0
        Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

def maxProduct(nums):
    
    curr_max_product = nums[0]
    curr_min_product = nums[0]

    ans = nums[0]

    prev_max_product = nums[0]
    prev_min_product = nums[0]

    for x in nums[1:]:
        
        curr_max_product = max(prev_max_product * x , prev_min_product * x , x)
        curr_min_product = min(prev_max_product * x , prev_min_product * x , x)

        ans = max(ans,curr_max_product)

        prev_max_product = curr_max_product
        prev_min_product = curr_min_product

    return ans

print(maxProduct([-2,0,-1]))

'''
Optimal Solution :-

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        if 0 in nums:
            nums = self.splitByZero(nums)
            products = []
            
            for arr in nums:
                products.append(self.maxProductNoZeros(arr))
                
            products.append(0)
            print(products)
            return max(products)
        else:
            return self.maxProductNoZeros(nums)
            
    def splitByZero(self, nums):
        retArr = [] #2d array
        row = []
        for num in nums:
            if num == 0:
                if len(row) > 0:
                    retArr.append(row)
                    row = []
            else:
                row.append(num)
        if len(row) > 0:
            retArr.append(row)
        return retArr
    
    def maxProductNoZeros(self, nums):        
        if (len(nums) == 1):
            return nums[0]
        
        countNeg = 0
        for num in nums:
            if num < 0:
                countNeg += 1
                
        if (countNeg % 2) == 0:
            #include whole array
            prod = 1
            for num in nums:
                prod *= num
            return prod
        
        #odd number of negatives in array - find whether we should eliminate the last or the first
        elimFirstProd = 1
        i = 0
        while nums[i] > 0 and i < len(nums):
            i += 1
        while i < len(nums)-1:
            i += 1
            elimFirstProd *= nums[i]
            
            
        elimLastProd = 1
        i = len(nums)-1
        while (nums[i] > 0) and i >= 0:
            i -= 1
        while i > 0:
            i -= 1
            elimLastProd *= nums[i]
            
            
        return max(elimFirstProd, elimLastProd)
'''