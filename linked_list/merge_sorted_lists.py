# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Given
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity = O(n+m) where n & m are the no. of nodes in list1 and list2 respectively.
# Space Complexity = O(1)

def merge_sorted_lists(list1:ListNode, list2:ListNode):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:

        if list1.val < list2.val:

            tail.next = list1
            list1 = list1.next
        
        else:

            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list2:
        tail.next = list2
    
    if list1:
        tail.next = list1
    
    return dummy.next

# Recursion

def _merge_sorted_lists(list1:ListNode, list2:ListNode):

    if not list1:
        return list2
    
    if not list2:
        return list1

    if list1.val < list2.val:

        list1.next = _merge_sorted_lists(list1.next, list2)
        return list1
    
    else:

        list2.next = _merge_sorted_lists(list1, list2.next)
        return list2
    
