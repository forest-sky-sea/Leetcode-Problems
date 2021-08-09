class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        judge_list = [x * x for x in range(2 ** 16)]
        judge_set = set(judge_list)
        break_p = c / 2
        for i in judge_list:
            if c - i in judge_set:
                return True
            if i > break_p:
                return False

    def judgeSquareSum2(self, c: int) -> bool:
        low = 0
        high = int(c ** 0.5)
        while low <= high:
            s = low ** 2 + high ** 2
            if c == s:
                return True
            elif c < s:
                high -= 1
            else:
                low += 1
        return False


print(Solution().judgeSquareSum2(2147482647))
