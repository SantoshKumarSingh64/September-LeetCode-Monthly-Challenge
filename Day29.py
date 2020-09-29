'''
Question Description :-

Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.


Example 1:
        Input: s = "leetcode", wordDict = ["leet", "code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
        Input: s = "applepenapple", wordDict = ["apple", "pen"]
        Output: true
        Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
                    Note that you are allowed to reuse a dictionary word.

Example 3:
        Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
        Output: false
'''
def wordBreak(s, wordDict):

    dp = [True] + [False] * len(s)
        
    for x in range(1,len(s)+1):
            
        for word in wordDict:
            if dp[x- len(word)] and s[:x].endswith(word):
                    
                dp[x] = True
                    
    return dp[-1]

    

print(wordBreak("aaaaaaa",["aaaa","aaa"]))

'''
Optimal Solution :-


def wordBreak(s, wordDict):
    
    def helper(idx):
        if idx == len(s):
            return True
        if idx > len(s):
            return False
            
        for word in wordDict:
            if s.find(word, idx) == idx and helper(idx+len(word)) == True:
                return True
        return False
    
    return helper(0)
'''