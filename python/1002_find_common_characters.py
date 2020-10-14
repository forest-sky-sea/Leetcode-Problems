from functools import reduce
from typing import List
from collections import defaultdict, Counter


class Solution:
    def commonChars_magic(self, A: List[str]) -> List[str]:
        return list(reduce(lambda x, y: x & y, map(Counter, A)).elements())

    def commonChars(self, A: List[str]) -> List[str]:
        def char_count(x_str: str) -> dict:
            count_dict = defaultdict(int)
            for x_char in x_str:
                count_dict[x_char] += 1
            return count_dict

        dict_res = char_count(A[0])
        for i in range(1, len(A)):
            dict_a = dict_res.copy()
            dict_b = char_count(A[i])
            for key_a in dict_a.keys():
                if key_a in dict_b.keys():
                    dict_res[key_a] = min(dict_a[key_a], dict_b[key_a])
                else:
                    dict_res.pop(key_a)

        res = []
        for key, value in dict_res.items():
            res.extend(list(key) * value)
        return res

    def commonChars2(self, A: List[str]) -> List[str]:
        def merge_dict(dict_a: dict, dict_b: dict) -> dict:
            res_dict = {}
            for key_a in dict_a.keys():
                if key_a in dict_b.keys():
                    res_dict[key_a] = min(dict_a[key_a], dict_b[key_a])
            return res_dict

        alphabet = []
        for a_str in A:
            count = defaultdict(int)
            for a_char in a_str:
                count[a_char] += 1
            alphabet.append(count)

        res = []
        for key, value in reduce(merge_dict, alphabet).items():
            res.extend(list(key) * value)
        return res


print(Solution().commonChars_magic(["bella", "label", "rolle"]))
