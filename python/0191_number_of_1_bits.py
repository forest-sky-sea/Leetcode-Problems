class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count


print(Solution().hammingWeight(0b00000000000000000000000000001011))
