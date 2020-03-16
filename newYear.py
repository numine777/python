def minBribes(q):
    count = 0
    q = [p-1 for p in q]

    for i, p in enumerate(q):
        if p - 2 > i:
            return 'Too chaotic'
        for j in range(max(p-1, 0), i):
            if q[j] > p:
                count += 1
    
    return count
