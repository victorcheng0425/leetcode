from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] #doesnt matter, base case
        length = len(nums)

        list_l = nums[:length//2]
        list_r = nums[length//2:]
        sum_l = self.maxSubArray(list_l)
        sum_r = self.maxSubArray(list_r)
        #print(list_l)
        #print(list_r)
        #print("sum_l: ",sum_l)
        #print("sum_r: ",sum_r)
        cross_sum = 0
        left_sum = -1000
        right_sum = -1000

        for i in range(length//2-1, -1, -1):
          cross_sum += nums[i]
          if cross_sum > left_sum:
            left_sum = cross_sum

        cross_sum = 0
        for i in range(length//2, length):
          cross_sum += nums[i]
          if cross_sum > right_sum:
            right_sum = cross_sum

        cross_sum = right_sum + left_sum
        #print("left_sum: ", left_sum, "right_sum: ", right_sum)
        #print("cross_sum: ", cross_sum)
        return max(sum_l, sum_r, cross_sum)
        
            
        
        

a = Solution()
li = [-2,1,-3,4,-1,2,1,-5,4]
print(li)
li1 = [-2, -1]
print(li1)
result = a.maxSubArray(li)
print(result)
print(a.maxSubArray(li1))
