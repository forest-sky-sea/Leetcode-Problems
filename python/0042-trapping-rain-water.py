from typing import List


class Solution:
    def trap1(self, height: List[int]) -> int:
        i = 1
        water = 0
        while i < len(height) - 1:
            left_max = max(height[0: i])
            right_max = max(height[i + 1:])
            water += max(min(left_max, right_max) - height[i], 0)
            i += 1
        return water

    def trap2(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        i = 1
        while i < n:
            left_max[i] = max(left_max[i - 1], height[i - 1])
            i += 1
        i = n - 2
        while i >= 0:
            right_max[i] = max(right_max[i + 1], height[i + 1])
            i -= 1
        i = 1
        water = 0
        while i < n - 1:
            water += max(min(left_max[i], right_max[i]) - height[i], 0)
            i += 1
        return water

    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        left_max = height[left]
        right_max = height[right]
        water = 0
        while left < right:
            if height[left] < height[right]:
                water += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                water += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return water


h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap1(h))
