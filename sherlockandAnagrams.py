from collections import Counter

def sherlockAnagrams(s):
    all_s = Counter(''.join(sorted(s[i:j])) for i in range(0, len(s)) for j in range(i+1, len(s)+1))
    return sum(((all_s[key] - 1) * all_s[key])//2 for key in all_s)
