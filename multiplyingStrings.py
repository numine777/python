class Solution:
    def __init__(self):
        self.lut1 = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
        self.lut2 = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0"}
    
    def multiply(self, num1: str, num2: str) -> str:
        
        iresult = self.convert(num1) * self.convert(num2)
        if iresult == 0:
            return "0"
        return self.stringify(iresult, "")
    
    def convert(self, n):
        tot = 0
        for i, l in enumerate(n):
            tot += self.lut1[l] * 10**(len(n)-1-i)
        print(tot)
        return tot
            
    def stringify(self, r, s):
        if r <= 0:
            return s
        s = self.lut2[r % 10] + s
        return self.stringify(r//10, s)

ans = Solution()

print(ans.multiply("123", "456"))