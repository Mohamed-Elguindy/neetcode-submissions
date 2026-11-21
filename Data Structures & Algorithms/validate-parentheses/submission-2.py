class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in range(len(s)):
            if stack ==[]:
                stack.append(s[i])
                continue
            elif s[i] in pairs:
                p = pairs[s[i]]
                if stack[-1] == p:
                    stack.pop()
                    continue
                
            stack.append(s[i])
        
        return stack==[]
        