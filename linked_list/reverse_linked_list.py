# https://leetcode.com/problems/reverse-linked-list/description/


# GIVEN
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head):

    prev = None
    node = None

    def iteratively_reverse(head, node, prev):

        while head != None:

            node = ListNode(head.val)
            node.next = prev
            prev = node
            head = head.next

        return node


    def recursive_reverse(head, prev):

        if not head:
            return prev

        node = ListNode(head.val, None)

        node.next = prev

        prev = node

        return recursive_reverse(head.next, prev)

    # Uncomment to run iterative approach
    # return iteratively_reverse(head, node, prev)

    # Uncomment to run recursive approach
    # return recursive_reverse(head, prev)