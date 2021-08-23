class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 1)
        nums[0] = 0
        if n < 1:
            return nums[0]
        nums[1] = 1
        i = 2
        j = 1
        flag = True
        res = 1
        while i < n + 1:
            if flag:
                nums[i] = nums[j]
            else:
                nums[i] = nums[j] + nums[j + 1]
                j += 1
            if nums[i] > res:
                res = nums[i]
            i += 1
            flag = not flag
        return res


print(Solution().getMaximumGenerated(15))
