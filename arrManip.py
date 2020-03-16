def arrayManipulation(n, queries):
    ans = [0 for i in range(n + 1)]
    for i in queries:
        a = queries[0]
        b = queries[1]
        k = queries[2]
        ans[a] += k
        ans[b] -= k
    max_val = 0
    running_count = 0
    for i in ans:
        running_count += i
        if running_count > max_val:
            max_val = running_count
    
    return max_val
