'''
Qustion Description :-

Subarray Product Less Than K

You are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where 
the product of all the elements in the subarray is less than k.


Example 1:
    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are: 
                [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
                Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.



Note:
        0 < nums.length <= 50000
        0 < nums[i] < 1000
        0 <= k < 10^6
'''
def numSubarrayProductLessThanK(nums, k):

    l = 0
    prod = 1
    count = 0

    for r in range(len(nums)):
        prod = prod * nums[r]

        if prod >= k:
            while prod >= k and l <= r:
                prod = prod//nums[l]
                l += 1
        count += (r-l+1)

    return count

print(numSubarrayProductLessThanK([10, 5, 2, 6],100))    

#This is a optimal solution.