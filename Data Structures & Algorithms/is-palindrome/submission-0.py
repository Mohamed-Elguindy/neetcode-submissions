class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=0
        j = len(s)
        arr=[]
        revArr=[]
        for i in range(len(s)):
            if s[i].isalnum():
                arr.append(s[i].lower())
            if s[j-i-1].isalnum():
                revArr.append(s[j-i-1].lower())
        return arr == revArr
        

            

        