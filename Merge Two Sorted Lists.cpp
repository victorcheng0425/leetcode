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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *c1 = l1;
        ListNode *c2 = l2;
        ListNode *t = NULL;
        ListNode *head = NULL;
        if(l1 == NULL && l2 == NULL){
            return l1;
        }else if(l1 == NULL){
            return l2;
        }else if(l2 == NULL){
            return l1;
        }
        if(l1->val <= l2->val){
            head = l1;
            c1 = l1;
            c2 = l2;
        }else{
            head = l2;
            c1 = l2;
            c2 = l1;
        }
        while(c1 != NULL){
            t = c1->next;
            if(t == NULL){
                c1->next = c2;
                break;
            }
            if(t->val <= c2->val){
                c1 = t;
            }else{
                c1->next = c2;
                c1 = c2;
                c2 = t;
            }
        }
        return head;
    }
};
