'''
Question Description :-

Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:
    
    Input: [1,2,3,4]
    Output: "23:41"

Example 2:
    
    Input: [5,5,5,5]
    Output: ""
 

Note:
    A.length == 4
    0 <= A[i] <= 9

'''

import itertools

def largestTimeFromDigits(A):
    combination = sorted(list(itertools.permutations(A)),reverse=True)

    for x in combination:
        h,i,j,k = x

        hour = h*10 + i

        minute = j*10 +k

        if hour < 24 and minute < 60:
            return f"{h}{i}:{j}{k}"

    return ''


print(largestTimeFromDigits([0,0,3,0]))



'''
Optimal Solution which I got from LeetCode itself


from collections import Counter

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        def getMaxLessThan(A, upperChar):
            maxChar = -1
            for char in A:
                if (maxChar == -1 and char <= upperChar) or (char >= maxChar and char <= upperChar):
                    maxChar = char
            return maxChar
        
        solution = ''
        
        digits = A.copy()
        if 0 in digits:
            h1 = 0
            digits.remove(0)
            
            h2 = max(digits)
            digits.remove(h2)
            
            if min(digits) <= 5:
                m1 = getMaxLessThan(digits, 5)
                digits.remove(m1)
                
                m2 = max(digits)
                digits.remove(m2)
                
                solution = '{}{}:{}{}'.format(h1, h2, m1, m2)
        
        digits = A.copy()
        if 1 in digits:
            h1 = 1
            digits.remove(1)
            
            h2 = max(digits)
            digits.remove(h2)
            
            if min(digits) <= 5:
                m1 = getMaxLessThan(digits, 5)
                digits.remove(m1)

                m2 = max(digits)
                digits.remove(m2)

                solution = '{}{}:{}{}'.format(h1, h2, m1, m2)
        
        digits = A.copy()
        if 2 in digits:
            h1 = 2
            digits.remove(2)
            
            if min(digits) <= 3:
                h2 = getMaxLessThan(digits, 3)
                digits.remove(h2)
                
                if min(digits) <= 5:
                    m1 = getMaxLessThan(digits, 5)
                    digits.remove(m1)
                    
                    m2 = max(digits)
                    digits.remove(m2)
                    
                    solution = '{}{}:{}{}'.format(h1, h2, m1, m2)
        
        return solution
'''
