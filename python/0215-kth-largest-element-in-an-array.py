from typing import List


class Solution:
    def findKthLargest2(self, nums: List[int], k: int) -> int:

        def partition(l: int, r: int) -> int:
            pivot = nums[l]
            p_idx = l + 1
            while p_idx < r + 1 and nums[p_idx] > pivot:
                p_idx += 1
            p_idx -= 1
            for i in range(p_idx + 1, r + 1):
                if nums[i] > pivot:
                    p_idx += 1
                    nums[i], nums[p_idx] = nums[p_idx], nums[i]
            nums[l], nums[p_idx] = nums[p_idx], nums[l]
            return p_idx

        left, right = 0, len(nums) - 1
        idx = partition(left, right)
        while idx != k - 1:
            if idx > k - 1:
                right = idx - 1
            else:
                left = idx + 1
            idx = partition(left, right)
        return nums[idx]

    def findKthLargest(self, nums: List[int], k: int) -> int:

        def heapify(root: int, last: int):
            while True:
                left_child = root * 2 + 1
                if left_child >= last:
                    return
                max_child = root
                if nums[left_child] > nums[root]:
                    max_child = left_child
                if left_child + 1 < last and nums[left_child + 1] > nums[max_child]:
                    max_child = left_child + 1
                if max_child != root:
                    nums[max_child], nums[root] = nums[root], nums[max_child]
                    root = max_child
                else:
                    return

        n = len(nums)
        for i in range(n // 2, -1, -1):
            heapify(i, n)

        for i in range(k - 1):
            nums[0], nums[n - i - 1] = nums[n - i - 1], nums[0]
            heapify(0, n - i - 1)

        return nums[0]


print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
