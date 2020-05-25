

def biggerIsGreater(w):
    letterlist = list(w)
    valuelist = list()

    for l in letterlist:
         valuelist.append(ord(l))
    
    i = len(valuelist) - 1
    while i != 0 and valuelist[i-1] >= valuelist[i]:
        i-=1
    
    if i <= 0:
        return "no answer"

    j = len(valuelist) - 1
    while j > i and valuelist[j] <= valuelist[i-1]:
        j-=1

    letterlist[j], letterlist[i-1] = letterlist[i-1], letterlist[j]
    prefix = letterlist[:i]
    suffix = letterlist[i:]
    suffix.reverse()

    return "".join(prefix + suffix)
