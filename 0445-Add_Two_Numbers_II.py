# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res, b = 0, 0
        while l1:
            res = res * 10 + l1.val
            l1 = l1.next
        while l2:
            b = b * 10 + l2.val
            l2 = l2.next
        res = str(res + b)
        tmp = ListNode(res[0])
        head = tmp
        for i in range(1, len(res)):
            tmp.next = ListNode(int(res[i]))
            tmp = tmp.next
        return head