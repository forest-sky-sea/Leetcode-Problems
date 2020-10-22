from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        last_index = defaultdict(int)
        for i, s in enumerate(S):
            last_index[s] = i
        res_list = []
        head, tail = 0, 0
        for i, s in enumerate(S):
            lst = last_index[S[i]]
            if lst == len(S) - 1:
                res_list.append(lst - head + 1)
                break
            if lst > tail:
                tail = lst
            if i == tail:
                res_list.append(tail - head + 1)
                head = tail + 1
        return res_list


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
