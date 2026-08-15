class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_b = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in closed_b:
                if stack and stack[-1] == closed_b[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False