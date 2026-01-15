# def minimum_boats(weights, priority, limit):
#     n = len(weights)
#     used = [False] * n
#     boats = 0

#     for i in range(n):
#         if used[i]:
#             continue
#         used[i] = True
#         paired = False
#         for j in range(i + 1, n):
#             if not used[j]:
#                 if weights[i] + weights[j] <= limit and not (priority[i] == 1 and priority[j] == 1):
#                     used[j] = True
#                     paired = True
#                     break
#         boats += 1
#     return boats


# def can_pair(x, y, weights, priority, limit):
#     if weights[x] + weights[y] > limit:
#         return False
#     if priority[x] == 1 and priority[y] == 1:
#         return False
#     return True


# def remaining_people(B, weights, priority, limit):
#     n = len(weights)
#     used = [False] * n
#     boats = 0
#     evacuated = 0

#     for i in range(n):
#         if boats == B:
#             break
#         if used[i]:
#             continue
#         used[i] = True
#         evacuated += 1
#         for j in range(i + 1, n):
#             if not used[j]:
#                 if weights[i] + weights[j] <= limit and not (priority[i] == 1 and priority[j] == 1):
#                     used[j] = True
#                     evacuated += 1
#                     break
#         boats += 1

#     return n - evacuated


# weights = [30, 50, 60, 40, 70, 80]
# priority = [1, 0, 1, 0, 0, 1]
# limit = 100

# print("Minimum boats =", minimum_boats(weights, priority, limit))
# print("Yes" if can_pair(0, 1, weights, priority, limit) else "No")
# print("Yes" if can_pair(0, 2, weights, priority, limit) else "No")
# print(remaining_people(2, weights, priority, limit))


def minimum_boats(weights, priority, limit):
    people = sorted(zip(weights, priority))
    i = 0
    j = len(people) - 1
    boats = 0

    while i <= j:
        if i != j and people[i][0] + people[j][0] <= limit and not (people[i][1] == 1 and people[j][1] == 1):
            i += 1
            j -= 1
        else:
            j -= 1
        boats += 1

    return boats


def can_pair(x, y, weights, priority, limit):
    if weights[x] + weights[y] > limit:
        return False
    if priority[x] == 1 and priority[y] == 1:
        return False
    return True


def remaining_people(B, weights, priority, limit):
    people = sorted(zip(weights, priority))
    i = 0
    j = len(people) - 1
    boats = 0
    evacuated = 0

    while i <= j and boats < B:
        if i != j and people[i][0] + people[j][0] <= limit and not (people[i][1] == 1 and people[j][1] == 1):
            evacuated += 2
            i += 1
            j -= 1
        else:
            evacuated += 1
            j -= 1
        boats += 1

    return len(people) - evacuated


weights = [30, 50, 60, 40, 70, 80]
priority = [1, 0, 1, 0, 0, 1]
limit = 100

print("Minimum boats =", minimum_boats(weights, priority, limit))
print("Yes" if can_pair(0, 1, weights, priority, limit) else "No")
print("Yes" if can_pair(0, 2, weights, priority, limit) else "No")
print(remaining_people(2, weights, priority, limit))
