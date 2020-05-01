from typing import List
#Can you solve it in O(N) time and O(1) space?
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = 0
        while(len(S) > i):
            if i == 0 and S[i] == '#':
                S = S[i+1:]
                i = -1
            elif S[i] == '#':
               S = S[:i-1] + S[i+1:]
               i = -1
            i += 1
        i = 0
        while(len(T) > i):
            if i == 0 and T[i] == '#':
                T = T[i+1:]
                print("FIRST IF: ", T)
                i = -1
            elif T[i] == '#':
               T = T[:i-1] + T[i+1:]
               i = -1
               print(T)
            i += 1
        print(S,T)
        return S==T

            

a = Solution()
S = "j##xfix"
T = "j###xfix"
li = [1,2,3]
li = [1,1,2]
li = [999,998,997,996,995]
print(a.backspaceCompare(S,T))
