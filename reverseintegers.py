def reverse(self, x: int) -> int:
    isPositive = x > 0
    
    s = "".join(reversed(str(abs(x))))
    
    if isPositive and int(s) < (2**31)-1:
        return int(s)
    elif isPositive == False and -int(s) > (-2)**31 :
        return -int(s)
    else:
        return 0
    