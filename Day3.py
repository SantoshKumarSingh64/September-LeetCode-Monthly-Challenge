'''
Question Description :-
Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it 
and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only 
and its length will not exceed 10000.


Example 1:
    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.


Example 2:
    Input: "aba"
    Output: False


Example 3:
    Input: "abcabcabcabc"
    Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''


def repeatedSubstringPattern(s):
    ss = (s + s)[1:-1] 
    print(ss)
    print(s)
    return ss.find(s) != -1

'''
def repeatedSubstringPattern(s):
    
    substring_len = len(set(s))

    if len(s)//2 < substring_len: 
        return False 
     

    def correct_substring(string,substr_length):

        for x in range(substr_length,len(string),substr_length):

            print(string[:substr_length],string[x:x+substr_length])
            if string[:substr_length] != string[x:x+substr_length]:
                
                return False
        
        return True

    while True:

        if correct_substring(s,substring_len):
            print(substring_len)
            return True

        substring_len += 1

        if len(s)//2 < substring_len: 
            break

    return False

'''   


print(repeatedSubstringPattern('ababab'))