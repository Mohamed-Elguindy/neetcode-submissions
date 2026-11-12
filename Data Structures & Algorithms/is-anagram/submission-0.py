from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        string1 = Counter()

        for i in range(len(s)):
            string1[s[i]]+=1
            string1[t[i]]-=1
        return all(count == 0 for count in string1.values())
            
        