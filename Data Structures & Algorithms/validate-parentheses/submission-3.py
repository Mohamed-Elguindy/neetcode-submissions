class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if stack != [] and char in pairs:
                p = pairs[char]
                if stack[-1] == p:
                    stack.pop()
                    continue
            stack.append(char)
        
        return stack==[]
        