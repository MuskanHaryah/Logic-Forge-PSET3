def find_anagram_indices(s, p):
    res = []
    k = len(p)
    p_sorted = sorted(p)

    for i in range(len(s) - k + 1):
        if sorted(s[i:i + k]) == p_sorted:
            res.append(i)
    return res


s = "cbaebabacd"
p = "abc"

print(find_anagram_indices(s, p))
