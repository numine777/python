from collections import Counter
# Complete the shortPalindrome function below.
def Mix(ch1, ch2):
    return (ch1 * 26) + ch2

def shortPalindrome(s):
    mod = 1000000007
    freq = Counter()
    cfreq = Counter()
    pairfreq = Counter()
    ans = 0

    for ch in s:
        v = ord(ch) - ord('a')
        ans = (ans + cfreq[v]) % mod
        for nc in range(26):
            cfreq[nc] = (cfreq[nc] + pairfreq[Mix(nc, v)]) % mod
        for nc in range(26):
            idx = Mix(nc, v)
            pairfreq[idx] = (pairfreq[idx] + freq[nc]) % mod
        freq[v] += 1

    return ans


print(shortPalindrome("kkkkkkkz"))