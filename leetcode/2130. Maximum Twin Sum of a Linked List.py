from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_value = 0
        first_half_stack = []

        slow = head
        fast = head

        while slow:
            if fast.next:
                fast = fast.next.next or fast.next
                first_half_stack.append(slow.val)

            else:
                new_val = slow.val + first_half_stack.pop(-1)
                max_value = max(max_value, new_val)

            slow = slow.next

        return max_value


solution = Solution()
node_1 = ListNode(1)
node_2 = ListNode(2, node_1)
node_4 = ListNode(4, node_2)
example_1 = ListNode(5, node_4)

node_3 = ListNode(3)
node_2 = ListNode(2, node_3)
node_22 = ListNode(2, node_2)
example_2 = ListNode(4, node_22)

node_10 = ListNode(100000)
example_3 = ListNode(1, node_10)

print(solution.pairSum(example_1))
print(solution.pairSum(example_2))
print(solution.pairSum(example_3))
