# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        value = l1.val + l2.val
        if value % 10 != value:
            value = value % 10
            carry += 1
        temp = head = ListNode(value)
        l1 = l1.next
        l2 = l2.next
        while l1 is not None and l2 is not None:
            value = l1.val + l2.val
            if value % 10 == value:
                if carry > 0:
                    value += 1
                    carry -= 1
            else:
                value = value % 10
                if carry > 0 :
                    value += 1
                    carry -= 1
                carry += 1
            if value % 10 != value:
                value = value % 10
                carry += 1
            temp.next = ListNode(value)
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
        while l1 is not None:
            value = l1.val
            if carry > 0 :
                value += 1
                carry -= 1
                if value % 10 != value:
                    value = value - 10
                    carry += 1
            temp.next = ListNode(value)
            l1 = l1.next
            temp = temp.next
        while l2 is not None:
            value = l2.val
            if carry > 0 :
                value += 1
                carry -= 1
                if value % 10 != value:
                    value = value - 10
                    carry += 1
            temp.next = ListNode(value)
            l2 = l2.next
            temp = temp.next
        if carry > 0:
            temp.next = ListNode(1)
            carry -=1
            temp = temp.next
        return head



        
