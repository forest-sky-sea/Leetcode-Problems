/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1 == NULL) {
            return l2;
        } else if (l2 == NULL) {
            return l1;
        }

        int flag = false;
        ListNode* head = NULL;
        ListNode* p = NULL;
        int temp = 0;

        while(l1 != NULL && l2 != NULL) {
            temp = l1->val + l2->val + flag;
            if (head == NULL) {
                head = new ListNode(temp%10);
                p = head;    
            } else {
                p->next = new ListNode(temp%10);
                p = p->next;
            }
            flag = temp/10;
            l1 = l1->next;
            l2 = l2->next;
        }

        while(l1 == NULL && l2 != NULL) {
            temp = l2->val + flag;
            if (flag < 1) {
                p->next = l2;
                break;
            } else {
                p->next = new ListNode(temp%10);
                p = p->next;
                flag = temp/10;
                l2 = l2->next;
            }
        }

        while(l1 != NULL && l2 == NULL) {
            temp = l1->val + flag;
            if (flag < 1) {
                p->next = l1;
                break;
            } else {
                p->next = new ListNode(temp%10);
                p = p->next;
                flag = temp/10;
                l1 = l1->next;
            }
        }
        if (l1==NULL && l2==NULL && flag>0) {
            p->next = new ListNode(1);
        }

        return head;
    }
};
