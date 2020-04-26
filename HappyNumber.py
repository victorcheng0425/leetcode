class Solution:
    def isHappy(self, n: int) -> bool:
        temp_list = []
        while True:
            list1 = []
            sum = 0
            while n:
              temp = n%10
              list1.append(temp)
              n = n//10
            
            for i in list1:
              sum = sum + i**2
              print(sum)
            if sum in temp_list:
              return False
            temp_list.append(sum)
            n = sum
            if sum == 1:
               return True
    
            
            
            
