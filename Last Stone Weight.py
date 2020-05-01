class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        length = len(stones)
        ### construct heap array first ###
        for i in range(length//2, -1, -1):
            self.heap(stones, length, i)
        i = 0
        ## choose the two heaviest stones and smash them together ##
        while(len(stones) > 1):
            if(len(stones) > 2 and stones[i+1] < stones[i+2]):
                stones[i+1], stones[i+2] = stones[i+2], stones[i+1]
            stones[i+1] = stones[i] - stones[i+1] ##done
         
            stones = stones[i+1:]  ##construct new array after collision
            length = len(stones) ##construct new heap array
            for i in range(length//2, -1, -1):
                self.heap(stones, length, i)
            #self.heap(stones, len(stones), i)

        return stones[0]
        
   ##heapify function         
    def heap(self, stones: List[int], length, i):

        l = 2*i + 1
        r = 2*i + 2
        largest = i
        if l < length and stones[l] > stones[i]:
            largest = l
        if r < length and stones[r] > stones[largest]:
            largest = r
        if largest != i:
            stones[i], stones[largest] = stones[largest], stones[i]
            self.heap(stones, length, largest)
            
            
