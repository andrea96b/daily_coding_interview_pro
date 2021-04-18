
# This problem was recently asked by Microsoft:

# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        ret = ListNode(0)
        tmp = ret
        carry = 0

        while l1:
            tmpVal = l1.val + carry
            if l2:
                tmpVal = tmpVal + l2.val
                carry , tmpVal = divmod(tmpVal,10)
                l2 = l2.next
            else:
                carry = 0
            tmp.next = ListNode(tmpVal)
            tmp = tmp.next
            l1 = l1.next
        
        while l2:
            carry = 0
            tmp.next = ListNode(l2.val)
            tmp = tmp.next
            l2 = l2.next

        if carry > 0:
            tmp.next = ListNode(carry)

        return ret.next

if __name__=="__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    i = 1
    s = 0
    while result:
        s += result.val * i
        i = i * 10
        result = result.next
    print(s)
    pass
