'''
Question Description :-

Word Pattern

Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern 
and a non-empty word in str.


Example 1:
        Input: pattern = "abba", str = "dog cat cat dog"
        Output: true

Example 2:
        Input:pattern = "abba", str = "dog cat cat fish"
        Output: false


Example 3:
        Input: pattern = "aaaa", str = "dog cat cat dog"
        Output: false


Example 4:
        Input: pattern = "abba", str = "dog dog dog dog"
        Output: false

Notes:
You may assume pattern contains only lowercase letters, 
and str contains lowercase letters that may be separated by a single space.
'''
def wordPattern(pattern,str):
    
    lt = str.split()
    if len(pattern) != len(lt):
        return False  
    dt = {}
    dt1 = {}

    for (x,y) in zip(pattern,lt):
        if x in dt:
            if dt[x] != y:
                return False
        elif y in dt1:
            if dt1[y] != x:
                return False
        else:
            dt[x] = y
            dt1[y] = x
                
    return True

print(wordPattern('aaa','aa aa aa'))

#This solution is a optimal solution