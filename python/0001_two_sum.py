def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target - nums[i] == nums[j]:
                return [i, j]


print(two_sum([2, 7, 11, 15], 26))
