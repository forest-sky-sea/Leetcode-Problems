from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_d = defaultdict(int)
        for num in nums:
            nums_d[num] += 1
        nums_l = list(nums_d.items())

        def heapy(node: int, n: int):
            min_ind = node
            left = node * 2 + 1
            if left < n and nums_l[min_ind][1] > nums_l[left][1]:
                min_ind = left
            right = node * 2 + 2
            if right < n and nums_l[min_ind][1] > nums_l[right][1]:
                min_ind = right
            if not min_ind == node:
                nums_l[min_ind], nums_l[node] = nums_l[node], nums_l[min_ind]
                heapy(min_ind, n)

        def heap_sort():
            for i in range(k // 2 - 1, -1, -1):
                heapy(i, k)
            for i in range(k, len(nums_l)):
                if nums_l[i][1] > nums_l[0][1]:
                    nums_l[i], nums_l[0] = nums_l[0], nums_l[i]
                    heapy(0, k)

        heap_sort()
        return [x[0] for x in nums_l[0:k]]


a = Solution().topKFrequent([3, 0, 1, 0], 1)
b = Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
o = 1
