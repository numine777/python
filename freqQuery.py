from collections import defaultdict

def freqQuery(queries):
    freqs = defaultdict(set)
    lut = dict()
    a = []

    for i, j in queries:
        freq = lut.get(j, 0)
        if i == 1:
            lut[j] = freq + 1
            freqs[freq].discard(j)
            freqs[freq + 1].add(j)
        if i == 2:
            lut[j] = max(freq - 1, 0)
            freqs[freq].discard(j)
            freqs[freq - 1].add(j)
        if i == 3:
            a.append(1 if freqs[j] else 0)
    return a
