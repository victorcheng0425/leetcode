class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for (x, y) in enumerate(nums):
            temp = target - y
            if temp in dic:
                li = []
                li.append(dic[temp])
                li.append(x)
                return li
            dic[y] = x
                
            
        
