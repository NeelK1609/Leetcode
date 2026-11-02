"""LeetCode 21 — Merge Two Sorted Lists.

Problem (in my own words): two singly linked lists are each already
sorted in increasing order. Splice their nodes together into a single
list that is also sorted, reusing the existing nodes rather than
creating new ones.

Approach: keep a dummy node in front of the result so the head never
needs a special case. Walk both lists with a tail pointer; at each step
attach whichever current node is smaller and advance that list. When one
list runs out, attach whatever remains of the other. This is a single
pass over both lists.

Time complexity: O(m + n), where m and n are the lengths of the lists.
Space complexity: O(1) extra space (nodes are reused, not copied).
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def from_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.mergeTwoLists(from_list([1, 2, 4]), from_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(s.mergeTwoLists(None, None)) == []
    assert to_list(s.mergeTwoLists(None, from_list([0]))) == [0]
    assert to_list(s.mergeTwoLists(from_list([5]), from_list([1, 2]))) == [1, 2, 5]
    assert to_list(s.mergeTwoLists(from_list([-3, 0]), from_list([-5, -1, 7]))) == [-5, -3, -1, 0, 7]
    print("All self-checks passed.")
