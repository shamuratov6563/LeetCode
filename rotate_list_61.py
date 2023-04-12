from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # At first i found count of variables
        if head == None or head.next == None or k == 0:
            return head

        count = 0
        copy_node = head
        while copy_node != None:
            count += 1
            copy_node = copy_node.next

        # find move variable which is help me to how many items should be rotated
        move = k % count  # to find where to cut node
        if k == count or move == 0:
            return head

        count_1 = 0
        result = head
        copy_node = head
        prev = head
        while count != count_1:
            if count - count_1 == move:
                prev.next = None
                result = copy_node

            count_1 += 1
            if count_1 == count:
                copy_node.next = head

            prev = copy_node
            copy_node = copy_node.next

        return result


s = Solution()
n1 = ListNode(0)
n2 = ListNode(1)
n3 = ListNode(2)
n1.next = n2
n2.next = n3

a = s.rotateRight(head=n1, k=2)
