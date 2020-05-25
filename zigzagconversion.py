def convert(self, s: str, numRows: int) -> str:
    newOrder = [[] for i in range(numRows)]
    snewOrder = list()
    
    if numRows <= 1:
        return s
    
    curRow = 0
    goingDown = True
    
    for l in s:
        newOrder[curRow].append(l)
        if curRow < numRows-1 and goingDown:
            curRow += 1
            if curRow == numRows -1:
                goingDown = False
        elif curRow > 0:
            curRow -= 1
            if curRow == 0:
                goingDown = True
    
    for i in range(numRows):
        snewOrder += newOrder[i]
        
    return "".join(snewOrder)