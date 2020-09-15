'''
Question Description :-

Length of Last Word

Given a string s consists of upper/lower-case alphabets and 
empty space characters ' ', return the length of last word 
(last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
        Input: "Hello World"
        Output: 5
'''
def lengthOfLastWord(s):

    arr = list(s.split())
    if len(arr) == 0:
        return 0
    return len(arr[-1])

print(lengthOfLastWord("Hello World")) 

'''
Optimal Solution :-

def lengthOfLastWord(s):
    if not s or len(s) == 0:
        return 0
    return len(re.split('\s+', s.strip())[-1])
'''