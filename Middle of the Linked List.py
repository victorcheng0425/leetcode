class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        curr = head
        count = 0
        while(curr):
            curr = curr.next
            count += 1
        #print(count)
        x = 0
        curr = head
        while(x < count//2):
            curr = curr.next
            #print(curr.val)
            x += 1
        return curr
