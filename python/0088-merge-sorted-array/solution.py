"""LeetCode 88 - Merge Sorted Array.

Approach: merge from the back. nums1 has room for m + n elements, with its
m real values at the front and n trailing zeroes; nums2 holds n values.
Walk two pointers (i at the end of nums1's real values, j at the end of
nums2) and a write pointer k at the very end of nums1, copying the larger
of the two pointed values into nums1[k] each step. Whatever remains of
nums2 is copied over; anything left in nums1 is already in place.

Time: O(m + n) — each element is moved once.
Space: O(1) — merged in place.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Merge nums2 into nums1 in place; nums1 has length m + n."""
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == "__main__":
    s = Solution()

    a = [1, 2, 3, 0, 0, 0]
    s.merge(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6], a

    a = [1]
    s.merge(a, 1, [], 0)
    assert a == [1], a

    a = [0]
    s.merge(a, 0, [1], 1)
    assert a == [1], a

    a = [4, 5, 6, 0, 0, 0]
    s.merge(a, 3, [1, 2, 3], 3)
    assert a == [1, 2, 3, 4, 5, 6], a

    a = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    s.merge(a, 6, [1, 2, 2], 3)
    assert a == [-1, 0, 0, 1, 2, 2, 3, 3, 3], a

    a = [2, 0]
    s.merge(a, 1, [1], 1)
    assert a == [1, 2], a

    print("All self-checks passed.")
