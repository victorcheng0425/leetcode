/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* curr = head;
        ListNode* delay = head;
        for(int x = 0; x < n; x++){
            if(delay->next != NULL){
                delay = delay->next;
            }else{
                head = head->next;
                return head;
            }
        }

        while(delay->next != NULL){
            curr = curr->next;
            delay = delay->next;
        }
        curr->next = curr->next->next;
        return head;
    }
};
