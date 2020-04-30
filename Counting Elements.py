##Given an integer array arr, count element x such that x + 1 is also in arr.
##If there're duplicates in arr, count them seperately.

class Solution:
    def countElements(self, arr: List[int]) -> int:
        x = 0
        li = [0]*1001
        for i in arr:
            li[i] += 1
        for i in range(len(li)-1):
            if li[i+1] != 0:
                x += li[i]
        
        return x
