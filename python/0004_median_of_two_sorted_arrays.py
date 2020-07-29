def findMedianSortedArrays(nums1, nums2):
    def find_k(sub1, sub2, k):
        if len(sub1) == 0:
            return sub2[k - 1]
        if len(sub2) == 0:
            return sub1[k - 1]
        if k == 1:
            return min(sub1[0], sub2[0])
        pos1 = min(len(sub1), k // 2)
        pos2 = min(len(sub2), k // 2)
        if sub1[pos1 - 1] < sub2[pos2 - 1]:
            return find_k(sub1[pos1:], sub2, k - pos1)
        else:
            return find_k(sub1, sub2[pos2:], k - pos2)

    def find_k2(ind1, ind2, k):
        if ind1 == len(nums1):
            return nums2[k + ind2 - 1]
        if ind2 == len(nums2):
            return nums1[k + ind1 - 1]
        if k == 1:
            return min(nums1[ind1], nums2[ind2])
        pos1 = min(len(nums1), k // 2 + ind1)
        pos2 = min(len(nums2), k // 2 + ind2)
        if nums1[pos1 - 1] < nums2[pos2 - 1]:
            return find_k2(pos1, ind2, k - (pos1 - ind1))
        else:
            return find_k2(ind1, pos2, k - (pos2 - ind2))

    if (len(nums1) + len(nums2)) % 2 != 0:
        return find_k(nums1, nums2, (len(nums1) + len(nums2)) // 2 + 1)
    else:
        return (find_k(nums1, nums2, (len(nums1) + len(nums2)) // 2 + 1) +
                find_k(nums1, nums2, (len(nums1) + len(nums2)) // 2)) / 2

    # if (len(nums1) + len(nums2)) % 2 != 0:
    #     return find_k2(0, 0, (len(nums1) + len(nums2)) // 2 + 1)
    # else:
    #     return (find_k2(0, 0, (len(nums1) + len(nums2)) // 2 + 1) +
    #             find_k2(0, 0, (len(nums1) + len(nums2)) // 2)) / 2


print(findMedianSortedArrays([2], [1, 3, 4]))
print(findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8]))
print(findMedianSortedArrays([1, 2], [3, 4]))


