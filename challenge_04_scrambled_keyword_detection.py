# def find_anagram_indices(s, p):
#     res = []
#     k = len(p)
#     p_sorted = sorted(p)

#     for i in range(len(s) - k + 1):
#         if sorted(s[i:i + k]) == p_sorted:
#             res.append(i)
#     return res


# s = "cbaebabacd"
# p = "abc"

# print(find_anagram_indices(s, p))


def find_anagram_indices(s, p):
    if len(p) > len(s):
        return []

    res = []
    freq_p = [0] * 26
    freq_w = [0] * 26

    for ch in p:
        freq_p[ord(ch) - 97] += 1

    k = len(p)
    for i in range(k):
        freq_w[ord(s[i]) - 97] += 1

    if freq_w == freq_p:
        res.append(0)

    for i in range(k, len(s)):
        freq_w[ord(s[i]) - 97] += 1
        freq_w[ord(s[i - k]) - 97] -= 1
        if freq_w == freq_p:
            res.append(i - k + 1)

    return res


s = "cbaebabacd"
p = "abc"

print(find_anagram_indices(s, p))
