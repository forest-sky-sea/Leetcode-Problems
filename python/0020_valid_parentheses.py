from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        queue = deque()
        for c in s:
            if c == '(':
                queue.append('(')
            elif c == '[':
                queue.append('[')
            elif c == '{':
                queue.append('{')
            elif c == ')':
                if queue:
                    if queue.pop() != '(':
                        return False
                else:
                    return False
            elif c == ']':
                if queue:
                    if queue.pop() != '[':
                        return False
                else:
                    return False
            elif c == '}':
                if queue:
                    if queue.pop() != '{':
                        return False
                else:
                    return False
        if queue:
            return False
        return True


print(Solution().isValid("()[]{}"))
print(Solution().isValid("([]{}"))
print(Solution().isValid("([)]"))
