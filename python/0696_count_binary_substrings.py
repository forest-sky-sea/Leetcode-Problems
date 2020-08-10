class Solution:
    # 192ms
    def countBinarySubstrings(self, s: str) -> int:
        count_last = 0
        count_ret = 0
        i = 0
        while i < len(s):
            last = s[i]
            if last == '0':
                index = s.find('1', i)
            else:
                index = s.find('0', i)
            if index != -1:
                count_cur = index - i
                i = index
            else:
                count_cur = len(s) - i
                i = len(s)
            count_ret += min(count_cur, count_last)
            count_last = count_cur
        return count_ret

    # 200ms
    def countBinarySubstrings1(self, s: str) -> int:
        if not s:
            return 0
        count0 = 0
        count1 = 0
        count_ret = 0
        last = s[0]
        if last == '0':
            count0 = 1
        else:
            count1 = 1
        for i in range(1, len(s)):
            c = s[i]
            if c != last:
                last = c
                count_ret += min(count0, count1)
                if c == '0':
                    count0 = 1
                else:
                    count1 = 1
            else:
                if c == '0':
                    count0 += 1
                else:
                    count1 += 1
        count_ret += min(count0, count1)
        return count_ret

    # 172ms
    def countBinarySubstrings2(self, s: str) -> int:
        if not s:
            return 0
        count0 = 0
        count1 = 0
        count_ret = 0
        last = s[0]
        if last == '0':
            count0 = 1
        else:
            count1 = 1
        for i in range(1, len(s)):
            c = s[i]
            if c != last:
                if c == '0':
                    count0 = 1
                else:
                    count1 = 1
                last = c
            else:
                if c == '0':
                    count0 += 1
                else:
                    count1 += 1
            if c == '0':
                if count1 >= count0:
                    count_ret += 1
            else:
                if count0 >= count1:
                    count_ret += 1

        return count_ret


print(Solution().countBinarySubstrings('00100'))
print(Solution().countBinarySubstrings('00110011'))
print(Solution().countBinarySubstrings('10101'))
