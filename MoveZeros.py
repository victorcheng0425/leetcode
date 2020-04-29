from typing import List
#insertion method
class Solution:  
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            temp = nums[i]
            #print("temp: ", temp)
            key = i
            #print("key: ", key)
            while key >= 0 and nums[key-1] == 0:
                nums[key] = nums[key-1]
                key = key - 1
            #print("Key after while loop: ", key)
            if key >= 0:
              nums[key] = temp
            else:
              nums[key+1] = temp
              
#move num != 0 to the front, idx keep track of the index.              
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0
        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0
