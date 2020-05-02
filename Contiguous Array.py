Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maximum = 0
        curr = 0
        hmap = {0:-1}
        for i in range(0, len(nums), 1):
            if nums[i] == 0:
                curr -= 1
            else:
                curr += 1
            if curr not in hmap:
                hmap[curr] = i
            else:
                maximum = max(maximum, i - hmap[curr])
                
            
        return maximum
              
