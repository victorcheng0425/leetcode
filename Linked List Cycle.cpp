/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 //O(1) (i.e. constant) memory
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL || head->next == NULL){
            return 0;
        }
        ListNode *curr = head;
        ListNode *n = head->next;
        while(curr != NULL){
            if(n == curr){
                return 1;
            }
            if(n==NULL || n->next==NULL){
                return 0;
            }
            n = n->next->next;
            curr = curr->next;
        }
        return 0;
    }
};
