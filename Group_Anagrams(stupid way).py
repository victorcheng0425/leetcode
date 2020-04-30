  
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li = []
        for i in range(len(strs)):
            flag = 0
            if len(li) == 0:
                li.append([strs[i]])
                continue
            for j in range(len(li)):
                if type(li[j]) == list:
                    if sorted(strs[i]) == sorted(li[j][0]):
                        li[j].append(strs[i])
                        flag = 1
                        break
            if flag == 0:    
              li.append([strs[i]])
                
        return li

a = Solution()
li = ["eat", "tea", "tan", "ate", "nat", "bat"]
#print(li)
print(a.groupAnagrams(li))
