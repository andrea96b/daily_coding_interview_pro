import unittest
from sum_number_linked_list import Solution, ListNode

class Test(unittest.TestCase):

    def test_1(self):
        l1 = ListNode(2)
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

        self.assertEqual(s,807)

    def test_2(self):
        l1 = ListNode(9)
        l1.next = ListNode(9)
        l1.next.next = ListNode(9)

        l2 = ListNode(9)
        l2.next = ListNode(9)
        l2.next.next = ListNode(9)

        result = Solution().addTwoNumbers(l1, l2)
        i = 1
        s = 0
        while result:
            s += result.val * i
            i = i * 10
            result = result.next

        self.assertEqual(s,1998)

    def test_3(self):
        l1 = ListNode(1)

        l2 = ListNode(0)
        l2.next = ListNode(0)
        l2.next.next = ListNode(1)

        result = Solution().addTwoNumbers(l1, l2)
        i = 1
        s = 0
        while result:
            s += result.val * i
            i = i * 10
            result = result.next

        self.assertEqual(s,101)

    def test_4(self):
        l1 = ListNode(1)
        l2 = None

        result = Solution().addTwoNumbers(l1, l2)
        i = 1
        s = 0
        while result:
            s += result.val * i
            i = i * 10
            result = result.next

        self.assertEqual(s,1)


if __name__ == '__main__':
    unittest.main()