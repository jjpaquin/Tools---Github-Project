# spc2jxe
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None):
            return l2
        elif (l2 == None):
            return l1
        elif (l1.val <= l2.val):
            head = tail = ListNode(0)
            while l1:
                while(l2 and (l1.val > l2.val)):
                    tail.next = l2
                    tail = tail.next
                    l2 = l2.next
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            while l2:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
            return head.next
        else:
            head = tail = ListNode(0)
            while l2:
                while(l1 and (l2.val > l1.val)):
                    tail.next = l1
                    tail = tail.next
                    l1 = l1.next
                tail.next = l2
                tail = tail.next
                l2 = l2.next
            while l1:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            return head.next