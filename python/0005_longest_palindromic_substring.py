# 660ms
def longestPalindrome(s: str):
    i = 0
    c_dict = {}
    # pal_list = []
    max_pal = ""
    max_l = 0
    while i < len(s):
        if c_dict.get(s[i]):
            for c_ind in c_dict.get(s[i]):
                if s[c_ind: i + 1][::-1] == s[c_ind: i + 1]:
                # if (c_ind == i - 1 or
                #         c_ind == i - 2 or
                #         (c_ind == i - 3 and
                #          s[c_ind + 1] == s[i - 1]) or
                #         (c_ind + 1, i - 1) in pal_list or
                #         s[c_ind: i + 1][::-1] == s[c_ind: i + 1]):
                #     pal_list.append((c_ind, i))
                    if i - c_ind + 1 > max_l:
                        max_l = i - c_ind + 1
                        max_pal = s[c_ind: i + 1]
                    break
            c_dict.get(s[i]).append(i)
        else:
            c_dict[s[i]] = [i]
            # pal_list.append((i, i))
            if max_l == 0:
                max_l = 1
                max_pal = s[i]
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


print(longestPalindrome1("adda"))
print(longestPalindrome("avaddsddaa"))
print(longestPalindrome("as"))
print(longestPalindrome("aaaaasaaaa"))
print(longestPalindrome("aaaaaaaaa"))
print(longestPalindrome("ccc"))
