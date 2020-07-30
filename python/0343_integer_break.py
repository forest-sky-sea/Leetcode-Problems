class Solution:
    def integerBreak(self, n: int) -> int:
        def recursive_break(num: int) -> int:
            # opt: always put n * r(0) in res_l
            # for n == 4 r(n) == n
            # for n > 4 r(n) >> n
            if num == 3:
                return 3
            res_l = [num]
            # opt: 1 * r(n - 1) << r(n)
            # opt: 2 * r(n - 2) >> (n - 2) * r(2)
            for i in range(2, num - 2):
                if num - i in dp_cache.keys():
                    res_l.append(i * dp_cache[num - i])
                else:
                    res = recursive_break(num - i)
                    dp_cache[num - i] = res
                    res_l.append(i * res)
            return max(res_l)

        dp_cache = {}
        if n == 2:
            return 1
        if n == 3:
            return 2
        return recursive_break(n)


print(Solution().integerBreak(10))
print(Solution().integerBreak(4))
print(Solution().integerBreak(5))
print(Solution().integerBreak(3))
print(Solution().integerBreak(2))
print(Solution().integerBreak(11))
print(Solution().integerBreak(57))
