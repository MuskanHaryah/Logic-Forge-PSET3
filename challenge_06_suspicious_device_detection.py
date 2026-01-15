# def find_repeated_identifier(nums):
#     n = len(nums) // 2
#     for x in nums:
#         count = 0
#         for y in nums:
#             if x == y:
#                 count += 1
#         if count == n:
#             return x


# nums = [2, 1, 2, 5, 3, 2]
# print(find_repeated_identifier(nums))


def find_repeated_identifier(nums):
    freq = {}
    target = len(nums) // 2

    for x in nums:
        freq[x] = freq.get(x, 0) + 1
        if freq[x] == target:
            return x


nums = [2, 1, 2, 5, 3, 2]
print(find_repeated_identifier(nums))
