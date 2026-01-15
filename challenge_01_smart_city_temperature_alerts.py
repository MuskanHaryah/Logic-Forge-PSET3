# def compute_alert_days(temps, K):
#     N = len(temps)
#     alert = [0] * N

#     for i in range(N):
#         for j in range(i + 1, N):
#             if temps[j] >= temps[i] + K or temps[j] <= temps[i] - K:
#                 alert[i] = j
#                 break

#     return alert


# def count_alert_days(alert, L, R):
#     count = 0
#     for i in range(L, R + 1):

#         if alert[i] != 0:
#             count += 1
#     return count



def compute_alert_days(temps, K):
    N = len(temps)
    next_warmer = [0] * N
    next_colder = [0] * N

    stack = []
    for i in range(N):
        while stack and temps[i] >= temps[stack[-1]] + K:
            idx = stack.pop()
            next_warmer[idx] = i
        stack.append(i)

    stack = []
    for i in range(N):
        while stack and temps[i] <= temps[stack[-1]] - K:
            idx = stack.pop()
            next_colder[idx] = i
        stack.append(i)

    alert = [0] * N
    for i in range(N):
        if next_warmer[i] and next_colder[i]:
            alert[i] = min(next_warmer[i], next_colder[i])
        elif next_warmer[i]:
            alert[i] = next_warmer[i]
        elif next_colder[i]:
            alert[i] = next_colder[i]

    return alert


def count_alert_days(alert, L, R):
    pref = [0] * len(alert)
    pref[0] = 1 if alert[0] != 0 else 0

    for i in range(1, len(alert)):
        pref[i] = pref[i - 1] + (1 if alert[i] != 0 else 0)

    return pref[R] - (pref[L - 1] if L > 0 else 0)


temps = [73, 74, 75, 71, 69, 72, 76, 73]
K = 3

alert = compute_alert_days(temps, K)

print("Alert days array:", alert)
print("NEXT 0:", alert[0] if alert[0] != 0 else "No Alert")
print("NEXT 3:", alert[3] if alert[3] != 0 else "No Alert")
print("COUNT 0 7:", count_alert_days(alert, 0, 7))
print("COUNT 4 7:", count_alert_days(alert, 4, 7))