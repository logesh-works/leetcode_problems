class Solution:
    def isValid(self, s: str) -> bool:
        vv = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        if len(s) <= 1:
            return False
        for i in s:
            if i in vv.values():
                stack.append(i)
            elif stack and vv[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return False if stack else True