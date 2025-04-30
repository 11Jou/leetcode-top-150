# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        y = head

        visited_node = {}

        while y is not None and y.next is not None:
            y = y.next
            if y in visited_node:
                return True
            visited_node[y] = y.val

        return False
        