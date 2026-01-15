def longest_palindromic_substring(s):
    n = len(s)
    best = ""

    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]
            if sub == sub[::-1] and len(sub) > len(best):
                best = sub

    return best


s = "babad"
print(longest_palindromic_substring(s))
