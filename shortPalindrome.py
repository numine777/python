from collections import Counter
# Complete the shortPalindrome function below.
def Mix(ch1, ch2):
    return (ch1 * 26) + ch2

def shortPalindrome(s):
    freq = Counter()
    cfreq = Counter()
    pairfreq = Counter()
    ans = 0

    for ch in s:
        v = ord(ch) - ord('a')
        ans += cfreq[v]
        for nc in range(26):
            cfreq[nc] += pairfreq[Mix(nc, v)]
            pairfreq[Mix(nc, v)] += freq[nc]
        freq[v] += 1

    return ans % 1000000007


print(shortPalindrome("kkkkkkkz"))
