def larrysArray(A):
    count = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                count+=1
    if count%2 == 0:
        return "YES"
    else:
        return "NO"

print(larrysArray([3, 1, 2]))
