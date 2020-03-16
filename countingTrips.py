from collections import Counter

def countTrips(arr, r):
    count = 0
    mp2 = Counter()
    mp3 = Counter()

    for i in arr:
        if i in mp3:
            count += mp3[i]
        if i in mp2:
            mp3[i * r] += mp2[i]
        mp2[i*r] += 1
    
    return count
