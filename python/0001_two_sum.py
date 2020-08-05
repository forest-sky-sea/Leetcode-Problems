def two_sum2(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target - nums[i] == nums[j]:
                return [i, j]


def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if target - nums[i] in d.keys():
            return [i, d[target - nums[i]]]
        d[nums[i]] = i


print(twoSum([2, 7, 11, 15], 26))

