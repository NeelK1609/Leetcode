"""LeetCode 83 — Remove Duplicates from Sorted List.

Approach: the list is sorted, so any duplicates sit next to each other.
Walk once with a single pointer: whenever the current node and the next
node hold the same value, skip the next node by rewiring
``current.next``; otherwise advance. No extra storage is used.

Time: O(n) — one pass. Space: O(1) — in place.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


def _to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def _from_list(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


if __name__ == "__main__":
    sol = Solution()
    # LeetCode 83 examples + edge cases.
    assert _to_list(sol.deleteDuplicates(_from_list([1, 1, 2]))) == [1, 2]
    assert _to_list(sol.deleteDuplicates(_from_list([1, 1, 2, 3, 3]))) == [1, 2, 3]
    assert _to_list(sol.deleteDuplicates(_from_list([1, 1, 1]))) == [1]
    assert _to_list(sol.deleteDuplicates(_from_list([1, 2, 3]))) == [1, 2, 3]
    assert _to_list(sol.deleteDuplicates(_from_list([1]))) == [1]
    assert sol.deleteDuplicates(None) is None
    assert _to_list(sol.deleteDuplicates(_from_list([0, 0, 0, 1, 1, 2, 2, 2, 3]))) == [0, 1, 2, 3]
    assert _to_list(sol.deleteDuplicates(_from_list([-3, -3, -1, 0, 0]))) == [-3, -1, 0]
    print("All 8 checks passed.")
