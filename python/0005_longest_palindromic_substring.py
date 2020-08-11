from collections import defaultdict


# 660ms
def longestPalindrome(s: str):
    if not s:
        return ''
    max_pal = s[0]
    max_l = 1
    c_dict = defaultdict(list)
    i = 0
    while i < len(s):
        for c_ind in c_dict[s[i]]:
            if s[c_ind: i + 1][::-1] == s[c_ind: i + 1]:
                if i - c_ind + 1 > max_l:
                    max_l = i - c_ind + 1
                    max_pal = s[c_ind: i + 1]
                break
        c_dict[s[i]].append(i)
        i += 1
    return max_pal


# guided 1212ms
def longestPalindrome1(s: str):
    def expend_pal(left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    start, end = 0, 0
    for i in range(len(s)):
        l, r = expend_pal(i, i)
        if r - l > end - start:
            start, end = l, r
        l, r = expend_pal(i, i + 1)
        if r - l > end - start:
            start, end = l, r
    return s[start: end + 1]


print(longestPalindrome("adda"))
print(longestPalindrome("avaddsddaa"))
print(longestPalindrome("as"))
print(longestPalindrome("aaaaasaaaa"))
print(longestPalindrome("aaaaaaaaa"))
print(longestPalindrome("ccc"))
