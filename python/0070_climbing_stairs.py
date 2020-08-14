import math


class Solution:
    def climbStairs2(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        return round(sqrt5 / 5 * (math.pow(((1 + sqrt5) / 2), n + 1) - math.pow(((1 - sqrt5) / 2), n + 1)))

    def climbStairs1(self, n: int) -> int:
        if n <= 3:
            return n
        tmp2, tmp1 = 2, 3
        i = 4
        res = 0
        while i <= n:
            res = tmp2 + tmp1
            tmp2 = tmp1
            tmp1 = res
            i += 1
        return res

    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        i = 2
        res = n

        def choose(a: int, b: int):
            result = a / b
            for j in range(1, b):
                result *= (a - j) / (b - j)
            return result

        while i <= n - i:
            res += choose(n - i, i)
            i += 1
        return int(res)


print(Solution().climbStairs(2))
print(Solution().climbStairs(5))
print(Solution().climbStairs(6))
print(Solution().climbStairs(7))
