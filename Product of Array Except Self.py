#division method
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        muls = 1
        num = 0
        for i in nums:
            if i!= 0:
                muls = muls * i
            if i == 0:
                num = num +1 
            
        res = []
        if num == 0:
            for i in range(len(nums)):
                res.append(muls//nums[i])
        if num == 1:
            for i in range(len(nums)):
                if nums[i]== 0:
                    res.append(muls)
                else:
                    res.append(0)
        if num >1:
            for i in range(len(nums)):
                res.append(0)
            
        return res
        
  ##dynamic programming   
  class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0]*len(nums)
        r = [0]*len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                l[i] = 1
            else:
                l[i] = l[i-1] * nums[i-1]
            
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                r[i] = 1
            else:
                r[i] = r[i+1] * nums[i+1]
        #print(l,r)
        
        for i in range(0, len(nums)):
            l[i] = l[i] * r[i]
        
        #print(l)
        return l
        
        
        
