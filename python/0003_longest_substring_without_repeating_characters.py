def lengthOfLongestSubstring(s: str):
    if len(s) == 0:
        return 0
    max_l = 0
    head = 0
    tail = head + 1
    # cur_l = {s[head]: head}
    while tail < len(s):
        # if s[tail] in cur_l.keys() and cur_l[s[tail]] >= head:
        # pos = cur_l.get(s[tail], -1)
        pos = s.find(s[tail], head, tail)
        if pos != -1:
            max_l = max(max_l, tail - head)
            head = pos + 1
            # head = cur_l[s[tail]] + 1
            # head = max(head, pos + 1)
        # cur_l[s[tail]] = tail
        tail = tail + 1
    max_l = max(max_l, tail - head)
    return max_l


print(lengthOfLongestSubstring('pwwkpw'))
print(lengthOfLongestSubstring('abba'))
