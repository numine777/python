
# Complete the lilysHomework function below.
def lilysHomework(arr):
    count = 0
    lut = dict()
    for i, v in enumerate(arr):
        lut[v] = i
    narr = sorted(arr)
    
    for i in range(len(arr)):
        if arr[i] != narr[i]:
            count+=1
            idx = lut[narr[i]]
            arr[i], arr[idx] = arr[idx], arr[i]
            lut[arr[i]] = i
            lut[arr[idx]] = idx
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    asc = lilysHomework(list(arr))
    desc = lilysHomework(list(reversed(arr)))
    result = min(asc, desc)

    fptr.write(str(result) + '\n')