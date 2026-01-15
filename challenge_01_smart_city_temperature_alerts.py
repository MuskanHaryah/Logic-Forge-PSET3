def compute_alert_days(temps, K):
    N = len(temps)
    alert = [0] * N

    for i in range(N):
        for j in range(i + 1, N):
            if temps[j] >= temps[i] + K or temps[j] <= temps[i] - K:
                alert[i] = j
                break

    return alert


def count_alert_days(alert, L, R):
    count = 0
    for i in range(L, R + 1):
        if alert[i] != 0:
            count += 1
    return count