from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        circular_list = []
        curr = head
        while curr is not None:
            circular_list.append(curr)
            curr = curr.next
        i = 0
        for _ in range(k % len(circular_list)):
            # prev
            prev = (i - 1 + len(circular_list)) % len(circular_list)
            # set new head
            circular_list[prev].next = circular_list[i]
            circular_list[prev-1].next = None
            i = prev
            head = circular_list[prev]

        return head


        # for _ in range(k):
        #     new_tail = tail.prev
solution = Solution()
# example_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# example_2 = ListNode(0, ListNode(1, ListNode(2)))
example_3 = ListNode(1, ListNode(2, ListNode(3)))

# print(solution.rotateRight(example_1, 2))
# print(solution.rotateRight(example_2, 4))
print(solution.rotateRight(example_3, 2000000000))
