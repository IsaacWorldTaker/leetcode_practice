from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head
        prev = head
        slow_counter = 0
        fast_counter = 0

        while slow:

            slow_counter += 1
            if fast.next:
                if fast.next.next:
                    fast_counter += 2
                    fast = fast.next.next
                else:
                    fast_counter = +1
                    fast = fast.next
            else:
                if fast_counter//2 > slow_counter:
                    slow.next = slow.next.next
                else:
                    prev.next = slow.next
                break
            prev = slow
            slow = slow.next
        return head


solution = Solution()

node_6 = ListNode(6)
node_2 = ListNode(2, node_6)
node_1 = ListNode(1, node_2)
node_7 = ListNode(7, node_1)
node_4 = ListNode(4, node_7)
node_3 = ListNode(3, node_4)
example_1 = ListNode(1, node_3)

node_4 = ListNode(4)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
example_2 = ListNode(1, node_2)

node_1 = ListNode(1)
example_3 = ListNode(2, node_1)

# result1 = solution.deleteMiddle(example_1)
# result2 = solution.deleteMiddle(example_2)
result3 = solution.deleteMiddle(example_3)
while result3:
    print(result3.val)
    result3 = result3.next
