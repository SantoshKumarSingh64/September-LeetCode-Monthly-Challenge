'''
Question Description :- 

Image Overlap

Two images A and B are given, represented as binary, square matrices of the same size.(A binary matrix has only 0s and 1s as values.)
We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.
(Note also that a translation does not include any kind of rotation.)
What is the largest possible overlap?

Example 1:

        Input: A = [[1,1,0],
                    [0,1,0],
                    [0,1,0]]
            B = [[0,0,0],
                    [0,1,1],
                    [0,0,1]]
        Output: 3
        Explanation: We slide A to right by 1 unit and down by 1 unit.


Notes: 

-> 1 <= A.length = A[0].length = B.length = B[0].length <= 30
-> 0 <= A[i][j], B[i][j] <= 1

'''

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        
        def finder(x_shift,y_shift):
            num = 0
            for r in range(N):
                for c in range(N):
                    if 0 <= c+x_shift < N and 0<= r+y_shift < N and A[r+y_shift][c+x_shift] == 1 and B[r][c] ==1:
                        num += 1
            return num
        
        return max([finder(x,y) for y in range(-N,N) for x in range(-N,N)])
    
'''
Optimal Solution :-

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        
        a1 = []
        b1 = []
        
        for i in range(N):
            for j in range(N):
                if A[i][j] == 1:
                    a1.append((i,j))
                    
        for i in range(N):
            for j in range(N):
                if B[i][j] == 1:
                    b1.append((i,j))
                    
        dt = Counter((xa-xb, ya-yb) for xa,ya in a1 for xb,yb in b1)

        return max(dt.values() or [0])
'''