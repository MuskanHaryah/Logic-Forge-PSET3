# def longest_palindromic_substring(s):
#     n = len(s)
#     best = ""

#     for i in range(n):
#         for j in range(i, n):
#             sub = s[i:j + 1]
#             if sub == sub[::-1] and len(sub) > len(best):
#                 best = sub

#     return best


# s = "babad"
# print(longest_palindromic_substring(s))


def longest_palindromic_substring(s):
    if not s:
        return ""

    start = 0
    max_len = 1

    for i in range(len(s)):
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1

        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1

    return s[start:start + max_len]


s = "babad"
print(longest_palindromic_substring(s))
