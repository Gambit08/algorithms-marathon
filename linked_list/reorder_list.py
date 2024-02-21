# https://leetcode.com/problems/reorder-list/description/

# Given
# L0 → L1 → … → Ln - 1 → Ln
# Output
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …   

# Input [1,2,3,4]
# Output [1,4,2,3]

# Approach
# Find the middle of the list.
# Reverse the second half of the list.
# Make that both halfs end with a null at the end.
# Now merge the two lists together.

# GIVEN
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head:ListNode):

    # 1. middle of the list

    slow = head
    fast = head.next


    # if the number of nodes in the list are even, then the fast pointer is going to end at last by the point slow reaches middle of the list
    # if the number of nodes in the list are odd, then the fast pointer is going to pass through the entire list and be null
    # we want to continue until we reach the above two conditions.
    while fast and fast.next != None:

        slow = slow.next
        fast = fast.next
        fast = fast.next

    # at this point slow.next would give us the head of the second part of the node list.
    
    second = slow.next
    # The first part of the node list ends with a null
    slow.next = None

    # 2. reverse the second part of the list

    prev = None

    while second:

        temp = second.next
        second.next = prev
        prev =  second
        second = temp


    # 3. Merge the two lists

    first = head
    second = prev

    while second:

        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2
