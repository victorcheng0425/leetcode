  
from typing import List
//Sort everytime
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


//hash key method
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li = []
        key = []
        for i in range(len(strs)):
            flag = 0
            #print("Start")
            if len(li) == 0:
                li.append([strs[i]])
                a = (sorted(strs[i]))
                key.append(a)
                continue
            temp = sorted(strs[i])
            if temp in key:
                index = key.index(temp)
                li[index].append(strs[i])
                flag = 1
            #print(li)
            #print(key)
            if flag == 0:    
              li.append([strs[i]])
              key.append(sorted(strs[i]))
                
        return li
