# February 5th, 2020
# Python 3.7.4
# adam note:
#   runtime was 28 ms, faster than 96.01% of online submissions!
#   i have never achieved this speed before now!
"""
21. Merge Two Sorted Lists
    Merge two sorted linked lists and return it as a new list.
    The new list should be made by splicing together the nodes
    of the first two lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class LinkedList:
    def __init__(self, node):
        self.head = node


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == l2 == None:
            return ListNode('')
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val <= l2.val:
            newl = LinkedList(l1)
            l1 = l1.next
            low, hi = l1, l2
        else:
            newl = LinkedList(l2)
            l2 = l2.next
            low, hi = l2, l1
        out = newl.head
        while low != None:
            if low.val > hi.val:
                out.next = hi
                out = out.next
                hi = hi.next
                low, hi = hi, low
            else:
                out.next = low
                out = out.next
                low = low.next
        while hi != None:
            out.next = ListNode(hi.val)
            out = out.next
            hi = hi.next

        return newl.head
