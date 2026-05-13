class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedVals = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closedVals:
                if stack and stack[-1] == closedVals[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False