class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sMap = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in sMap:
                if stack and stack[-1] == sMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False