
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        if len(candidates) == 0:
            return []
        rs = set()
        self.findCombinations(candidates, target, [], rs)
        return [list(i) for i in rs]
        
    def findCombinations(self, list1, goal, ls, rs):
        if goal == 0:
            rs.add(tuple(ls))
            return
        if goal < 0:
            return
        for i in range(len(list1)):
            if list1[i] > goal: return
            self.findCombinations(list1[i+1:], goal - list1[i], ls +[list1[i]], rs)
            
        