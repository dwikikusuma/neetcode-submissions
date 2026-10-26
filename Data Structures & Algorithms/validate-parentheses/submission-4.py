class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
            
        stack = []

        symbol = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }

        for i in s:
            if stack and i in symbol and stack[-1] == symbol[i]:
                stack.pop()
                continue
            
            stack.append(i)
            
        return len(stack) == 0