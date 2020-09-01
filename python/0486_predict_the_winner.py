from typing import List


class Solution:
    # magic
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = [[nums[i] for i in range(len(nums))] for _ in range(len(nums))]
        j = 1
        while j < len(nums):
            i = j - 1
            while i >= 0:
                score[i][j] = max((nums[i] - score[i + 1][j]), (nums[j] - score[i][j - 1]))
                i -= 1
            j += 1
        return score[0][len(nums) - 1] >= 0

    # guided
    def PredictTheWinner_dp(self, nums: List[int]) -> bool:
        nums_l = len(nums)
        if nums_l <= 2:
            return True

        has_score = [[False for _ in range(len(nums))] for _ in range(len(nums))]
        dp_score = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        def score(left: int, right: int) -> int:
            if right == left:
                return nums[left]
            if not has_score[left][right]:
                head_score = nums[left] - score(left + 1, right)
                tail_score = nums[right] - score(left, right - 1)
                has_score[left][right] = True
                dp_score[left][right] = max(head_score, tail_score)
            return dp_score[left][right]

        return score(0, len(nums) - 1) >= 0

    def PredictTheWinner_dp2(self, nums: List[int]) -> bool:
        nums_l = len(nums)
        if nums_l <= 2:
            return True

        dp_cache1 = {}
        dp_cache2 = {}
        TURN1 = True
        TURN2 = False

        def dfs(remain: List[int], turn: bool):
            if len(remain) == 2:
                max_remain, min_remain = max(remain), min(remain)
                if str(remain) not in dp_cache1.keys():
                    dp_cache1[str(remain)] = (max_remain, min_remain)
                if str(remain) not in dp_cache2.keys():
                    dp_cache2[str(remain)] = (min_remain, max_remain)
                if turn:
                    return dp_cache1[str(remain)]
                else:
                    return dp_cache2[str(remain)]
            if turn:
                if str(remain) not in dp_cache1.keys():
                    val1_head, val2_head = dfs(remain[1:], TURN2)
                    val1_tail, val2_tail = dfs(remain[:-1], TURN2)
                    if val1_head + remain[0] >= val1_tail + remain[-1]:
                        dp_cache1[str(remain)] = (val1_head + remain[0], val2_head)
                    else:
                        dp_cache1[str(remain)] = (val1_tail + remain[-1], val2_tail)
                return dp_cache1[str(remain)]
            else:
                if str(remain) not in dp_cache2.keys():
                    val1_head, val2_head = dfs(remain[1:], TURN1)
                    val1_tail, val2_tail = dfs(remain[:-1], TURN1)
                    if val2_head + remain[0] >= val2_tail + remain[-1]:
                        dp_cache2[str(remain)] = (val1_head, val2_head + remain[0])
                    else:
                        dp_cache2[str(remain)] = (val1_tail, val2_tail + remain[-1])
                return dp_cache2[str(remain)]

        dfs(nums, TURN1)
        return dp_cache1[str(nums)][0] >= dp_cache1[str(nums)][1]

    def PredictTheWinner_old(self, nums: List[int]) -> bool:
        nums_l = len(nums)
        if nums_l <= 2:
            return True

        def dfs(remain: List[int], turn1: bool, sum1: int, sum2: int):
            if len(remain) == 2:
                if turn1:
                    return sum1 + max(remain) >= sum2 + min(remain)
                else:
                    return sum1 + min(remain) >= sum2 + max(remain)
            if turn1:
                return (dfs(remain[1:], not turn1, sum1 + remain[0], sum2) or
                        dfs(remain[:-1], not turn1, sum1 + remain[-1], sum2))
            else:
                return (dfs(remain[1:], not turn1, sum1, sum2 + remain[0]) and
                        dfs(remain[:-1], not turn1, sum1, sum2 + remain[-1]))

        return dfs(nums, True, 0, 0)


print(Solution().PredictTheWinner([1, 5, 233, 7]))
print(Solution().PredictTheWinner([1, 1, 567, 1, 1, 99]))
