class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c = nums[0]
        g = nums[0]
        for i in range(1, len(nums), 1):
          c = max(nums[i], nums[i] + c)

          if c > g:
            g = c

        return g
        
