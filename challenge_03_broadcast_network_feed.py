def process_operations(N, Q, K, operations):
    subs = [set() for _ in range(N + 1)]
    messages = []
    own_messages = [[] for _ in range(N + 1)]
    msg_id = 1
    result = []

    for idx, op in enumerate(operations):
        parts = op.split()
        if parts[0] == "S":
            u, v = map(int, parts[1:])
            subs[u].add(v)
        elif parts[0] == "U":
            u, v = map(int, parts[1:])
            subs[u].discard(v)
        elif parts[0] == "B":
            u, m = map(int, parts[1:])
            own_messages[u].append(msg_id)
            if len(own_messages[u]) > K:
                expired = own_messages[u].pop(0)
            messages.append((msg_id, u, idx, m))
            msg_id += 1
        else:
            u = int(parts[1])
            visible = []
            for mid, sender, t, m in messages:
                if sender == u or sender in subs[u]:
                    visible.append((t, m % 3 == 0, mid))
            visible.sort(key=lambda x: (-x[0], -(x[1])))
            if not visible:
                result.append("EMPTY")
            else:
                result.append(" ".join(str(x[2]) for x in visible[:10]))
    return result


N = 3
Q = 9
K = 2
operations = [
    "S 1 2",
    "S 1 3",
    "B 2 5",
    "B 3 9",
    "F 1",
    "U 1 2",
    "B 3 6",
    "F 1",
    "F 2"
]

out = process_operations(N, Q, K, operations)
for line in out:
    print(line)
