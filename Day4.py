'''
Question Description :-

Partition Labels

    A string S of lowercase English letters is given.
    We want to partition this string into as many parts as possible 
    so that each letter appears in at most one part, 
    and return a list of integers representing the size of these parts.

Example 1:
    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
    :  S will have length in range [1, 500].
    :  S will consist of lowercase English letters ('a' to 'z') only.
'''

def partitionLabels(S):
    
    lt = []
    start = 0
    end = S.rfind(S[start])
    curr_letter = start+1
    
    while curr_letter < len(S):

        if curr_letter > end:
            
            lt.append(end+1-start)
            start = curr_letter
            end = S.rfind(S[curr_letter])

        temp = S.rfind(S[curr_letter])

        if temp > end :
            end = temp
        
        curr_letter += 1

    lt.append(end+1-start)
    
    return lt


print(partitionLabels("ababcbacadefegdehijhklij"))

'''
Optimal Solution :-

def partitionLabels(self, S: str) -> List[int]:
    last = {s: i for i, s in enumerate(S)}
    j,anchor = 0,0
    ans = []
    for i, c in enumerate(S):
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
            
    return ans
'''