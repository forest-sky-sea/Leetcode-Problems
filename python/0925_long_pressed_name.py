class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name and not typed:
            return True
        if not name or not typed:
            return False
        if not name[0] == typed[0]:
            return False
        i, j = 1, 1
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif typed[j] == name[i - 1]:
                j += 1
            else:
                return False
        return i == len(name)

    def isLongPressedName2(self, name: str, typed: str) -> bool:
        if not name and not typed:
            return True
        if not name or not typed:
            return False
        if not name[0] == typed[0]:
            return False
        last_i, last_j = name[0], typed[0]
        i, j = 1, 1
        while i < len(name) or j < len(typed):
            if i < len(name) and name[i] == last_i:
                i += 1
                if j < len(typed) and typed[j] == last_j:
                    j += 1
                else:
                    return False
            else:
                if j >= len(typed):
                    return False
                if typed[j] == last_j:
                    j += 1
                else:
                    if i >= len(name):
                        return False
                    last_i = name[i]
                    last_j = typed[j]
                    if not last_i == last_j:
                        return False
                    else:
                        i += 1
                        j += 1
        return True


print(Solution().isLongPressedName("alex", "alexx"))

