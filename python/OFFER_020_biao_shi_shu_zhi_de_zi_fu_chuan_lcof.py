class Solution:
    def isNumber(self, s: str) -> bool:
        import re

        def is_float(sf: str) -> bool:
            if sf == '.' or not sf:
                return False
            s_parts = re.split('[.]', sf)
            if len(s_parts) > 2:
                return False
            for s_part in s_parts:
                if s_part and re.match('[0-9]+$', s_part) is None:
                    return False
            return True

        s = s.strip()
        if not s:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        e_parts = re.split('[eE]', s)
        if len(e_parts) > 2 or not is_float(e_parts[0]):
            return False
        if len(e_parts) == 2:
            if re.match('[+-]?[0-9]+$', e_parts[1]) is None:
                return False

        return True


print(Solution().isNumber('3.'))
print(Solution().isNumber('.1'))
print(Solution().isNumber(' '))
print(Solution().isNumber(''))
print(Solution().isNumber('+.8'))
print(Solution().isNumber('01'))
print(Solution().isNumber('0 0'))
print(Solution().isNumber('.1e1'))
print(Solution().isNumber('. 1'))
print(Solution().isNumber('2e0'))
print(Solution().isNumber('0'))
print(Solution().isNumber('1'))
print(Solution().isNumber('1 '))
